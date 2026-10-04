# Frente África, Ásia e global — fontes para o datalake

Pesquisa e aquisição concluídas em 2026-08-21, priorizando serviços e repositórios primários. Não foi necessário Playwright: GSJ, CGS, GRO.data/GEOROC e USGS expuseram downloads ou APIs diretas, e o volume encontrado foi suficiente.

## Resumo do que foi baixado

| Região | Dataset | Volume local | Cobertura | Papel para ML |
| --- | --- | ---: | --- | --- |
| África do Sul | CGS geochemistry 1:250k | 79.835.213 bytes; 145.224 pontos | 9 folhas | **Alvo direto**: óxidos/elementos em coordenadas |
| África | GEOROC Archaean Cratons | ~4,5 MB; 5.027 amostras | 6 unidades geológicas | **Alvo direto condicionado**: geoquímica de rocha publicada |
| Japão | GSJ Geochemical Map | 1.533.253 bytes; 3.025 amostras | nacional, sedimentos fluviais | **Alvo direto**: 53 analitos em coordenadas |
| Índia/China | GEOROC Archaean Cratons | ~6,0 MB; 6.517 amostras | 6 unidades geológicas | **Alvo direto condicionado** |
| Global | USGS MRDS | ZIP 25,8 MB / CSV 137,2 MB; 304.632 registros | 166 países, desigual | **Auxiliar**: ocorrências, commodities e contexto; não teores consistentes |

Todos os arquivos têm SHA-256 em `SHA256SUMS`; cada pasta contém fonte, licença, schema, uso e limitações. O CGS inclui o JSON oficial da camada e um dicionário operacional; GEOROC inclui a metadata oficial da versão e schema inferido; GSJ inclui schema inferido; MRDS inclui o `mrds.met` oficial. Os schemas inferidos registram explicitamente método/proveniência, unidades, missing/censura, CRS e chaves. Nenhum arquivo individual baixado excede 500 MB.

## Compatibilidade com o SACM

O SACM contém rochas mineralizadas/de depósitos, coordenadas WGS84 e melhores valores químicos em ppm ou porcentagem. A compatibilidade não é binária:

1. **CGS África do Sul** é tabular e multielementar como o SACM, mas usa principalmente sedimento de drenagem/solo e um painel menor de XRF. Harmonize unidades e use a interseção de analitos (`Fe`, `Ti`, `Mn`, `Sc`, `V`, `Cr`, `Co`, `Ni`, `Cu`, `Zn`, `As`, `Rb`, `Sr`, `Y`, `Zr`, `Nb`, `Mo`, `Sn`, `Sb`, `Ba`, `W`, `Pb`, `Th`, `U`). Não converta óxidos em elementos sem registrar a fórmula e massa molar.
2. **GSJ Japão** também é geoquímica de superfície, com painel amplo e coordenadas, mas o suporte espacial é a bacia de drenagem. É excelente teste de mudança de país, sensor e meio amostral.
3. **GEOROC** se aproxima mais de análises de rocha, porém mistura rochas não mineralizadas, métodos e publicações. Use `MATERIAL`, `ROCK TYPE`, alteração e precisão de coordenadas como filtros/domínios; agrupe pelo artigo para impedir vazamento.
4. **MRDS** não fornece vetores de teor compatíveis. Ele deve validar se anomalias caem perto de ocorrências conhecidas e fornecer rótulos auxiliares, nunca substituir a matriz química.

Schema canônico sugerido: `sample_id`, `source`, `country_iso3`, `region_id`, `latitude`, `longitude`, `crs_original`, `sample_medium`, `material`, `collection_year`, `method`, `analyte`, `value`, `unit`, `qualifier`, `citation_id`, `coordinate_precision`. Mantenha uma tabela longa de determinações e derive a tabela larga apenas após definir o painel comum.

## Estratégia de validação para regiões nunca vistas

### Leave-country-out

- Normalize e ajuste imputação **somente no treino**.
- Treine em SACM + países disponíveis e retenha Japão, África do Sul, Índia ou China por inteiro.
- No GEOROC, obtenha país por *spatial join* com fronteiras versionadas; o nome do cráton não basta.
- Exclua amostras próximas à fronteira do conjunto retido com um buffer compatível com a resolução das imagens para reduzir vazamento espacial.

### Leave-continent-out

- Experimento principal: treino América do Norte/SACM + Ásia, teste África; depois rotacione África/Ásia/Américas.
- Como o meio amostral confunde continente, reporte duas análises: (a) tudo disponível, refletindo uso real; (b) apenas meios comparáveis, como rocha total GEOROC versus rocha SACM.
- Ajuste bandas e índices por sensor/época dentro de um pipeline congelado. Não permita que mosaicos da região de teste influenciem seleção de features ou hiperparâmetros.

### Folds espaciais internos

- África do Sul: retenha `MapNo` inteiro (leave-sheet-out) ou blocos espaciais maiores que a autocorrelação estimada.
- Japão: agrupe por bacia/folha, evitando amostras vizinhas em treino e teste.
- GEOROC: agrupe primeiro por `CITATIONS` e depois por blocos espaciais; análises do mesmo estudo ou local nunca devem atravessar folds.
- MRDS: deduplique antes da avaliação por distância, nome e identificadores.

Métricas: MAE/RMSE por analito em espaço logarítmico quando justificável, erro composicional (Aitchison) para vetores fechados, cobertura de intervalos de incerteza e desempenho por país/meio. Sempre compare contra baseline de mediana do país de treino e contra um modelo que usa apenas covariáveis ambientais.

## Riscos de interpretação

- Mudança de domínio inclui geologia, clima, sensor, campanha, laboratório e meio amostral; “país nunca visto” não isola apenas geografia.
- Geoquímica publicada tem censura, limites de detecção e valores ausentes não aleatórios. Preserve qualificadores quando existirem.
- Dados de ocorrência são positivos incompletos; áreas sem registros não são negativos confiáveis.
- Resultados de prospecção devem ser apresentados como priorização/hipótese, não prova de depósito ou estimativa de reserva.

## Fontes primárias consultadas

- GSJ Geochemical Map: <https://gbank.gsj.jp/geochemmap/data/data.htm>
- GSJ terms: <https://www.gsj.jp/en/license/index.html>
- CGS layer: <https://maps.geoscience.org.za/hosting/rest/services/RSA_GEOCHEMISTR_MIL1/MapServer/2>
- CGS item/license: <https://maps.geoscience.org.za/hosting/rest/services/RSA_GEOCHEMISTR_MIL1/MapServer/2/iteminfo>
- GEOROC dataset DOI: <https://doi.org/10.25625/1KRR1P>
- GEOROC citation/license guidance: <https://georoc.mpch-mainz.gwdg.de/georoc/cite.asp>
- MRDS fields: <https://mrdata.usgs.gov/mrds/about.php>
- MRDS service: <https://energy.usgs.gov/arcgis/rest/services/Hosted/Mineral_Resource_Data_System/FeatureServer/0>
- USGS copyright/public-domain policy: <https://www.usgs.gov/information-policies-and-instructions/copyrights-and-credits>
