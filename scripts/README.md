# Exportação do PDF original do GEDWeb

Estes são os dois helpers do fluxo final, testado com a NBR 14724:2024, versão corrigida de 2025, pelo acesso institucional autorizado da UFFS. O resultado preserva texto, fontes, imagens, vetores e marcas institucionais; não usa OCR nem reconstrói páginas a partir de capturas de tela.

## Arquivos

- `exportar-pdf-gedweb.playwright.js`: função executada pelo MCP do Playwright na aba autenticada do visualizador.
- `receber-pdf-gedweb.py`: receptor HTTP temporário em `127.0.0.1:37660`; abre o PDF com a senha recebida e salva uma cópia sem criptografia, validando todas as páginas.

## Execução

1. Pelo MCP Playwright, abra o [catálogo da UFFS](https://consulta.uffs.edu.br/), pesquise o número da norma na base Target GEDWeb e autentique-se com seu acesso institucional. Confira a versão no histórico e abra o visualizador. Selecione essa aba com `browser_tabs`.
2. No terminal, a partir da raiz do projeto, inicie o receptor. É necessário ter PyMuPDF (`fitz`) no ambiente Python:

   ```sh
   python scripts/receber-pdf-gedweb.py --output docs/abnt/nbr-14724-2024-corrigida-2025.pdf
   ```

3. Em até 60 segundos, execute `browser_run_code_unsafe` do MCP Playwright passando:

   ```json
   {
     "filename": "/home/matheus/Documents/projetos/tcc-tabpfn/scripts/exportar-pdf-gedweb.playwright.js"
   }
   ```

4. Confira o resultado do helper: deve indicar `encrypted: false`, o número de páginas e a validação de texto e renderização. O receptor atende uma requisição e encerra. Se expirar, reinicie-o antes de executar o helper novamente.
5. Abra o PDF salvo com `doc_open` do MCP PDFCraft. Para converter, descubra `doc_export_office` por `tool_search` e execute com `tool_call`, passando `doc` e o caminho absoluto de destino terminado em `.md`. Confira o texto com `text_extract` e extraia imagens com `doc_export_all_images`. Revise tabelas, títulos e equações contra o PDF; a exportação automática não garante a organização correta desses elementos.

O argumento `--output` escolhe outro destino. O receptor aceita `--port`, mas alterar a porta exige atualizar a URL local no helper JavaScript. Um arquivo já existente no destino será substituído somente depois de o novo PDF passar pelas verificações.

## Como funciona

1. O helper instala uma observação em `Worker.prototype.postMessage` antes de recarregar a aba. O leitor recebe a senha do documento na carga inicial (`data.source.password`) ou em uma resposta posterior (`data.password`).
2. Quando o documento termina de carregar, o helper lê os bytes originais por `doc.ba.pdfDocument.getData()`. Essa chamada sozinha continua devolvendo o arquivo criptografado.
3. O arquivo e a senha são enviados em memória ao receptor local. A senha do PDF pode mudar a cada carregamento: uma senha capturada abriu o arquivo da mesma carga e não abriu o de uma carga anterior. Portanto, capture sempre os bytes e a senha juntos. A senha do PDF é distinta das credenciais de login; os helpers não precisam ler o `.env` nem registrar essa senha.
4. O receptor usa `fitz.Document.authenticate` e salva com `PDF_ENCRYPT_NONE`. Antes de substituir o destino, compara o texto e os pixels renderizados de cada página com o original autenticado.

A implementação depende da estrutura atual do PDF.js Express usado pelo GEDWeb, em especial do iframe `webviewer` e do caminho interno `doc.ba.pdfDocument`. Se esses componentes mudarem ou o documento deixar de carregar, o helper deve falhar e ser revisto, sem recorrer automaticamente a OCR ou apresentar uma reprodução como arquivo original.

Os scripts preservam a sessão autorizada do usuário e não contêm senhas fixas. Credenciais e arquivos temporários do navegador ficam fora do versionamento. A senha capturada é removida da variável usada para transferência; a instrumentação desaparece ao fechar a aba/contexto do navegador.
