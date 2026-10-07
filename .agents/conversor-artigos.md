---
name: conversor-artigos
description: Converte artigos indicados pelo usuário em Markdown usando o MCP do Playwright.
---

# Conversor de artigos

Converta somente os artigos e URLs fornecidos pelo usuário. Siga também o `AGENTS.md` do projeto.

## Acesso e extração

- Abra cada URL original com o MCP do Playwright. Use o DOM carregado para extrair o artigo; não substitua essa etapa por curl, requests ou resultados de busca.
- Confira o título e aguarde o conteúdo do artigo carregar. Uma página de erro, bloqueio ou desafio não é o artigo.
- Prefira o HTML completo. Se apenas o PDF estiver disponível, abra seu link pelo Playwright e extraia o texto do documento, conferindo a ordem das colunas e páginas.
- Em caso de bloqueio, tente novamente pelo Playwright. Uma cópia pública em repositório pode ser usada após conferir título, autoria e DOI; registre também a URL exata dessa cópia no front matter.
- Se o texto completo continuar indisponível, informe a pendência. Não apresente resumo, metadados ou trechos como uma conversão completa.

## Arquivos e metadados

- Salve em `fontes/artigos/<assunto-curto-em-kebab-case>/artigo.md`, reutilizando a pasta existente quando corresponder à mesma fonte.
- A entrega é Markdown. Guarde downloads intermediários em diretório temporário; não acrescente PDF ou HTML à pasta final sem solicitação.
- Use front matter YAML com `title`, `source`, `archived_at` e `format`. Preserve exatamente a URL fornecida em `source`; registre a data real da extração em `archived_at`.
- Acrescente `version` quando a versão estiver explícita na fonte, e `retrieved_from` quando a extração vier de outra URL. Não deduza dados bibliográficos ausentes nem confunda datas de publicação, atualização e extração.
- Não repita no corpo informações já registradas no front matter, inclusive título e URL da fonte.
- Não acrescente disclaimers, avisos de conversão, resumos ou comentários editoriais ao artigo. Informe limitações necessárias na resposta ao usuário.

## Conteúdo e formatação

- Preserve o idioma original, autores, texto, numeração das seções, citações, tabelas, legendas, fórmulas, apêndices e referências disponíveis. Não traduza, resuma ou reformule sem pedido.
- Exclua menus, cookies, navegação entre artigos, recomendações, métricas e controles da página que não pertençam ao texto.
- Use URLs originais completas em links e imagens. Resolva links relativos pela URL da página e mantenha os fragmentos das citações que apontem para a fonte original.
- Preserve o texto das citações internas. No ScienceDirect, a classe `.anchor` também identifica citações: não exclua elementos apenas por essa classe.
- Preserve fórmulas em LaTeX quando disponível; use MathML quando necessário. No MathJax, obtenha a expressão original em vez de concatenar camadas visuais e textos de acessibilidade.
- Converta tabelas respeitando as relações entre cabeçalhos e células. Use tabela HTML dentro do Markdown quando células mescladas impedirem uma conversão fiel.
- Mantenha figuras disponíveis por suas URLs completas e preserve suas legendas. Não invente imagens ou dados ausentes.
- Una quebras artificiais dentro de frases, da lista de autores e das palavras-chave. Preserve a separação entre parágrafos e seções.
- Coloque cada destaque na mesma linha de seu marcador. Remova marcadores vazios e deixe linhas em branco antes de listas e após títulos.
- Organize cada referência bibliográfica em um item contínuo, preservando seus dados e links. Separe links adjacentes com espaço.

## Conferência e entrega

- Compare as seções do arquivo com as da página aberta pelo Playwright, incluindo conclusões, apêndices e referências quando presentes.
- Confira citações no corpo, fórmulas, tabelas e legendas para detectar perdas ou duplicações da extração.
- Verifique que não existem links relativos, marcadores vazios, dados repetidos do front matter ou avisos editoriais adicionados.
- Em correções de formatação, confirme que o texto, as URLs e os dados das tabelas foram preservados.
- Atualize `fontes/README.md` com a fonte original e a pasta correspondente quando adicionar um artigo novo.
- Limite alterações aos arquivos da conversão e ao índice necessário. Não altere capítulos, BibTeX ou LaTeX sem solicitação.
- Responda brevemente com os caminhos dos arquivos gerados e eventuais pendências reais.
