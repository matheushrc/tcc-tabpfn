# Organização do projeto

Este repositório reúne a pesquisa e a escrita do TCC de Matheus Henrique Rodrigues da Costa sobre avaliação do TabPFN para classificação litológica e predição da composição química a partir de dados espectrais de satélite.

## Texto e apresentação

O conteúdo principal está em `tcc/markdown/`. Os capítulos escritos são `01-introducao.md` e `03-trabalhos-relacionados.md`. `02-revisao-bibliografica.md` reserva a fundamentação conceitual, ainda pendente.

O projeto de apresentação está em `tcc/latex/`, com `principal.tex` como ponto de entrada, `capitulos/` para os capítulos, `bibliografia.bib` para referências e `figuras/` para imagens. A IA escreve o LaTeX diretamente a partir do Markdown quando solicitado ou quando o autor finalizar explicitamente um capítulo ou seção, conforme P06 de `ABNT.md`. Nesse último caso, incorpora também o texto final ao capítulo Markdown correspondente. Os nomes-base dos capítulos correspondem entre os dois formatos, com ordem numérica antes do nome, como `01-introducao`.

O Markdown é a fonte do conteúdo; revisões originadas no PDF devem ser aplicadas nele antes de atualizar o LaTeX. A numeração exibida no trabalho é responsabilidade do LaTeX. Não há conversor automático nem sincronização automática entre os formatos.

`tcc.conf` centraliza os dados básicos em texto `chave=valor`. Os dados são transcritos para o projeto LaTeX ao atualizar os pares autorizados; campos vazios representam pendências. O projeto atual é uma versão parcial de TCC I: título em inglês, palavras-chave, resumo e abstract serão definidos ao final dessa etapa.

## Template e referências de escrita

`Template_UFFSTex/` contém o template original da faculdade e deve ser preservado. A classe em `tcc/latex/UFFStex.cls` é uma cópia desse original. As adaptações do trabalho ficam no projeto em `tcc/latex/`, mantendo o sistema de citações do template.

`templates/natanael/` reúne o PDF integral e um projeto LaTeX de reprodução do TCC de Natanael Henrik Zago, orientado pelo mesmo professor, conforme identificação fornecida pelo autor deste projeto. Servem para consultar estrutura e escrita; não integram os capítulos autorais.

## Pesquisa e experimentos

`docs/` reúne leituras, ideias, avaliação da introdução e planejamento. `reports/` contém levantamentos de conjuntos de dados. `fontes/artigos/` guarda os sete estudos selecionados em pastas numeradas na sequência de preparação indicada em `fontes/README.md`; cada pasta possui `artigo.md` e `trabalhos-relacionados.md`, com roteiro de leitura; `fontes/artigos-descartados/` preserva, sem numeração, os estudos removidos da seleção. `fontes/noticias/` guarda fontes jornalísticas. Esses materiais apoiam a escrita, mas não são capítulos finais. A fundamentação será escrita pelo autor; os roteiros da IA contêm somente tópicos e perguntas, e os dois textos de análise já existentes foram preservados.

`datasets/` contém dados locais e está ignorado pelo Git. `mineshafts.ipynb` contém exploração inicial dos dados. `main.py` ainda é o exemplo inicial do projeto; não há pipeline completo de treinamento ou extração de imagens implementado. O ambiente Python é descrito por `pyproject.toml`, `.python-version` e `uv.lock`.

## Documentação e verificação

`README.md` orienta a navegação. `AGENTS.md` contém regras operacionais para a IA. `ORGANIZACAO_TCC.md` registra o plano e o resultado de sua execução. Evitar repetir árvores de arquivos e explicações extensas nas instruções para agentes.

O projeto LaTeX foi preparado para revisão no Overleaf com `principal.tex` como documento principal. A compilação e a revisão visual do PDF ainda precisam ser realizadas: este ambiente não dispõe de compilador LaTeX.

O guia de escrita dos artigos está em `templates/guia-trabalhos-relacionados.md`. A organização segue o exemplo de Natanael: capítulo 2 para Revisão Bibliográfica e capítulo 3 para Trabalhos Relacionados. O LaTeX de referência em `templates/natanael/` é uma reconstrução editável do PDF usando cópia da classe UFFS, identificada como transcrição; não é o fonte original.
