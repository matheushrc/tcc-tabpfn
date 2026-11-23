# tcc-tabpfn

Pesquisa e escrita do TCC sobre o TabPFN com dados espectrais de satélite. O escopo vigente, as decisões e as pendências estão em `docs/decisoes-projeto.md`; os dados básicos, em `tcc.conf`. Este arquivo só aponta onde cada coisa está e não registra estados (pendente, finalizado, compilado).

## Mapa do repositório

| Pasta ou arquivo | Conteúdo |
| --- | --- |
| `tcc/markdown/` | Capítulos em Markdown, que são a fonte do conteúdo. |
| `tcc/latex/` | Projeto LaTeX: `principal.tex`, `capitulos/` com os mesmos nomes-base do Markdown, `bibliografia.bib` e a classe `UFFStex.cls`. |
| `Template_UFFSTex/` | Template original da faculdade; deve ser preservado. |
| `templates/` | Exemplos de escrita, como o TCC de referência em `templates/natanael/`; não integram os capítulos. |
| `fontes/` | Material de apoio à escrita: artigos convertidos (`artigos/`, um por pasta, e `artigos-descartados/`), normas ABNT (`normas/`), notícias e PDFs da revisão bibliográfica (locais). Índice em `fontes/README.md`. |
| `docs/` | Documentação do projeto. Índice gerado em `docs/SUMARIO.md`; regras de escrita em `docs/PADRAO-DOCS.md`. |
| `datasets/` | Dados locais, fora do git; cada pasta tem seu `README.md`. |
| `scripts/` | Scripts auxiliares (`scripts/README.md`). |
| `AGENTS.md`, `ABNT.md` | Regras de trabalho da IA e regras editoriais. |

O fluxo de escrita (`fontes/` → `tcc/markdown/` → `tcc/latex/capitulos/`) e a compilação com Docker estão descritos em `AGENTS.md`.
