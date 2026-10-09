# TCC de referência — Natanael Henrik Zago

Documento: *Usando esquema GraphQL para geração de consultas de forma aleatória*, Universidade Federal da Fronteira Sul, 2023. Autor: Natanael Henrik Zago. Orientador: Samuel da Silva Feitosa.

`principal.tex` é uma **reconstrução editável a partir do PDF**, escrita com a classe da pasta `Template_UFFSTex/`. A cópia local `UFFStex.cls` preserva o conteúdo da classe original. O ano do documento foi fixado em 2023. O PDF fornecido permanece intacto em `tcc-original.pdf`.

Os seis capítulos estão em `capitulos/`, com transcrição de apoio em `markdown/`. Os elementos pré-textuais estão em `pretextuais/`; as três figuras e o logotipo foram extraídos do PDF para `figuras/`. O cronograma foi reconstruído como tabela LaTeX editável. Sumário, listas e citações são gerados pelo LaTeX, em vez de incluídos como páginas do PDF.

Para compilar, abra esta pasta e execute:

```powershell
pdflatex -interaction=nonstopmode -halt-on-error principal.tex
bibtex principal
pdflatex -interaction=nonstopmode -halt-on-error principal.tex
pdflatex -interaction=nonstopmode -halt-on-error principal.tex
```

No Overleaf, envie esta pasta preservando as subpastas e selecione `principal.tex` como documento principal.

## Fidelidade e referências

A reconstrução preserva o conteúdo do trabalho de referência, incluindo sua autoria, data, banca, resumos, capítulos, figuras e cronograma. Erros de redação do documento, como “repeitando” e “QraphQL”, foram mantidos; a transcrição não é uma revisão acadêmica do trabalho. As imagens permanecem rasterizadas como no PDF.

As doze referências estão em `bibliografia.bib`, separado da bibliografia do TCC de TabPFN. Consulte `conferencia-referencias.md` para as fontes completas e as correções de metadados. `transcricao-pdf.txt` preserva a extração do documento, inclusive a lista bibliográfica original. A numeracão das citações é preservada pela ordem declarada em `principal.tex`.

Os fontes originais do Natanael não foram disponibilizados. Esta reconstrução não é seu código-fonte original, e paginação, quebras de linha e composição visual podem diferir. A ficha mantém “33 f.” como informação histórica do original, sem afirmar que a reconstrução tem o mesmo número de páginas. O título em inglês não foi inferido.

## Verificação da reconstrução

Compilação local concluída em 9 de outubro de 2026 com pdfLaTeX e BibTeX, gerando `principal.pdf` com 38 páginas. Não restaram citações ou referências cruzadas indefinidas. Foram conferidos 52 trechos de prosa e itens contra a transcrição de apoio, os seis capítulos, as três figuras, o cronograma e as doze chaves bibliográficas. O PDF original e a classe UFFS foram preservados sem alterações.

Capa, figuras e cronograma foram inspecionados visualmente. O logotipo preserva a máscara de transparência do PDF. Permanecem avisos de caixas da classe e pequenas extrapolações de margem em títulos e parágrafos; nenhum bloco de texto foi encontrado fora das páginas. A consulta direta da referência KTH continua pendente, conforme `conferencia-referencias.md`.

A estrutura de referência distingue **2 — Revisão Bibliográfica** (conceitos) de **3 — Trabalhos Relacionados** (análise dos estudos), seguida de metodologia, cronograma e considerações finais. Seu conteúdo não integra os capítulos autorais do TCC sobre TabPFN.
