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
- **Elevação:** SRTM de 3" (cerca de 90 m), versão 4.1 com falhas preenchidas, em 63 blocos de 5° × 5°. Fonte: CGIAR-CSI, <https://srtm.csi.cgiar.org/srtmdata/>. É atributo opcional da ablação (D22).

Os shapefiles da ANM e do IBGE estão em SIRGAS 2000 (EPSG:4674); as camadas do SGB e o SRTM, em WGS 84 (EPSG:4326). Integrá-los exige um sistema métrico comum para distâncias, áreas e margens de exclusão.

Material auxiliar:
- **Bibliotecas espectrais de laboratório:** 27 bibliotecas ENVI, com 1.783 espectros (USGS, JPL, JHU, IGCP e vegetação), recebidas do coorientador sem metadados de origem.
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

- **USGS (`usgs_min.hdr`):** 481 espectros de laboratório da biblioteca de 1993, em 420 comprimentos de onda de cerca de 0,395 a 2,56 µm.
- **JPL:** 430 espectros em três granulometrias.
- **IGCP:** 139 espectros em cinco instrumentos, de 30 amostras distintas.
- **JHU de minerais:** começa em cerca de 2,079 µm, então não reconstrói as bandas visíveis do Sentinel-2.

Nenhuma dessas contagens é de localidades brasileiras.

As bibliotecas servem para:
- comparar assinaturas;
- simular as bandas do sensor com as [funções de resposta espectral do Sentinel-2](https://sentinels.copernicus.eu/-/sentinel-2-spectral-response-functions-update).

Um modelo treinado com espectros de laboratório reamostrados não equivale a um treinado com observações de satélite. Medições do mesmo espécime em instrumentos ou granulometrias diferentes devem ficar no mesmo grupo na avaliação.

## Lacunas

| Lacuna | Situação |
| --- | --- |
| Reflectância Sentinel-2 (L2A, B2–B12) | Não obtida. Dado público (Copernicus Data Space ou Google Earth Engine). |
| Lineamentos geofísicos | Sem camada nacional equivalente. A aerogeofísica do SGB está em <https://geoportal.sgb.gov.br/server/rest/services/geofisica/aerogeofisica/MapServer>, em rasters por projeto. |
| Validação de lítio e terras raras | Como substância principal, as ocorrências do SGB têm só 34 de lítio e 14 de terras raras. |
| Metadados e licença das bibliotecas espectrais do coorientador | A confirmar com ele, inclusive para publicar derivados no Kaggle (D08). |

## Qualidade

- Os binários espectrais têm tamanhos compatíveis com os cabeçalhos e nenhum valor não finito.
- Antes de normalizar, conferir:
  - valores negativos em bibliotecas de solo e vegetação;
  - valores acima de um na IGCP e na USGS;
  - comprimentos de onda fora de ordem na biblioteca de neve.
- As contagens das camadas nacionais conferem com o total informado por cada serviço.
- Não houve extração de imagens, ajuste de modelos nem validação preditiva.
