# América do Norte — inventário de geoquímica e depósitos minerais

Pesquisa e aquisição: 21 de agosto de 2026. Fontes oficiais/primárias foram priorizadas. Nenhum arquivo individual acima de 500 MB foi baixado. O NGDOD/SACM já presente no repositório foi inventariado, mas não duplicado.

## Resultado executivo

Há quatro conjuntos imediatamente utilizáveis na frente norte-americana:

| País/região | Dataset | Classe | Situação | Papel no TCC |
|---|---|---|---|---|
| EUA, múltiplos estados | NGDOD/SACM Legacy | **geoquímica de rocha/minério** | já existia em `SACM/` | alvos multielementares e tipo de depósito |
| EUA, Califórnia | MRDS Califórnia aprimorado | **ocorrência/depósito** | baixado, 42.744 pontos | grupos, commodities, tipos de depósito e teste regional; não é matriz de teores |
| Canadá, múltiplos levantamentos | CDoGS pacote 0434 | **geoquímica de sedimento** | baixado, 13.654 análises | transferência entre 17 levantamentos e censura/LOD explícitos |
| Canadá, sudoeste do Yukon | GSC Open File 2859 | **geoquímica de sedimento/água** | baixado, 623 locais | região aurífera/mineralizada totalmente separável |
| Canadá, Québec | SIGÉOM amostras de sedimento | **geoquímica regional** | baixado, 561.232 registros | grande domínio externo para treino ou teste cego por província/material |

O detalhamento de arquivos, checksums, licença e uso está em `datasets/estados_unidos/README.md` e `datasets/canada/README.md`. Cada dataset baixado tem metadado/dicionário no próprio diretório; o SACM usa seus `DataDictionary.csv` e `SACM_MD.xml` existentes.

## 1. Geoquímica

### NGDOD/SACM — existente, sem nova cópia

Fonte: [USGS DOI 10.5066/P944U7S5](https://doi.org/10.5066/P944U7S5).

É a melhor tabela norte-americana encontrada para o objetivo central: quase 30 mil amostras históricas de rocha/minério com coordenadas, geologia, sistema/tipo de depósito e *best values* químicos. `Geochem_BV.csv` já junta coordenadas e alvos; `ChemData1/2` preserva determinações, método, unidade e qualificadores.

Risco para ML: há forte dependência por depósito/distrito e heterogeneidade analítica histórica. Divisão aleatória por amostra mede memorização espacial. O identificador de depósito/distrito deve formar grupos indivisíveis e negativos codificados precisam ser tratados como censura.

### CDoGS pacote 0434 — baixado

Fonte: [Natural Resources Canada / GSC](https://geochem.nrcan.gc.ca/cdogs/content/pkg/pkg00434_e.htm); licença [Open Government Licence — Canada](https://open.canada.ca/en/open-government-licence-canada).

O XLSX tem 13.654 linhas e 49 colunas; 12.946 linhas possuem NAD83 longitude/latitude. Ele reúne 17 levantamentos e análise INAA uniforme de 35 grandezas, incluindo Au em ppb, Na/Fe em %, demais elementos principalmente em ppm e massa em gramas. A variante baixada usa valores negativos para resultados abaixo do LOD. Isso permite criar simultaneamente `valor`, `is_censored` e `lod` sem fingir concentração negativa.

Por que serve: é um domínio canadense com material e laboratório diferentes do SACM. Pode testar se representações espectrais/geoquímicas sobrevivem à troca `rocha de depósito → sedimento regional` e se o modelo identifica anomalias, embora não seja legítimo interpretar ambos como a mesma variável-alvo sem estratificação.

### GSC Open File 2859 — baixado

Fonte: [CDoGS Survey 210234](https://geochem.nrcan.gc.ca/cdogs/content/svy/svy210234_e.htm); arquivo [of_2859.zip](https://geochem.nrcan.gc.ca/ftp/data/publications/pub_00185/of_2859.zip).

O produto registra 623 locais de corrente em 7.825 km² no sudoeste do Yukon, com média de 1 amostra/12,6 km². Possui dados ASCII/DBF de 36 elementos, LOI e água, além de QA/QC e métodos. As posições são UTM zona 8 digitalizadas de mapas NTS 1:50.000; o datum não é declarado nos arquivos distribuídos e deve permanecer como metadado pendente até consulta do mapa original.

Por que serve: o território pode ficar completamente fora do datalake de treino e ser uma avaliação regional genuína. Os dois mapas NTS oferecem subfolds, mas a proximidade entre 115A e 115B requer *buffer* espacial.

### SIGÉOM Québec — baixado

Fonte: [Géochimie — Données Québec](https://www.donneesquebec.ca/recherche/dataset/geochimie); licença [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

O CSV de 218.619.131 bytes tem 561.232 registros, 124 colunas e coordenadas geográficas em todas as linhas. Abrange sedimento de lago/corrente, solos e frações de till, com muitos óxidos e elementos. É uma base dinâmica; a cópia é um snapshot e deve sempre guardar data e checksum.

Por que serve: o Québec sozinho é grande o bastante para um teste externo e inclui materiais de superfície mais relacionados ao pixel orbital que amostras subterrâneas. Porém, mistura campanhas, métodos, matrizes e códigos de censura; modelos devem ser condicionados/estratificados por `CODE_ECHN`, projeto e relatório.

## 2. Ocorrências e depósitos

### MRDS Califórnia aprimorado — baixado

Fonte: [USGS DOI 10.5066/P9HTERGK](https://doi.org/10.5066/P9HTERGK); direitos indicados como [CC0](https://creativecommons.org/publicdomain/zero/1.0/).

São 42.744 pontos WGS84, todos coordenados, com commodity, status, minerais, rocha hospedeira, alteração, estruturas e 328 nomes de modelo de depósito. O ganho sobre o MRDS genérico é a cobertura de tipo de depósito e a tabela que relaciona classificações do Brasil, USGS, GSC e British Columbia.

Uso correto: camada auxiliar para ligar amostras SACM a distritos/tipos, auditar cobertura e formar grupos. Não usar `Occurrence` como positivo e todo o restante como negativo; locais não cadastrados continuam não rotulados. `grade` é texto histórico e não substitui análise química.

## 3. Dados auxiliares e candidatos não baixados

### MRDS completo — ocorrência global, não geoquímica

- Serviço oficial: [USGS ArcGIS FeatureServer](https://energy.usgs.gov/arcgis/rest/services/Hosted/Mineral_Resource_Data_System/FeatureServer/0).
- Contagem consultada: 304.632 feições; limite de 2.000 por resposta e schema do serviço atual reduzido a `dep_id`, `site_name`, `dev_stat`, `code_list`, `grade` + geometria.
- Não baixado: exigiria paginação de uma coleção mundial e agrega pouco ao CSV Califórnia/SACM; é útil depois para testes de cobertura de ocorrência, não para regressão de teores.
- Comando base futuro (paginar `resultOffset`):

```bash
curl --get 'https://energy.usgs.gov/arcgis/rest/services/Hosted/Mineral_Resource_Data_System/FeatureServer/0/query' \
  --data-urlencode 'where=1=1' \
  --data-urlencode 'outFields=*' \
  --data-urlencode 'returnGeometry=true' \
  --data-urlencode 'outSR=4326' \
  --data-urlencode 'resultRecordCount=2000' \
  --data-urlencode 'resultOffset=0' \
  --data-urlencode 'f=geojson'
```

### Yukon Mineral Deposits by Zone — candidato prioritário com teores

- Catálogo: [Open Government Portal](https://open.canada.ca/data/en/dataset/2faf0800-d713-4cc9-aa3c-244df5f32b6f).
- Licença: [Open Government Licence — Yukon](https://open.yukon.ca/open-government-licence-yukon).
- Conteúdo descrito: centroide de zonas, propriedade, teor médio e recurso total por commodity, data, fonte e nível de confiança. É complementar ao CDoGS porque mede **teor de depósito**, não apenas sedimento regional.
- Não baixado: em 2026-08-21, o ArcGIS retornou HTTP 522 e o ZIP do portal retornou 403. O browser automatizado Playwright não estava disponível neste ambiente; a quantidade de fontes acessíveis não ficou baixa, portanto a aquisição continuou por APIs/HTTP oficiais.
- URLs completas para nova tentativa:
  - `https://mapservices.gov.yk.ca/arcgis/rest/services/GeoYukon/GY_Geological/MapServer/120`
  - `https://open.yukon.ca/data/2faf0800-d713-4cc9-aa3c-244df5f32b6f/resource/d22103bd-2a60-4ac9-addb-e21ca5943a78/download/mineral-deposits-by-zone-89fks1r6.zip`

### Yukon Regional Geochemical Database — candidato de escala territorial

- Catálogo: [Open Government Portal](https://open.canada.ca/data/en/dataset/a7d25aa3-4b25-412c-a5db-84ed648aad4d).
- Licença: Open Government Licence — Yukon.
- Recursos oficiais: `Regional_Geochemical_Surveys_RGS_250k.xls.zip` e FGDB.
- Não baixado: host `ygsftp.gov.yk.ca` respondeu 403. URL XLS para reaquisição:
  `https://ygsftp.gov.yk.ca/YGSIDS/compilations/RGS_Reanalysis/November_2020/Regional_Geochemical_Surveys_RGS_250k.xls.zip`.

### CDoGS nacional — catálogo auxiliar

A [home CDoGS](https://geochem.nrcan.gc.ca/cdogs/content/main/home_en.htm) registrava 1.646 levantamentos, 292 padronizados, 219.201 locais e mais de 13 milhões de valores analíticos na síntese de 2025-05-04. Não existe um único arquivo cru nacional explicitamente oferecido; os downloads são organizados por levantamento/pacote. Use o índice para expandir regiões de teste de forma controlada, não tente baixar a coleção sem limite.

### Québec rocha — candidato complementar

O catálogo Données Québec lista um CSV de amostras de rocha de aproximadamente 315 MB, ainda abaixo do teto definido, mas o URL oficial retornou 404 durante esta execução. Repetir a partir da ficha do dataset, pois os caminhos SIGÉOM mudam. A versão de sedimentos foi acessível e baixada.

## 4. Schema comum recomendado

Não concatene arquivos largos diretamente. Normalize primeiro para uma tabela longa:

| Campo comum | Origem/exemplo |
|---|---|
| `dataset_id` | `sacm`, `cdogs_pkg0434`, `gsc_of2859`, `sigeom_qc` |
| `survey_id` | `REF_SHORT_NAME`, `Survey_Key`, Open File/NTS, `PROJ_SEDM` |
| `site_id` | `SACM_ID`, `Site_Key`, mapa+sample, `ECHN_UNIQ` |
| `sample_material` | rocha/minério, lago, corrente, água, solo, till |
| `latitude`, `longitude` | sempre com `crs_source` e método de transformação |
| `analyte` | símbolo químico/óxido normalizado |
| `value` | valor numérico detectado ou limite para censurado |
| `unit` | `%`, ppm, ppb; nunca inferir pelo nome sem dicionário |
| `qualifier` | detectado, `<`, `>`, ausente, não amostrado |
| `lod` | limite de detecção quando recuperável |
| `method` | INAA, AAS, ICP etc. |
| `deposit_type` | classificação original + mapeamento CMMI quando possível |

Para regressão multialvo, pivote somente depois de filtrar material/método e definir uma política de censura. Mantenha uma máscara de alvos observados; não preencha ausência analítica com zero.

## 5. Folds para regiões nunca vistas

Uma sequência defensável é:

1. **Desenvolvimento interno EUA:** SACM com `GroupKFold` por depósito/distrito e *buffer* espacial; Califórnia pode ser um estado totalmente retido.
2. **Validação canadense por levantamento:** deixar um `Survey_Key` CDoGS inteiro fora. Réplicas e QA/QC ficam com o grupo original.
3. **Holdout territorial:** Yukon Open File 2859 nunca participa de ajuste, seleção de atributos, normalização ou escolha de hiperparâmetros.
4. **Holdout provincial grande:** Québec inteiramente retido ou usado só após congelar o pipeline. Alternativamente, treinar no Québec e testar Yukon/um survey CDoGS remoto.
5. **Teste país nunca visto:** treino apenas EUA e teste Canadá, reportando separadamente por material. Como SACM é rocha/minério e os conjuntos canadenses são majoritariamente sedimento, esse teste mede país + matriz + protocolo; a interpretação deve dizer isso explicitamente.

Para cada divisão, ajuste imputação, CLR/ILR, escalonamento e seleção de elementos **somente no treino**. Compare `random split` apenas como diagnóstico otimista. Métricas recomendadas: MAE/RMSE em log-concentração por elemento, erro composicional quando aplicável, cobertura de intervalo de incerteza e degradação relativa entre domínio visto e não visto.

## 6. Relação com satélite

- Associe cada local a um *patch* e a covariáveis de qualidade (nuvem, vegetação, água, relevo, distância ao pixel válido).
- Sedimentos de drenagem resumem uma bacia a montante; o pixel no ponto de coleta pode não representar a fonte geoquímica. Para CDoGS/SIGÉOM, delimitar bacia e agregar espectro a montante é mais geologicamente coerente que usar somente o pixel.
- Amostras de minério do SACM podem vir de mina, pilha ou subsuperfície. Use `SAMPLE_SOURCE` e alteração/mineralização para filtrar; não prometa que o pixel revela diretamente o teor da rocha subterrânea.
- Separe épocas/sensores e mantenha o holdout invisível até o final. Qualquer normalização calculada com Québec/Yukon antes do teste já constitui vazamento de domínio.

## Fontes primárias principais

- [USGS NGDOD/SACM](https://doi.org/10.5066/P944U7S5)
- [USGS MRDS Califórnia](https://doi.org/10.5066/P9HTERGK)
- [USGS MRDS FeatureServer](https://energy.usgs.gov/arcgis/rest/services/Hosted/Mineral_Resource_Data_System/FeatureServer/0)
- [Natural Resources Canada — CDoGS](https://geochem.nrcan.gc.ca/cdogs/content/main/home_en.htm)
- [GSC Open File 2859 / Survey 210234](https://geochem.nrcan.gc.ca/cdogs/content/svy/svy210234_e.htm)
- [Géologie Québec — geochemistry documentation](https://gq.mines.gouv.qc.ca/documentation/informations-complementaires/geochimie/)
- [Données Québec — Géochimie](https://www.donneesquebec.ca/recherche/dataset/geochimie)
- [Yukon Mineral Deposits by Zone](https://open.canada.ca/data/en/dataset/2faf0800-d713-4cc9-aa3c-244df5f32b6f)

