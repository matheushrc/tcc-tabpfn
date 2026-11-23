# Dataset do Brasil

Dono do inventário, dos rótulos e das lacunas dos dados usados no TCC. Os dados ficam em `datasets/brasil/`, fora do git; o `README.md` dessa pasta tem os arquivos, as fontes e as contagens, e o `SHA256SUMS.txt`, os hashes. O escopo (alvo, classes e validação) está em D24 de `docs/decisoes-projeto.md`.

## Conteúdo

Camadas nacionais:
- **Processos minerários ativos:** 270.994 polígonos, com `SUBS`, `FASE` e `UF`. Fonte: ANM, SIGMINE, <https://dadosabertos.anm.gov.br/SIGMINE/PROCESSOS_MINERARIOS/BRASIL.zip>, listado em <https://dados.gov.br/dados/conjuntos-dados/sistema-de-informacoes-geograficas-da-mineracao-sigmine>.
- **Ocorrências minerais:** 36.484 pontos e 42.631 relações ocorrência–substância. Fonte: SGB, <https://geoportal.sgb.gov.br/server/rest/services/geologia/ocorrencias/MapServer>.
- **Geoquímica de baixa densidade:** 3.756 amostras de solo e 14.373 de sedimento de corrente, com cerca de 50 elementos. Fonte: SGB, <https://geoportal.sgb.gov.br/server/rest/services/gestaoterritorial/geoquimica_baixa_densidade/MapServer>.
- **Geologia:**
  - 1:1.000.000 do Brasil, com 46.712 polígonos. Fonte: SGB, <https://geoportal.sgb.gov.br/server/rest/services/geologia/litoestratigrafia_1000000/MapServer>;
  - 24 mapas estaduais, sem BA, PB e DF. O de MG tem 8.893 polígonos e 399 unidades. Fonte: SGB, <https://geoportal.sgb.gov.br/server/rest/services/geologia/litoestratigrafia_estados/MapServer>.
- **Estruturas geológicas:** 32.323 linhas. Fonte: SGB, <https://geoportal.sgb.gov.br/server/rest/services/geologia/Estruturas_GIS_Brasil_2004/MapServer>.
- **Drenagem:** 210.382 trechos da Base Cartográfica Contínua ao Milionésimo (BCIM 2016). Fonte: IBGE, <https://geoftp.ibge.gov.br/cartas_e_mapas/bases_cartograficas_continuas/bcim/versao2016/shapefile/bcim_2016_shapefiles_21-11-2018.zip>.
- **Limites estaduais:** 27 unidades da federação, malha de 2024. Fonte: IBGE, <https://geoftp.ibge.gov.br/organizacao_do_territorio/malhas_territoriais/malhas_municipais/municipio_2024/Brasil/BR_UF_2024.zip>.
- **Elevação:** NASADEM de 1" (cerca de 30 m), em 819 blocos de 1° × 1° que tocam o território brasileiro, com `.hgt` (elevação), `.num` (origem de cada pixel) e `.swb` (máscara de água), cerca de 6,7 GB. Fonte: NASA, <https://www.earthdata.nasa.gov/data/catalog/lpcloud-nasadem-hgt-001> (DOI 10.5067/MEASURES/NASADEM/NASADEM_HGT.001); o download exige conta no NASA Earthdata. É atributo opcional da ablação (D22). Substitui o SRTM do CGIAR-CSI, cuja licença proíbe a redistribuição (D03, D08).

Os shapefiles da ANM e do IBGE estão em SIRGAS 2000 (EPSG:4674); as camadas do SGB e o NASADEM, em WGS 84 (EPSG:4326). Integrá-los exige um sistema métrico comum para distâncias, áreas e margens de exclusão.

Material auxiliar:
- **USGS Spectral Library 7, reamostrada para o Sentinel-2:** 3.152 arquivos em `Assinaturas_Espectrais/usgs_splib07/`, extraídos de `usgs_splib07.zip` ([Kokaly et al., 2017](https://doi.org/10.5066/F7RR1WDJ)). Apoio fora do modelo (D03).
- **Bibliotecas do coorientador:** 27 bibliotecas ENVI, com 1.783 espectros (USGS, JPL, JHU, IGCP e vegetação), copiadas do software ENVI. Não são usadas (D03); conferência na seção Bibliotecas espectrais.
- **MapBiomas SoilData:** dois estudos de solo com reflectância, sem coordenadas utilizáveis.

## O que os rótulos informam

- **`SUBS` dos processos.** Cada registro tem uma substância cadastrada, com 326 valores distintos; 10.522 processos têm "DADO NÃO CADASTRADO". As fases vão de requerimento a concessão, e um processo não é necessariamente uma mina em operação. A [ANM descreve o SIGMINE como um cadastro de áreas de processos minerários](https://www.gov.br/anm/pt-br/assuntos/exploracao-mineral/sistemas-de-exploracao-mineral). A substância cadastrada não demonstra predominância, teor nem reserva na área. `AREA_HA` é área, e `ANO` é do processo, não da coleta.
- **Ocorrências do SGB.** São observações de campo. Locais sem registro são não rotulados, e não ausências.
- **Geologia.** Os litotipos são listas qualitativas da unidade cartografada, não proporções nem a rocha de cada pixel. Comparar com o mapa mede concordância com a cartografia. Milhões de pixels com o mesmo rótulo não são milhões de amostras independentes.
- **Geoquímica.** Os teores medem solo e sedimento de corrente, não a superfície observada pelo satélite. O valor associado a um pixel vem do ponto mais próximo ou de interpolação.

## Dados espectrais de satélite em tabela

A proposta não depende de análise visual de imagens. Cada ponto amostrado vira uma linha de tabela, com a reflectância de cada banda como coluna e o rótulo como alvo. Os metadados descrevem a banda (por exemplo, B4 centrada em cerca de 665 nm, com 10 m de resolução); a medição é a fração da luz daquela faixa que voltou do terreno e está nos pixels das imagens.

| ponto (lat, lon) | B2 | B3 | B4 | … | B12 | rótulo (`SUBS`) |
| --- | --- | --- | --- | --- | --- | --- |
| −19,95; −43,90 | 0,08 | 0,11 | 0,14 | … | 0,21 | Ouro |

Valores ilustrativos. A elevação, a unidade geológica e os teores geoquímicos entram como colunas adicionais (D22).

## Bibliotecas espectrais

Em uso (D03): a USGS Spectral Library 7 já reamostrada pelo USGS para as 13 bandas do Sentinel-2 (`s07SNTL2`), com as funções de resposta espectral de cada banda. Serve para:
- escolher bandas e índices espectrais (seção 4.2);
- interpretar a ablação (D22);
- discutir os limites do sensor, comparando a curva de laboratório com a versão em 13 bandas.

As bibliotecas do coorientador não são usadas. São cópias das que acompanham o ENVI, e a IA as conferiu com as fontes oficiais em 22 de novembro de 2026:
- **USGS (`usgs_min`, `usgs_veg`, `igcp_4`):** iguais à versão 7 em 98% a 100% dos espectros pareados.
- **JPL e JHU:** iguais ao [ECOSTRESS](https://speclib.jpl.nasa.gov/), exceto 35% da JHU de minerais, que divergem por motivo não verificado.
- **Sem fonte conferida:** `veg_1dry`, `veg_2grn` e IGCP medidas fora do USGS.

Nenhuma biblioteca tem localidades brasileiras.

Um modelo treinado com espectros de laboratório reamostrados não equivale a um treinado com observações de satélite. Medições do mesmo espécime em instrumentos ou granulometrias diferentes devem ficar no mesmo grupo na avaliação.

## Lacunas

| Lacuna | Situação |
| --- | --- |
| Reflectância Sentinel-2 (L2A, B2–B12) | Não obtida. Dado público (Copernicus Data Space ou Google Earth Engine). |
| Lineamentos geofísicos | Sem camada nacional equivalente. A aerogeofísica do SGB está em <https://geoportal.sgb.gov.br/server/rest/services/geofisica/aerogeofisica/MapServer>, em rasters por projeto. |
| Validação de lítio e terras raras | Como substância principal, as ocorrências do SGB têm só 34 de lítio e 14 de terras raras. |

## Qualidade

- Os binários espectrais têm tamanhos compatíveis com os cabeçalhos e nenhum valor não finito.
- Antes de normalizar, conferir:
  - valores negativos em bibliotecas de solo e vegetação;
  - valores acima de um na IGCP e na USGS;
  - comprimentos de onda fora de ordem na biblioteca de neve.
- As contagens das camadas nacionais conferem com o total informado por cada serviço.
- Não houve extração de imagens, ajuste de modelos nem validação preditiva.
