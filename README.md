# tcc-tabpfn

## Escrita do TCC

O texto principal da introdução está em `tcc/markdown/01-introducao.md`. Faça as revisões de conteúdo no Markdown e solicite à IA a atualização de `tcc/latex/capitulos/01-introducao.tex` quando necessário, seguindo o template da faculdade.

Os dados básicos do trabalho ficam em `tcc.conf`, no formato `chave=valor`. O projeto LaTeX está em `tcc/latex/`, com `principal.tex` como documento principal e `bibliografia.bib` para referências. `Template_UFFSTex/` preserva o modelo original.

Para revisar no Overleaf, envie os arquivos de `tcc/latex/`, preservando as subpastas, e selecione `principal.tex` como documento principal. A tentativa de compilação local ficou bloqueada no carregamento do Babel/MiKTeX; o PDF ainda não foi validado. Título em inglês, palavras-chave, resumo e abstract permanecem pendentes para o fim do TCC I; a versão atual contém introdução e trabalhos relacionados; a revisão conceitual está pendente.

Consulte `ARCHITECTURE.md` para a organização das áreas, `AGENTS.md` para as regras de trabalho e `ORGANIZACAO_TCC.md` para o plano e as verificações da reorganização. `templates/natanael/` contém o documento integral de referência e uma reconstrução LaTeX editável a partir do PDF; `templates/guia-trabalhos-relacionados.md` contém o guia de escrita.

## Escopo vigente

O trabalho pretende avaliar o TabPFN para classificação litológica e predição da composição mineral a partir de dados espectrais de satélite, associados a referências geológicas e laboratoriais compatíveis. A viabilidade dos alvos e o protocolo experimental ainda dependem das verificações registradas em `docs/decisoes-projeto.md` (D01–D07).

As decisões e pendências ficam nesse registro; `tcc.conf` define os dados básicos e `ABNT.md` reúne as regras editoriais. Notas de pesquisa, artigos e exemplos não substituem essas definições. As ideias do autor para explorar em 2027 estão preservadas em `docs/historico-planejamento.md`. Permanecem possibilidades em aberto, sem constituir compromissos do escopo atual.
