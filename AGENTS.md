# Instruções para agentes

## Conversão de artigos

- Para converter artigos em Markdown, siga o agente definido em `.agents/conversor-artigos.md`.

## Decisões e coerência do projeto

- Sempre que o autor apresentar uma nova decisão, ideia ou mudança de escopo, consulte `docs/decisoes-projeto.md`, `tcc.conf` e os trechos pertinentes da introdução e da metodologia antes de incorporá-la ao trabalho.
- Compare a proposta com o problema de pesquisa, as hipóteses, os objetivos, os dados de referência e o protocolo de avaliação. Informe de forma breve se ela está alinhada, depende de confirmação ou altera o escopo, explicando a consequência concreta e indicando os IDs afetados no registro.
- Distinga decisões do autor de sugestões da IA. Não transforme uma sugestão, possibilidade ou pergunta em compromisso assumido. Se a intenção for ambígua e afetar o escopo, esclareça o ponto com o autor; continue as atividades que não dependam dessa definição.
- Registre decisões e ideias expressas em `docs/decisoes-projeto.md`, usando um ID estável, estado, condições de viabilidade e evidências necessárias. Atualize o histórico com data, IDs afetados, motivo e evidência; preserve decisões anteriores e registre explicitamente sua substituição ou descarte.
- Uma nova decisão explícita do autor pode revisar o escopo anterior. Não a rejeite apenas por divergir do registro: identifique o que mudou e atualize os compromissos afetados. Não escolha por conta própria uma mudança de título, tarefa ou objetivo para resolver incompatibilidades entre os dados e a proposta.
- Verifique especialmente a distinção entre composição geoquímica e mineralógica, rótulos independentes e mapas derivados, superfície e subsuperfície, observações e valores interpolados ou previstos. Confira também compatibilidade espacial e temporal, harmonização entre bases e independência dos dados de teste quando esses aspectos forem afetados.
- Mantenha hipóteses como afirmações a testar e intenções como entregas propostas. Marque uma atividade como realizada somente com evidência identificável; registre resultados negativos, limitações e atividades não executadas sem apresentá-los como sucesso ou omiti-los para manter a proposta original.
- Ao alterar o conteúdo do TCC, confira sua coerência com o registro e ajuste os arquivos Markdown pertinentes dentro do escopo autorizado. Atualize LaTeX somente quando solicitado, diretamente a partir do Markdown; se houver versões ou capítulos afetados fora do pedido, indique a pendência. Confira as citações e as entradas de `tcc/latex/bibliografia.bib` quando fontes forem adicionadas ou alteradas.
- Antes de finalizar uma alteração, confira se o texto distingue o que foi proposto, executado e demonstrado. Na revisão final do TCC, confronte cada compromisso registrado com as evidências e ajuste introdução, metodologia e conclusões ao trabalho efetivamente realizado.

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
- Siga a separação adotada no TCC de Natanael: capítulo 2, **Revisão Bibliográfica**, para conceitos e fundamentação; capítulo 3, **Trabalhos Relacionados**, para análise e comparação dos artigos. Consulte `templates/guia-trabalhos-relacionados.md` ao incorporar estudos; preserve os textos e suas fontes.
- Reúna exemplos de escrita em `templates/`, distinguindo-os do conteúdo autoral. Consulte `templates/natanael/README.md` antes de usar o trabalho de referência: incluir páginas de um PDF em LaTeX não recupera os fontes editáveis originais. Não apresente uma reprodução como fonte original ou transcrição editável, nem recrie `introducao.example.md`, excluído pelo autor.
- Mantenha em `tcc/latex/bibliografia.bib` apenas referências efetivamente citadas no TCC. Referências de pesquisas, decisões ou extensões opcionais permanecem nos documentos correspondentes até serem usadas nos capítulos. Ao incorporar ou remover citações, confira chaves ausentes e entradas sem uso.
- Confira a correspondência entre fontes do Markdown, citações LaTeX e entradas bibliográficas.
- Para preencher ou corrigir referências bibliográficas, abra os links originais usando o MCP do Playwright e confira autoria e data na fonte. Se a página não informar a data, abra também os documentos vinculados, especialmente PDFs, e procure a ficha catalográfica, a folha de rosto e o expediente antes de registrar a referência como sem data.
- Distinga a data de publicação das datas de atualização da página e de criação ou modificação do arquivo. Não use estas últimas como data de publicação sem confirmação. Não transfira a data de um documento para a página que o hospeda: ao usar os dados do documento, cite seu título e sua URL original completa e mantenha a correspondência entre Markdown e BibTeX.
- Ao mover ou renomear arquivos versionados, use `git mv` e preserve seu conteúdo antes de aplicar os ajustes necessários.

## Commits da escrita

- Ao incorporar artigos ao TCC, faça um commit separado por artigo, reunindo Markdown, LaTeX solicitado e ajustes bibliográficos correspondentes. Separe a preparação da estrutura dos capítulos das adições de estudos.
- Quando o autor pedir para commitar o estado atual antes de iniciar uma tarefa, faça esse commit antes das novas alterações. Exclua do versionamento registros temporários de ferramentas.
- Use `git commit --amend` quando solicitado para corrigir o último commit; confira seu conteúdo antes da alteração e informe o novo hash. Não trate uma solicitação pontual de amend como autorização permanente para reescrever o histórico.
