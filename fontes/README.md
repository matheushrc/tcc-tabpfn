# Fontes para consulta

Esta pasta reúne os documentos da revisão bibliográfica e os sete estudos selecionados. Os sete possuem `artigo.md`, todos extraídos do HTML original com o MCP do Playwright em 6 ou 9 de outubro de 2026 ou, no caso de Yang et al., em 4 de novembro de 2026 e, no de Franca-Rocha et al., em 22 de novembro de 2026. A data de extração não é a data de publicação. Os PDFs redundantes foram removidos conforme a preferência do autor pelo HTML.

| Pasta em `artigos/` | Fonte original | Formato |
| --- | --- | --- |
| `01-sentinel2-prospectividade-ferro-bahia/` | [Identifying High-Potential Zones for Iron Mineralization in Bahia, Brazil, Using a Spectral Angle Mapper–Random Forest Integrated Framework](https://www.mdpi.com/2075-163X/15/11/1119) | Markdown; 13 figuras e quatro tabelas em `assets/` |
| `02-tabpfn-sentinel2-classificacao-culturas/` | [Mapping of Crop Planting Structures Under Limited Training Samples Using TabPFN and Sentinel-2 Time Series Data](https://www.mdpi.com/2072-4292/18/11/1857) | Markdown; oito figuras, 15 tabelas e fórmulas em LaTeX; material suplementar (Table S1) em `assets/`; PDF editorial em `artigo.pdf`, baixado pelo autor para leitura |
| `03-hiperespectral-predicao-geoquimica/` | [Potential of hyperspectral-based geochemical predictions with neural networks for strategic and regional exploration improvement](https://doi.org/10.1080/08120099.2022.2094465) | Markdown; cinco tabelas completas e três figuras; CSVs em `assets/` |
| `04-geoquimica-rejeitos-witwatersrand/` | [Deriving big geochemical data from high-resolution remote sensing data via machine learning: Application to a tailing storage facility in the Witwatersrand goldfields](https://www.sciencedirect.com/science/article/pii/S2666544123000059) | Markdown; fórmulas em LaTeX |
| `05-tabpfn-sentinel2-carbono-solo/` | [Integrating transformer-based learning and Sentinel-2 bare soil composites for soil organic carbon mapping in the black soil region of Northeast China](https://www.nature.com/articles/s41598-025-33682-4) | Markdown; tabela incorporada da página editorial de tamanho completo |
| `06-tabpfn-espectroscopia-solo/` | [From field-scale to large-scale spectral libraries: Tabular foundation models in soil spectroscopy](https://arxiv.org/html/2608.00608v1) | Markdown, versão v1; fórmulas em LaTeX |
| `07-tabpfn-mir-validacao-externa/` | [Zero-shot inference with Tabular Prior-data Fitted Network (TabPFN) for soil MIR spectral analysis](https://www.sciencedirect.com/science/article/pii/S0016706126002089) | Markdown; seis figuras, três tabelas e fórmulas em LaTeX |

Os títulos ficam no front matter; o corpo preserva autores, texto, citações, figuras, tabelas e referências. Os links usam URLs completas. As figuras de cada artigo ficam na pasta `assets/` do próprio artigo, nomeadas `figura-<número>.<extensão>` (por exemplo, `figura-1.jpg` e `figura-a1.svg` para figuras de apêndice); no Markdown, cada imagem usa o caminho relativo `assets/` e aponta para a URL original da imagem, na maior resolução disponível. As chamadas de figura no texto, como `[Fig. 1](assets/figura-1.jpg)`, também apontam para esses arquivos locais. As tabelas usam Markdown, com repetição das células mescladas nas linhas ou colunas correspondentes e combinação dos níveis de cabeçalho. Os arquivos Markdown dos artigos não usam tags HTML; índices e expoentes usam matemática LaTeX, e as citações mantêm links em Markdown. As fórmulas usam LaTeX, sem MathML dentro dos delimitadores matemáticos. Autores, siglas, listas e referências têm formatação contínua, e controles de navegação foram removidos. Confira os elementos na fonte original antes de transcrever dados para o TCC.

Em Kutzke, os botões de tabelas e figuras foram abertos pelo Playwright. Os cinco CSVs são exportações das tabelas publicadas, e não uma cópia dos registros brutos de espectroscopia e geoquímica. A procedência dos arquivos está documentada em `03-hiperespectral-predicao-geoquimica/assets/README.md`. Os textos de análise já redigidos foram preservados. Cada pasta possui um arquivo `trabalhos-relacionados.md` com roteiro de leitura identificado como sugestão da IA, para apoiar a escrita pelo autor.

Os artigos usam prefixos numéricos e nomes curtos relacionados ao assunto. As notícias estão em `fontes/noticias/`; documentos institucionais e legislação podem ser guardados em `fontes/documentos-institucionais/` e `fontes/legislacao/` quando forem adicionados.

## Revisão bibliográfica

A pasta `fontes/revisao-bibliografica/` guarda, fora do git, as cópias locais das fontes do capítulo 2: o índice em `README.md`, o inventário técnico em `manifesto.json`, os PDFs em `pdfs/` e as páginas web em `paginas/`. Só `manifesto-links-originais.json` pode ser versionado. A proposta do capítulo, já incorporada a `tcc/markdown/02-revisao-bibliografica.md`, foi arquivada em `docs/arquivo/proposta-revisao-bibliografica.md`.

As 41 fontes da proposta foram arquivadas em 5 de novembro de 2026: 63 PDFs e 7 HTMLs. O relatório de Taggart é distribuído em partes, preservadas em `pdfs/taggart2002/`; Clark possui o HTML do autor e uma reprodução desse conteúdo em PDF. Edições, manuscritos, origem dos downloads e limites das cópias estão descritos no índice da pasta.

## Artigos removidos da seleção

As conversões dos estudos removidos ficam, sem numeração, em `artigos-descartados/` e não integram o capítulo 3. Os motivos de cada remoção estão em `docs/artigos.md`.

## Ordem de preparação das análises

Os motivos da posição e os limites de cada estudo estão em `docs/artigos.md`. A ordem foi definida em 4 de novembro de 2026 pelo autor, a partir de proposta da IA, para acompanhar o título e o problema de pesquisa: previsão de ocorrências (classificação), composição química e, por fim, harmonização e generalização entre regiões. Em cada bloco, os estudos vão do mais distante ao mais próximo da proposta do TCC. A pasta `NN` corresponde à subseção `3.N` de `tcc/markdown/03-trabalhos-relacionados.md`; as subseções ainda não redigidas ficam como lacunas na numeração do Markdown até sua incorporação, e o LaTeX numera automaticamente as seções presentes. Os arquivos `trabalhos-relacionados.md` das análises já redigidas preservam esses textos; apesar do nome, pertencem a Trabalhos Relacionados. A ordem não representa compromisso de implementar os métodos dos artigos.

| Ordem | Estudo | Bloco | Situação da análise |
| --- | --- | --- | --- |
| 01 | Franca-Rocha et al. | Classificação | Texto da seção 3.1 redigido pela IA, finalizado pelo autor e incorporado |
| 02 | Yang et al. | Classificação | Texto da seção 3.2 redigido pela IA, finalizado pelo autor e incorporado |
| 03 | Kutzke et al. | Composição química | Texto da seção 3.3 redigido pela IA, finalizado pelo autor e incorporado |
| 04 | Zhang et al. | Composição química | Texto da seção 3.4 finalizado e incorporado |
| 05 | Chen et al. | Composição química | Texto da seção 3.5 redigido pela IA, finalizado pelo autor e incorporado |
| 06 | Barkov et al. | Harmonização e generalização | Texto da seção 3.6 finalizado e incorporado |
| 07 | Huang et al. | Harmonização e generalização | Texto da seção 3.7 redigido pela IA, finalizado pelo autor e incorporado |

## Autoria das análises

As análises de Zhang et al. e Barkov et al. foram escritas pelo autor; as demais foram redigidas pela IA a pedido do autor e finalizadas por ele (E08 e P06 de `ABNT.md`). Registros de terminologia em `docs/terminologia.md`.

| Pasta | Estudo | Autoria do texto |
| --- | --- | --- |
| 01 | Franca-Rocha et al. | IA (integral), finalizado pelo autor |
| 02 | Yang et al. | IA (integral), finalizado pelo autor |
| 03 | Kutzke et al. | IA (integral), finalizado pelo autor |
| 04 | Zhang et al. | Autor |
| 05 | Chen et al. | IA (integral), finalizado pelo autor |
| 06 | Barkov et al. | Autor |
| 07 | Huang et al. | IA (integral), finalizado pelo autor |

Os títulos e as URLs originais dos sete estudos estão na tabela acima. Essa sequência organiza a leitura e a redação pelo autor, mantendo a separação entre conceitos no capítulo 2 e comparação de estudos no capítulo 3. Os textos só entram nos capítulos após a finalização pelo autor. As referências usadas apenas neles não entram em `tcc/latex/bibliografia.bib` enquanto não forem efetivamente citadas no TCC.
