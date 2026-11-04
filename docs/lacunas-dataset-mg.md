# Lacunas do dataset de Minas Gerais

Levantamento da IA em 4 de novembro de 2026, comparando `datasets/Datasets_MG_Proj_Samuel` com a proposta registrada em `docs/decisoes-projeto.md` e nos objetivos de `tcc/markdown/01-introducao.md`. Complementa `docs/analise-dataset-mg.md`. São constatações e sugestões, não decisões do autor.

## Dados espectrais de satélite sem análise de imagem

A proposta não depende de análise visual de imagens (por exemplo, com CNN). Cada ponto amostrado vira uma linha de tabela, com a reflectância de cada banda como coluna e um rótulo como alvo; o TabPFN trabalha sobre essa tabela.

A reflectância, porém, não é metadado: os metadados descrevem a banda (por exemplo, B4 centrada em cerca de 665 nm, com 10 m de resolução), enquanto a medição é a fração da luz daquela faixa que voltou de cada ponto do terreno. Esses valores estão nos pixels das imagens de satélite. Por isso, as imagens precisam ser obtidas, mas apenas para amostrar os valores dos pixels nas coordenadas rotuladas.

| ponto (lat, lon) | B2 | B3 | B4 | … | B12 | rótulo (mapa geológico) |
| --- | --- | --- | --- | --- | --- | --- |
| −19,95; −43,90 | 0,08 | 0,11 | 0,14 | … | 0,21 | Xisto (Nova Lima) |

Valores ilustrativos. O raster SRTM da pasta pode ser tabelado do mesmo modo, como uma coluna de elevação.

## Ausentes e impeditivos

| Lacuna | Para quê | Situação |
| --- | --- | --- |
| 1. Reflectância Sentinel-2 (L2A, bandas B2–B12) das áreas de MG | Atributos de entrada do TabPFN (D01, D04, D05) | Dado público, obtido pelo autor no Copernicus Data Space ou no Google Earth Engine; não depende do coorientador |
| 2. Análises químicas laboratoriais georreferenciadas | Alvo da predição da composição química (D01, D09). A pasta só tem processos minerários com uma substância cadastrada (`SUBS`), sem teor | Principal lacuna. Requer tabela de amostras com coordenadas, data, material/profundidade, método analítico e teores de elementos ou óxidos. Candidata encontrada: tabela de solo da Base de Dados Geoquímica do SGB (`docs/fonte-sgb-geoquimica.md`) |
| 3. Dados compatíveis de outras regiões | Hipótese de generalização (D06) e avaliação em região externa (D07); a pasta cobre apenas MG | Depende dos datasets reunidos pelo autor (D02), com alvos compatíveis com os de MG |

O alvo do trabalho é a composição química (teores de elementos ou óxidos), conforme esclarecido pelo autor em 4 de novembro de 2026. Esses teores não equivalem a proporções de minerais e não devem ser descritos assim.

## Ausentes que enfraquecem a validação

| Lacuna | Motivo |
| --- | --- |
| 4. Observações litológicas independentes (afloramentos, pontos de campo) | Com rótulos apenas do mapa (`geologia_MG.shp`), a avaliação mede concordância com o mapa, não acerto geológico, ressalva também feita sobre Costa et al. (2019). Pontos de afloramento do SGB (GeoSGB) poderiam suprir essa lacuna |
| 5. Metadados da camada geológica: fonte, escala, edição e legenda | As 193 unidades não equivalem a 193 litologias; sem a legenda, não há base para agrupá-las em classes com significado geológico |

## Informações a confirmar com o coorientador

- 1. Licença de uso e redistribuição de cada camada, necessária para a publicação no Kaggle (D08).
- 1. Valor de ausência do raster SRTM: há 67.749.052 células com zero, sem valor de ausência declarado. Só é necessário se a elevação for usada como atributo.

## O que o dataset já fornece

- Rótulos litológicos cartográficos: `geologia_MG.shp`, com campos de litotipos.
- Seleção de áreas: processos minerários, drenagem, estruturas e limite estadual.
- Máscaras de nuvem e vegetação não exigem dado extra: podem ser derivadas do próprio Sentinel-2 (banda SCL e NDVI).
- Bibliotecas espectrais de laboratório: apoio para comparar assinaturas, sem substituir as lacunas 1 e 2.

## Síntese

Com esta pasta e o Sentinel-2 obtido pelo autor, a classificação litológica é viável, avaliada como concordância com o mapa. A predição da composição química depende da lacuna 2. Pedidos prioritários ao coorientador: lacunas 2, 4 e 5 e as confirmações 6 e 7.
