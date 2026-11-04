# Regras de escrita e revisão do TCC

Este registro reúne as regras acordadas com o autor e serve de referência para revisões pela IA. Apesar do nome do arquivo, nem todas as regras são exigências da ABNT: a natureza de cada grupo está indicada abaixo. Não é uma lista completa de requisitos normativos nem comprova que o TCC já foi revisado.

## Norma ABNT verificada

A cópia de consulta está em `docs/abnt/nbr-14724-2024-corrigida-2025.pdf`, com versão Markdown de mesmo nome-base. Consulte o PDF quando a interpretação depender da diagramação, dos exemplos ou de uma possível falha da conversão. Procedência e conferências estão em `docs/abnt/README.md`.

- **N01 — Primeira menção de siglas:** apresentar o nome completo seguido da sigla entre parênteses na primeira ocorrência no texto, conforme a seção 5.6 da [ABNT NBR 14724:2024, versão corrigida em 01.04.2025](https://www.gedweb.com.br/aplicacao/usuario/asp/detalhe_nbr.asp?nbr=21434). A norma não determina nesse item a tradução de siglas estrangeiras nem a reapresentação a cada seção.

## Preferências editoriais do autor

- **E01 — Preservar a escrita:** manter a estrutura, o vocabulário e a forma de expressão do autor. Corrigir ortografia, gramática e interpretações incorretas; não reescrever apenas por preferência de estilo.
- **E02 — Complementos solicitados:** incorporar ao texto proposto os complementos explicitamente pedidos, inclusive entre parênteses, de modo breve, claro e sustentado pelas fontes. Não acrescentar conteúdo por iniciativa da IA como se fosse do autor.
- **E03 — Separar proposta e explicações:** deixar explicações das correções, ressalvas e observações adicionais fora do texto proposto. Quando solicitada comparação, preservar o original integralmente e colocar apenas o texto revisado em um bloco delimitado por três crases.
- **E04 — Uso posterior de siglas:** após a apresentação inicial no texto completo do TCC, usar apenas a sigla nas menções seguintes, sem reiniciar a apresentação a cada seção ou capítulo. Conferir as ocorrências anteriores antes de expandir uma sigla. Essa preferência complementa N01.
- **E05 — Autoria da fundamentação:** a fundamentação teórica é escrita pelo autor. A IA pode preparar roteiros, perguntas e tópicos identificados como sugestões, além de revisar o texto existente e atender a complementos pontuais solicitados; isso não autoriza redigir novas seções de fundamentação por iniciativa própria.
- **E06 — Foco dos trabalhos relacionados:** manter cada subseção centrada no estudo analisado. Reservar a justificativa geral da escolha do TabPFN à introdução. Preservar comparações já escritas pelo autor e consultar `templates/guia-trabalhos-relacionados.md` ao incorporar estudos.
- **E07 — Ordem dos arquivos de apoio:** durante a elaboração, nos arquivos `fundamentacao-teorica.md`, manter primeiro o roteiro de leitura, depois as observações sobre a revisão e as propostas da IA, quando existirem, e por último “Anotações do autor”. O texto autoral deve ocupar o fim do arquivo, sem comentários ou propostas da IA depois dele. Preservar os textos existentes ao reorganizar; propostas para comparação continuam em blocos com três crases, conforme E03.

- **E08 — Proposta cumulativa até a versão final:** não apagar nem esvaziar a versão proposta pela IA quando o autor aprovar um trecho. Atualizar a mesma proposta progressivamente, preservando os trechos aprovados e incorporando a revisão das novas partes escritas pelo autor e os complementos que ele solicitar. Durante a elaboração, manter o texto proposto no bloco com três crases, conforme E03, e as observações fora dele. Somente quando o autor indicar que o texto está concluído, deixar o arquivo apenas com o subtópico numerado, seu título e o texto consolidado, seguindo a numeração do TCC. Nessa etapa, retirar o rótulo de versão da IA, o bloco de código, a seção “Anotações do autor” e as seções de apoio (roteiro e observações). Antes de retirar as anotações, conferir que o conteúdo que o autor decidiu aproveitar e suas fontes foram incorporados ao texto final; não descartar pendências por inferência. A aprovação de um trecho não equivale à conclusão do texto inteiro nem autoriza a IA a escrever sua continuação por iniciativa própria.

- **E09 — Tradução de termos técnicos:** antes de traduzir, pesquisar na internet o uso da tradução na literatura da área, comparando múltiplas fontes independentes de autores ou instituições diferentes, com preferência por artigos científicos, livros e materiais acadêmicos de computação ou geociências, conforme o contexto. Um único artigo, livro ou material não basta para afirmar que a tradução é comum; cópias ou reproduções da mesma origem não constituem evidências independentes. Comparar variantes de tradução, recorrência e contexto de uso; se as fontes divergirem, registrar a divergência sem apresentar uma escolha como consenso. A equivalência literal ou um dicionário isolado não comprovam uso consolidado. Adotar a tradução quando houver evidências adequadas; caso contrário, manter o termo original e explicá-lo brevemente na primeira ocorrência. Registrar os links originais das fontes nas observações de apoio, fora do texto proposto, e manter consistência de terminologia e siglas. Não afirmar que uma tradução inexiste apenas porque não foi encontrada. Esta é uma preferência editorial do autor, não uma exigência atribuída à ABNT.

## Convenções do projeto

- **P01 — Formato dos artigos:** usar apenas Markdown e matemática LaTeX nos arquivos Markdown dos artigos, sem tags HTML. Preservar conteúdo, dados, legendas e relações entre células ao adaptar tabelas.
- **P02 — Títulos e capítulos:** manter a numeração explícita dos títulos do TCC em Markdown; no LaTeX, deixar a numeração a cargo dos comandos do template. O capítulo 2, Revisão Bibliográfica, reúne conceitos e fundamentação; o capítulo 3, Trabalhos Relacionados, reúne análise e comparação dos estudos.
- **P03 — Fontes e referências:** preservar conteúdo e fontes, sem inventar informações, resultados ou referências. Toda fonte adicionada a Markdown deve apontar para a URL original completa efetivamente consultada. Manter correspondência entre as fontes do Markdown, as citações LaTeX e as entradas bibliográficas. As regras de conferência bibliográfica e de atualização do LaTeX permanecem em `AGENTS.md`.
- **P04 — Evidências e limites:** distinguir propostas, atividades executadas e resultados demonstrados; separar limitações relatadas pelas fontes de observações do autor ou da IA. Conferir a coerência com `docs/decisoes-projeto.md` ao revisar o conteúdo.

- **P05 — Marcadores de destaque em Markdown:** usar `_texto_` para itálico (`MD049`, `style: underscore`) e `**texto**` para negrito (`MD050`, `style: asterisk`).

## Como usar na revisão

- Conferir cada regra aplicável contra o texto solicitado, lendo o texto completo quando a verificação exigir contexto, como em E04.
- Informar problemas com o ID da regra, o arquivo e o trecho afetado, acompanhados de uma correção mínima proposta. Não declarar conformidade de partes não examinadas.
- Distinguir erro normativo, descumprimento de preferência editorial e sugestão opcional. Uma sugestão da IA não se torna regra sem decisão do autor.
- Ao acrescentar regras descobertas durante a escrita, manter IDs estáveis e indicar sua natureza. Para exigências normativas, registrar norma, edição, item e URL original consultada; se não houver confirmação, marcar como pendente, sem apresentá-la como obrigação da ABNT.
- **Pendência — siglas estrangeiras:** o item 5.6 consultado não resolve a escolha entre sigla original e traduzida. As sugestões discutidas na conversa não constituem uma regra geral aprovada para tradução.
