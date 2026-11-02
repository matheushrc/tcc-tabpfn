# Normas ABNT para consulta

## NBR 14724 — Trabalhos acadêmicos

- **Edição:** quarta, de 16.12.2024; versão corrigida em 01.04.2025, incorporando a Errata 1.
- **Fonte:** [registro da NBR 14724 no Target GEDWeb](https://www.gedweb.com.br/aplicacao/usuario/asp/detalhe_nbr.asp?nbr=21434), acessado pelo [catálogo da UFFS](https://consulta.uffs.edu.br/).
- **Obtenção:** 02.11.2026, na sessão institucional autenticada pelo autor. O histórico do GEDWeb indica a edição em vigor e a correção de abril de 2025.
- **PDF:** `nbr-14724-2024-corrigida-2025.pdf`, 16 páginas físicas, incluindo elementos preliminares; a numeração do conteúdo normativo vai de 1 a 12.
- **Markdown:** `nbr-14724-2024-corrigida-2025.md`, texto extraído pelo MCP do PDFCraft, sem OCR. Sumário, hierarquia do esquema, tabelas de exemplos e equações foram adaptados para Markdown e matemática LaTeX; o gráfico foi extraído pelo PDFCraft para `figuras/`.
- **Integridade:** o PDF foi obtido diretamente do leitor, aberto com a senha que a própria sessão forneceu e salvo sem criptografia, preservando as marcas institucionais, fontes, texto e elementos gráficos. Texto e renderização das 16 páginas foram comparados com o original autenticado e são idênticos. Não é uma reconstrução por imagens.
- **SHA-256 do PDF salvo:** `55e324185a33c9ccfdef522979ff2a74fb689cedcfb4c978d06e5981d33f7663`.

O PDF é a referência para conferir a transcrição e a disposição visual dos exemplos. As regras editoriais adotadas pelo projeto ficam em `ABNT.md`, na raiz; guardar uma norma aqui não significa que todos os requisitos já foram conferidos no TCC.

## Repetir a obtenção

1. Abra a versão desejada pelo MCP do Playwright, usando o acesso autorizado da UFFS e verificando o histórico da norma. Selecione a aba do visualizador.
2. Inicie o receptor local, que atende uma exportação e encerra: `python scripts/receber-pdf-gedweb.py --output docs/abnt/<nome>.pdf`. Ele depende de PyMuPDF (`fitz`) e espera por até 60 segundos.
3. Execute o MCP Playwright `browser_run_code_unsafe` com `filename` apontando para o caminho absoluto de `scripts/exportar-pdf-gedweb.playwright.js`. Ele recarrega a aba para observar o carregamento autorizado do documento. O helper depende da estrutura atual do PDF.js Express do GEDWeb e deve ser revisto se o visualizador mudar.
4. Abra o arquivo no MCP do PDFCraft com `doc_open`. Use `doc_export_office` para Markdown e `doc_export_text`/`text_extract` para conferir o texto. As ferramentas adicionais são descobertas por `tool_search` e executadas por `tool_call`.
5. Extraia imagens com `doc_export_all_images`; confira esquema, tabelas e fórmulas no PDF, pois a exportação automática pode interpretar texto corrido como tabelas ou separar títulos e números.

Os helpers não gravam a senha do PDF. Credenciais do autor, arquivos de sessão e resultados intermediários não integram estes documentos de consulta.
