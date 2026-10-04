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
- Deixe a numeração dos títulos para o LaTeX.
- Ao atualizar um capítulo, limite as alterações ao capítulo e aos arquivos compartilhados necessários.
- Confira a correspondência entre fontes do Markdown, citações LaTeX e entradas bibliográficas.
- Ao mover ou renomear arquivos versionados, use `git mv` e preserve seu conteúdo antes de aplicar os ajustes necessários.
