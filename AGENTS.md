# Instruções para agentes

## Citações em arquivos Markdown

- Toda citação, fonte ou referência adicionada a um arquivo `.md` deve usar o link original completo da fonte.
- Preserve exatamente a URL consultada; não use encurtadores, links relativos, IDs internos ou referências sem destino.
- Prefira a forma `[título](https://dominio.exemplo/fonte-original)` com a URL da fonte real; quando a URL precisar ficar visível, use `<https://dominio.exemplo/fonte-original>`.
- Para notícias, mantenha a fonte original no front matter e inclua também uma indicação explícita da fonte no corpo do arquivo.
- Antes de finalizar, confira se o destino do link corresponde à página que sustenta a informação citada.

## Escrita do TCC

- Use `tcc.conf` como fonte dos dados básicos; campos vazios são pendências e não devem ser preenchidos por inferência.
- O Markdown é a fonte principal do conteúdo. Faça alterações de conteúdo nele antes de atualizar a versão LaTeX.
- Crie ou atualize LaTeX somente quando solicitado, escrevendo-o diretamente a partir do Markdown, sem conversores automáticos.
- Preserve o conteúdo e as fontes; não invente informações, resultados experimentais ou referências bibliográficas.
- Preserve `Template_UFFSTex/` como referência original. Adapte sua cópia em `tcc/latex/`, seguindo os comandos do template.
- Mantenha os arquivos LaTeX em `tcc/latex/capitulos/`, com nomes como `01-introducao.tex`. Use o mesmo nome-base no Markdown correspondente em `tcc/markdown/`.
- Mantenha a numeração explícita dos títulos no Markdown. No LaTeX, deixe a numeração a cargo dos comandos de seção do template, sem inserir números manualmente nos títulos.
- Ao atualizar um capítulo, limite as alterações ao capítulo e aos arquivos compartilhados necessários.
- Confira a correspondência entre fontes do Markdown, citações LaTeX e entradas bibliográficas.
- Para preencher ou corrigir referências bibliográficas, abra os links originais usando o MCP do Playwright e confira autoria e data na fonte. Se a página não informar a data, abra também os documentos vinculados, especialmente PDFs, e procure a ficha catalográfica, a folha de rosto e o expediente antes de registrar a referência como sem data.
- Distinga a data de publicação das datas de atualização da página e de criação ou modificação do arquivo. Não use estas últimas como data de publicação sem confirmação. Não transfira a data de um documento para a página que o hospeda: ao usar os dados do documento, cite seu título e sua URL original completa e mantenha a correspondência entre Markdown e BibTeX.
- Ao mover ou renomear arquivos versionados, use `git mv` e preserve seu conteúdo antes de aplicar os ajustes necessários.
