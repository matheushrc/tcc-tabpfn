# Fontes para consulta

Esta pasta reúne os sete estudos selecionados em `docs/artigos.md`. Os sete possuem `artigo.md`: seis foram extraídos do HTML original com o MCP do Playwright em 6 ou 9 de outubro de 2026 ou, no caso de Yang et al., em 4 de novembro de 2026; Costa et al. foram convertidos do PDF local com o MCP do PDFCraft em 2 de novembro de 2026. A data de extração não é a data de publicação. O PDF de Costa et al. foi preservado; os demais PDFs redundantes foram removidos conforme a preferência do autor pelo HTML.

| Pasta em `artigos/` | Fonte original | Formato |
| --- | --- | --- |
| `01-mapeamento-litologico-carajas/` | [Predictive lithological mapping through machine learning methods: a case study in the Cinzento Lineament, Carajás Province, Brazil](https://jgsb.sgb.gov.br/index.php/journal/article/view/63) | Markdown extraído do PDF via MCP PDFCraft; seis figuras, seis tabelas e 33 referências; PDF editorial de 11 páginas preservado |
| `02-tabpfn-sentinel2-classificacao-culturas/` | [Mapping of Crop Planting Structures Under Limited Training Samples Using TabPFN and Sentinel-2 Time Series Data](https://www.mdpi.com/2072-4292/18/11/1857) | Markdown; oito figuras, 15 tabelas e fórmulas em LaTeX; material suplementar (Table S1) em `assets/`; PDF editorial em `artigo.pdf`, baixado pelo autor para leitura |
| `03-hiperespectral-predicao-geoquimica/` | [Potential of hyperspectral-based geochemical predictions with neural networks for strategic and regional exploration improvement](https://doi.org/10.1080/08120099.2022.2094465) | Markdown; cinco tabelas completas e três figuras; CSVs em `assets/` |
| `04-geoquimica-rejeitos-witwatersrand/` | [Deriving big geochemical data from high-resolution remote sensing data via machine learning: Application to a tailing storage facility in the Witwatersrand goldfields](https://www.sciencedirect.com/science/article/pii/S2666544123000059) | Markdown; fórmulas em LaTeX |
| `05-tabpfn-sentinel2-carbono-solo/` | [Integrating transformer-based learning and Sentinel-2 bare soil composites for soil organic carbon mapping in the black soil region of Northeast China](https://www.nature.com/articles/s41598-025-33682-4) | Markdown; tabela incorporada da página editorial de tamanho completo |
| `06-tabpfn-espectroscopia-solo/` | [From field-scale to large-scale spectral libraries: Tabular foundation models in soil spectroscopy](https://arxiv.org/html/2608.00608v1) | Markdown, versão v1; fórmulas em LaTeX |
| `07-tabpfn-mir-validacao-externa/` | [Zero-shot inference with Tabular Prior-data Fitted Network (TabPFN) for soil MIR spectral analysis](https://www.sciencedirect.com/science/article/pii/S0016706126002089) | Markdown; seis figuras, três tabelas e fórmulas em LaTeX |

Os títulos ficam no front matter; o corpo preserva autores, texto, citações, figuras, tabelas e referências. Os links usam URLs completas. As figuras de cada artigo ficam na pasta `assets/` do próprio artigo, nomeadas `figura-<número>.<extensão>` (por exemplo, `figura-1.jpg` e `figura-a1.svg` para figuras de apêndice); no Markdown, cada imagem usa o caminho relativo `assets/` e aponta para a URL original da imagem, na maior resolução disponível. As chamadas de figura no texto, como `[Fig. 1](assets/figura-1.jpg)`, também apontam para esses arquivos locais. As seis imagens de Costa et al. foram extraídas do PDF e apontam para as páginas correspondentes no RIGeo. As tabelas usam Markdown, com repetição das células mescladas nas linhas ou colunas correspondentes e combinação dos níveis de cabeçalho. Os arquivos Markdown dos artigos não usam tags HTML; índices e expoentes usam matemática LaTeX, e as citações mantêm links em Markdown. As fórmulas usam LaTeX, sem MathML dentro dos delimitadores matemáticos. Autores, siglas, listas e referências têm formatação contínua, e controles de navegação foram removidos. Confira os elementos na fonte original antes de transcrever dados para o TCC.

Em Kutzke, os botões de tabelas e figuras foram abertos pelo Playwright. Os cinco CSVs são exportações das tabelas publicadas, e não uma cópia dos registros brutos de espectroscopia e geoquímica. A procedência dos arquivos está documentada em `03-hiperespectral-predicao-geoquimica/assets/README.md`. Os textos de análise já redigidos foram preservados. Cada pasta possui um arquivo `fundamentacao-teorica.md` com roteiro de leitura identificado como sugestão da IA, para apoiar a escrita pelo autor.

Os artigos usam prefixos numéricos e nomes curtos relacionados ao assunto. As notícias estão em `fontes/noticias/`; documentos institucionais e legislação podem ser guardados em `fontes/documentos-institucionais/` e `fontes/legislacao/` quando forem adicionados.

## Artigos removidos da seleção

Em 4 de novembro de 2026, o autor removeu Peña-Asensio et al. (2024) e Luo et al. (2025) da seleção e incluiu Yang et al. (2026); os motivos estão em `docs/artigos.md`. As conversões foram preservadas, sem numeração, em `artigos-descartados/tabpfn-minerais-meteoritos/` e `artigos-descartados/tabpfn-litologia-reservatorios/`, e não integram o capítulo 3.

## Ordem de preparação das análises

A ordem foi definida em 4 de novembro de 2026 pelo autor, a partir de proposta da IA, para acompanhar o título e o problema de pesquisa: classificação litológica, composição química e, por fim, harmonização e generalização entre regiões. Em cada bloco, os estudos vão do mais distante ao mais próximo da proposta do TCC. A pasta `NN` corresponde à subseção `3.N` de `tcc/markdown/03-trabalhos-relacionados.md`; as subseções ainda não redigidas ficam como lacunas na numeração do Markdown até sua incorporação, e o LaTeX numera automaticamente as seções presentes. Os arquivos `fundamentacao-teorica.md` das análises já redigidas preservam esses textos; apesar do nome, pertencem a Trabalhos Relacionados. A fundamentação conceitual de `tcc/markdown/02-revisao-bibliografica.md` continua pendente. A ordem não representa compromisso de implementar os métodos dos artigos.

| Ordem | Estudo | Bloco | Situação da análise | Motivo da posição e limites a preservar |
| --- | --- | --- | --- | --- |
| 01 | Costa et al. | Classificação litológica | Texto da seção 3.1 finalizado e incorporado | Precedente brasileiro de mapeamento litológico com Random Forest; introduz a discussão sobre coordenadas e concordância com mapas de referência. |
| 02 | Yang et al. | Classificação litológica | Texto da seção 3.2 redigido pela IA, finalizado pelo autor e incorporado | TabPFN com atributos Sentinel-2 por pixel, comparado com RF, XGBoost e CatBoost, com poucas amostras, zonas de exclusão espacial e ablação das coordenadas, retomando a questão de Costa; as classes são culturas agrícolas e não há teste em outra região. |
| 03 | Kutzke et al. | Composição química | Texto da seção 3.3 redigido pela IA, finalizado pelo autor e incorporado | Múltiplos alvos geoquímicos a partir de espectros de testemunhos; a transferência entre crátons é comparada com outro modelo, não com análises independentes. |
| 04 | Zhang et al. | Composição química | Texto da seção 3.4 finalizado e incorporado | Passagem para dados de satélite com alvo geoquímico; o modelo geoestatístico não fornece novas observações laboratoriais independentes. |
| 05 | Chen et al. | Composição química | Texto da seção 3.5 redigido pela IA, finalizado pelo autor e incorporado | TabPFN com Sentinel-2 e controle de solo exposto, o mais próximo do sensor proposto; o alvo é carbono orgânico. |
| 06 | Barkov et al. | Harmonização e generalização | Texto da seção 3.6 finalizado e incorporado | TabPFN em bibliotecas espectrais de diferentes escalas e instrumentos; limites das partições aleatórias. |
| 07 | Huang et al. | Harmonização e generalização | Texto da seção 3.7 redigido pela IA, finalizado pelo autor e incorporado | Teste em região externa com espectros MIR, fechando o capítulo na questão da generalização; não demonstra transferência orbital para os alvos deste TCC. |

## Autoria das análises

As análises de Costa et al. (3.1), Zhang et al. (3.4) e Barkov et al. (3.6) foram escritas manualmente pelo autor, com revisão pontual da IA, e já estão incorporadas ao capítulo 3. As de Yang et al. (3.2), Kutzke et al. (3.3), Chen et al. (3.5) e Huang et al. (3.7) foram redigidas integralmente pela IA, a pedido do autor, em 4 de novembro de 2026, a partir do `artigo.md` de cada pasta e seguindo o padrão das três seções manuais. No mesmo dia, a IA conferiu números, autoria e data de cada proposta na página original, com o MCP do Playwright: todos os valores conferiram; o ano de Huang et al. (Geoderma, jul. 2026) e de Chen et al. (Scientific Reports, v. 16, publicado em 5 jan. 2026) foi confirmado, e a divergência entre estanho, citado no texto de Kutzke et al., e zinco, presente nas tabelas, é do próprio artigo. Em 4 de novembro de 2026, o autor finalizou as quatro propostas, que foram incorporadas a `tcc/markdown/` e a `tcc/latex/` conforme E08 e P06 de `ABNT.md`. Os registros de terminologia e a divergência de fonte em Kutzke et al. foram preservados em `docs/terminologia.md`.

| Pasta | Estudo | Autoria do texto |
| --- | --- | --- |
| 01 | Costa et al. | Autor |
| 02 | Yang et al. | IA (integral), finalizado pelo autor |
| 03 | Kutzke et al. | IA (integral), finalizado pelo autor |
| 04 | Zhang et al. | Autor |
| 05 | Chen et al. | IA (integral), finalizado pelo autor |
| 06 | Barkov et al. | Autor |
| 07 | Huang et al. | IA (integral), finalizado pelo autor |

Os títulos e as URLs originais dos sete estudos estão na tabela acima. Essa sequência organiza a leitura e a redação pelo autor, mantendo a separação entre conceitos no capítulo 2 e comparação de estudos no capítulo 3. Os textos só entram nos capítulos após a finalização pelo autor. As referências usadas apenas neles não entram em `tcc/latex/bibliografia.bib` enquanto não forem efetivamente citadas no TCC.
