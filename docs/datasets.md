# Datasets para o datalake geoquímico e mineral

Snapshot verificado em **21 de agosto de 2026**. Foram reunidos cerca de **541 MB** de novas distribuições em `datasets/`, organizadas por país ou região, além dos **656 MB** do SACM já existente. Há dados da América do Norte, América do Sul, Europa, África, Ásia e Oceania. Nenhum arquivo individual novo excede 500 MB.

O objetivo desta seleção não é apenas aumentar o número de linhas: é permitir testes em países, províncias, levantamentos e continentes que nunca participaram do ajuste do modelo. As coleções foram separadas pelo que realmente podem supervisionar.

## Inventário e prioridade

| Região | Dataset | Escala e volume | Papel correto | Metadado que decodifica os campos | Prontidão |
|---|---|---|---|---|---|
| Estados Unidos | **USGS SACM/NGDOD** | 29.781 amostras de rocha/minério; 1.437.757 determinações | Regressão multielementar e tipos de depósito | `SACM/SACM_DR_csv/DataDictionary.csv`, `Parameter.csv`, `AnalyticMethod.csv` e `SACM/SACM_MD.xml` | **Alta**; base principal já existente |
| Canadá | **CDoGS pacote 0434** | 13.654 análises, 17 levantamentos, 35 analitos | Regressão em sedimento regional | `pkg00434_metadata.html` + `schema_inferred.csv` | **Alta**, após censura/unidades |
| Canadá | **GSC Open File 2859, Yukon** | 623 locais, 36 elementos | Holdout territorial em sedimento/água | `NGR_DESC.ASC`, `PREFACE.DOS`, `README.TXT` | **Média**; confirmar datum UTM |
| Canadá | **SIGÉOM Québec** | 561.232 amostras, 124 colunas | Grande domínio externo de sedimento/solo/till | `Attributs_echantillons_sediment.xlsx`, `Echantillons_de_sediments.pdf`, `geochimie_documentation_officielle.html` | **Alta**, com estratificação por material/método |
| Brasil | **SGB ocorrências minerais** | 36.484 ocorrências e 42.631 relações com substâncias | Classificação positiva–não rotulada, distância e auditoria | `ocorrencias_schema_official.json` + `substancias_schema_official.json` | **Alta como ocorrência**; não contém teores |
| Brasil | **MapBiomas SoilData ZI0QIO** | 71 pontos/142 amostras descritos; solo e espectro | Protótipo de ferro–cor–espectro tropical | aba oficial `dicionário (admin)`, `metadata_dataverse.json` e `SCHEMA.md` | **Auxiliar**; coordenadas `#N/A` nesta cópia |
| Brasil | **MapBiomas SoilData LOOGRU** | 12 perfis em duas profundidades | Protótipo de solo, cor, ferro e reflectância | aba oficial `dicionário (admin)`, `metadata_dataverse.json` e `SCHEMA.md` | **Auxiliar**; coordenadas `#N/A` nesta cópia |
| Austrália | **NGSA** | 1.315 sítios; 7.893 registros; até 68 elementos | Regressão de fundo geoquímico por bacia | 11 linhas introdutórias do CSV + `schema_inferred.json` | **Alta**, agrupando por sítio/método/fração |
| Austrália | **OZMIN** | ZIP legado com 490 registros de carvão; 20 feições de amostra da API atual | Ocorrências/recursos, não química | `schema.json` oficial + `schema_inferred.json` | **Incompleto**; não alegar cobertura multicommodity |
| Europa | **GEMAS Ap** | 2.113 solos em 34 códigos de país; 52 elementos | Regressão e `leave-one-country-out` harmonizado | `layer_schema.json`, manual oficial PDF e `schema_inferred.json` | **Alta** |
| Reino Unido | **BGS G-BASE sample** | Duas planilhas de amostra | Teste do ETL e experimento pequeno | guia oficial PDF + `schema_inferred.json` | **Limitada**; base nacional pontual exige solicitação |
| África do Sul | **CGS 1:250k** | 145.224 pontos em 9 folhas | Regressão geoquímica; teste por folha | `layer_metadata_official.json` + `schema_inferred.csv` | **Alta** nas folhas cobertas |
| África | **GEOROC crátons** | 5.027 amostras em 6 unidades geológicas | Regressão condicionada de química de rocha | `dataset_metadata_official.json` + `schema_inferred.csv` | **Média/alta**, filtrando coordenada/material/citação |
| Índia e China | **GEOROC crátons** | 6.517 amostras em 6 unidades | Regressão condicionada de química de rocha | `dataset_metadata_official.json` + `schema_inferred.csv` | **Média/alta**; obter país por junção espacial |
| Japão | **GSJ Geochemical Map** | 3.025 sedimentos fluviais, 53 analitos | Regressão nacional e holdout Japão | `schema_inferred.csv` | **Alta**, respeitando CP932 e JGD2000 |
| Global | **USGS MRDS** | 304.632 ocorrências, 166 países | Ocorrência/commodity e auditoria global | `mrds.met` oficial | **Alta como ocorrência**; não contém matriz de teores |
| Estados Unidos | **MRDS Califórnia aprimorado** | 42.744 pontos, 328 modelos de depósito | Tipos, commodities, grupos e cobertura | XML oficial `MRDS_Features_in_CA_Enhanced_Deposit_Model_Data.xml` | **Alta como ocorrência**; `grade` textual não é teor padronizado |

Os schemas chamados `schema_inferred.*` são explicitamente não oficiais: foram criados porque a distribuição não trazia um dicionário tabular autônomo. Eles registram tipo numérico/categórico, unidade, chave, CRS, missing, censura e a proveniência da interpretação. Quando existe dicionário oficial, ele continua sendo a autoridade.

## Onde estão os dados

- [Brasil](datasets/brasil/README.md): SGB e MapBiomas SoilData.
- [Canadá](datasets/canada/README.md): CDoGS, Yukon e SIGÉOM Québec.
- [Estados Unidos](datasets/estados_unidos/README.md): inventário do SACM e MRDS Califórnia.
- [Austrália](datasets/australia/README.md): NGSA e OZMIN.
- [Europa](datasets/europa/README.md): GEMAS continental.
- [Reino Unido](datasets/reino_unido/README.md): amostras G-BASE.
- [África do Sul](datasets/africa/africa_do_sul/cgs_geochemistry_250k/README.md) e [GEOROC África](datasets/africa/georoc_cratons/README.md).
- [GEOROC Ásia](datasets/asia/georoc_cratons/README.md) e [GSJ Japão](datasets/asia/japao/gsj_geochemical_map/README.md).
- [MRDS global](datasets/global/usgs_mrds/README.md).
- [SACM existente](SACM/README.md).

Pastas continentais/globais são exceções intencionais à organização por país: GEMAS, GEOROC e MRDS atravessam fronteiras. No ETL, grave `country_iso3` por atributo oficial ou por *spatial join* com uma versão congelada das fronteiras. Não deduza o país pelo nome do cráton.

## Três classes que não podem ser misturadas

### A. Alvos quantitativos de geoquímica

SACM, CDoGS, Yukon, SIGÉOM, NGSA, GEMAS, CGS, GEOROC e GSJ possuem valores químicos utilizáveis. Isso não os torna automaticamente intercambiáveis: SACM e GEOROC são principalmente rochas; os demais incluem solo, sedimento, till, água ou material transportado. Primeiro compare dados de mesma mídia e método; depois trate a troca de mídia como um experimento de mudança de domínio.

### B. Ocorrências e depósitos

SGB, MRDS global, MRDS Califórnia e OZMIN dizem onde há registros conhecidos. Use-os para `positive-unlabeled learning`, estratificação por commodity, distância a ocorrências e auditoria das anomalias previstas. A ausência de um ponto cadastrado **não é um negativo**, e esses arquivos não devem virar alvo de regressão de teor.

### C. Dados auxiliares ou amostras limitadas

Os dois conjuntos SoilData permitem estudar espectro, cor, ferro e profundidade em solos brasileiros, mas nesta cópia não têm coordenadas utilizáveis. G-BASE é apenas uma amostra pública da base britânica. Ambos servem para validar parsers e hipóteses; não sustentam sozinhos uma conclusão nacional.

## Schema canônico recomendado

Mantenha uma tabela longa de determinações e pivote para formato largo somente após escolher meios, métodos e painel de analitos compatíveis.

```text
dataset_id, sample_id, site_id, survey_id, citation_id,
country_iso3, region_id, latitude, longitude, crs_original,
coordinate_precision, sample_medium, material, depth,
grain_fraction, collection_year, analyte, value, unit,
qualifier, is_censored, lod, method, digestion,
deposit_id, deposit_type, commodity
```

Regras obrigatórias:

1. identificadores e códigos categóricos permanecem texto, mesmo se forem compostos só por números;
2. `ppm` em massa e `mg/kg` são numericamente equivalentes; `1% = 10.000 mg/kg`, mas equivalência de unidade não implica equivalência de digestão ou método;
3. óxidos e elementos são alvos diferentes; qualquer conversão estequiométrica deve guardar fórmula e fator usados;
4. preserve `<`, `>`, valores negativos codificados, LOD e máscara de censura; não substitua ausentes por zero;
5. preserve CRS e coordenadas originais antes de criar WGS84/EPSG:4326;
6. controles, réplicas, frações e profundidades do mesmo sítio ficam no mesmo fold;
7. ajuste imputação, transformação log/CLR/ILR, normalização e seleção de atributos usando somente o treino.

## Protocolo para regiões nunca vistas

O teste mais defensável tem dois níveis. O *outer split* isola uma região inteira antes de qualquer pré-processamento; a validação interna escolhe hiperparâmetros somente entre regiões do treino.

1. **Congelar o holdout:** escolher país, província, folha ou continente e registrar os hashes dos arquivos antes de olhar métricas.
2. **Bloquear dependências:** agrupar SACM por depósito/distrito, CDoGS por `Survey_Key`, NGSA por `SITEID`, CGS por folha, GEOROC por citação/local e GEMAS por país.
3. **Aplicar buffer espacial:** remover do treino amostras vizinhas do teste; o raio deve acompanhar o suporte espacial da coleta e do sensor.
4. **Evitar atalhos:** `country_iso3`, nome do levantamento e identificadores podem formar folds e auditorias, mas não devem ser preditores no teste de país inédito.
5. **Reportar por domínio:** apresentar MAE/RMSE por analito e por mídia, degradação em relação ao domínio visto, cobertura de incerteza e distância ao domínio de treino.

Sequência prática de experimentos:

- **Rocha → rocha:** treinar SACM e parte do GEOROC; testar países/crátons GEOROC totalmente retidos.
- **Sedimento/solo regional:** treinar subconjuntos compatíveis de Canadá, Austrália, Europa, África do Sul e Japão; reter um país/levantamento/folha inteiro.
- **País inédito forte:** treinar Estados Unidos + Canadá e testar Japão ou África do Sul; depois rotacionar continentes.
- **Mudança de mídia:** treinar rocha SACM/GEOROC e testar sedimentos. Esse resultado mede geografia **mais** matriz/protocolo e deve ser descrito assim.
- **Validação mineral:** medir proximidade e ranking das previsões contra SGB/MRDS/OZMIN sem converter regiões não cadastradas em negativos.

Boas opções de teste selado são Yukon inteiro, Québec inteiro, Japão inteiro, uma folha sul-africana, um estado australiano e países GEMAS individuais. Para sedimentos de drenagem, agregar imagens e geologia da bacia a montante é mais coerente que usar apenas o pixel da coleta. Para amostras SACM de mina/subsuperfície, filtre `SAMPLE_SOURCE`: o sensor orbital não observa diretamente o teor subterrâneo.

## Aquisição, licenças e limitações

As fontes oficiais expuseram APIs ou downloads diretos suficientes; inclusive o Dataverse SoilData respondeu pela API. Portanto, não foi necessário automatizar navegador/Playwright. Duas fontes adicionais do Yukon responderam 403/522 e ficaram registradas como candidatas no relatório, mas a quantidade e diversidade obtidas já são adequadas para montar os primeiros folds globais.

Licenças variam entre CC BY, CC BY-SA, CC0/domínio público, licenças governamentais e atribuição específica. Consulte o README de cada pasta antes de redistribuir derivados. O serviço SGB e o CGS sul-africano exigem cautela especial porque os metadados consultados indicam titularidade/atribuição, mas não uma licença Creative Commons inequívoca.

Principais riscos científicos: viés de exploração e publicação; cobertura desigual; coordenadas aproximadas; métodos e limites de detecção históricos; autocorrelação espacial; diferença entre pixel, ponto, perfil e bacia; e confusão entre ocorrência, mineralização e depósito econômico. O produto do modelo deve ser apresentado como priorização de áreas para investigação, não como prova de depósito ou estimativa de reserva.
