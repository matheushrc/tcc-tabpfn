"""Recebe o PDF e a senha da sessão autorizada, preservando texto e gráficos.

Inicie antes de executar exportar-pdf-gedweb.playwright.js pelo MCP Playwright.
Nenhuma senha é gravada em disco ou mostrada na saída.
"""
import argparse
import base64
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from pathlib import Path
import tempfile
import fitz

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output', type=Path, required=True)
parser.add_argument('--port', type=int, default=37660)
args = parser.parse_args()
output = args.output.resolve()

class Receiver(BaseHTTPRequestHandler):
    def log_message(self, *_):
        pass

    def do_POST(self):
        try:
            if self.path != '/export':
                raise ValueError('Destino inválido')
            length = int(self.headers.get('Content-Length', 0))
            if not 0 < length <= 64 * 1024 * 1024:
                raise ValueError('Tamanho inválido')
            request = json.loads(self.rfile.read(length))
            data = base64.b64decode(request['pdf'], validate=True)
            if not data.startswith(b'%PDF-'):
                raise ValueError('O conteúdo recebido não é PDF')
            with fitz.open(stream=data, filetype='pdf') as source:
                if source.needs_pass and not source.authenticate(request['password']):
                    raise ValueError('Senha do documento não autenticou')
                if len(source) != request['pages']:
                    raise ValueError('Número de páginas inconsistente')
                output.parent.mkdir(parents=True, exist_ok=True)
                with tempfile.NamedTemporaryFile(dir=output.parent, suffix='.pdf', delete=False) as tmp:
                    temp = Path(tmp.name)
                try:
                    source.save(temp, encryption=fitz.PDF_ENCRYPT_NONE)
                    with fitz.open(temp) as saved:
                        assert not saved.needs_pass and len(saved) == len(source)
                        for before, after in zip(source, saved):
                            assert before.get_text() == after.get_text(), 'Texto alterado'
                            assert before.get_pixmap().samples == after.get_pixmap().samples, 'Renderização alterada'
                    temp.replace(output)
                finally:
                    temp.unlink(missing_ok=True)
                result = {'output': str(output), 'pages': len(source), 'encrypted': False,
                          'verified': 'Texto e renderização idênticos em todas as páginas'}
            body = json.dumps(result, ensure_ascii=False).encode()
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(body)
            print(body.decode(), flush=True)
        except Exception as error:
            # Mensagens controladas; não imprimir requisição ou valores de credenciais.
            self.send_error(400, type(error).__name__)
            print('Falha na exportação: ' + type(error).__name__, flush=True)

server = HTTPServer(('127.0.0.1', args.port), Receiver)
server.timeout = 60
print('Aguardando uma exportação local por até 60 segundos.', flush=True)
server.handle_request()
server.server_close()
