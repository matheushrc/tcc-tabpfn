# Frente Europa/Oceania — levantamento de datasets

Data da verificação: 21 de agosto de 2026.

## Resultado

Foram baixados quatro conjuntos de dados reais e documentação oficial, totalizando cerca de 14 MB: NGSA e um subconjunto OZMIN de carvão para a Austrália, GEMAS continental e duas amostras G-BASE do Reino Unido. Nenhum arquivo se aproxima do limite de 500 MB. A melhor dupla imediatamente utilizável para regressão multialvo é NGSA + GEMAS; OZMIN é camada de ocorrências e G-BASE, nesta aquisição, é amostra limitada. Cada diretório agora contém um schema oficial, um guia oficial ou um `schema_inferred.json` explicitamente identificado como inferido; os READMEs, sozinhos, não são usados como dicionário.

| Prioridade | Dataset | Tipo | Pontos/linhas úteis | Elementos/atributos | Adequação ao TCC |
| ---: | --- | --- | ---: | --- | --- |
| 1 | NGSA | geoquímica de sedimento de saída de bacia | 1.315 sítios; 7.893 registros de fração/profundidade/bulk | até 68 elementos, coordenadas e estado | Excelente teste continental e por estado; baixa resolução espacial. |
| 1 | GEMAS Ap | geoquímica de solo agrícola | 2.113 pontos em 34 códigos de país | 52 elementos AR, XRF/total e propriedades do solo | Excelente `leave-one-country-out` por protocolo comum. |
| 2 | OZMIN legado — carvão | depósitos/recursos de carvão | 490 feições nas duas tabelas do ZIP | commodities e recursos | Camada de validação/proximidade restrita a carvão, não alvo químico. |
| 2 | G-BASE sample | geoquímica de solo/sedimento | amostra limitada | elementos, tipo de amostra, British National Grid | Bom para testar ETL; aquisição nacional completa requer licença. |

## Candidatos pesquisados

### Austrália

1. **NGSA — adquirido.** Fonte nacional coerente, licenciada e com coordenadas. O arquivo tem digestões diferentes e linhas repetidas por sítio, logo exige normalização cuidadosa.
2. **OZMIN — subconjunto legado de carvão adquirido.** O download governamental é pequeno e antigo; apesar do título genérico no catálogo, seu conteúdo é formado pelas camadas `Cbl`/`Cbr`, não por todas as commodities OZMIN. A [coleção OGC Features atual da Geoscience Australia](https://linkeddata.pid.geoscience.gov.au/collections/mo?f=html) reportou 17.142 ocorrências, mas impôs dez feições por resposta; foram preservados schema e duas páginas de verificação. Uma coleta completa exigiria 1.715 requisições ou exportação do AGSON e deve confirmar a licença da API atual.
3. **NGSA Mercury 2025 — candidato complementar.** A GA oferece CSV oficial de 203,2 KB, DOI `10.26186/150328`, com aproximadamente 2.400 análises de Hg sobre amostras NGSA. Não foi baixado porque o NGSA principal já inclui Hg por AR/MMI e a prioridade foi diversidade regional.
4. **Heavy Mineral Map of Australia — candidato.** Dados oficiais recentes ligados às 1.315 amostras NGSA e úteis para alvos mineralógicos, mas não necessários para a primeira harmonização elementar.

### Europa

1. **GEMAS — adquirido.** O serviço da Geological Survey Ireland expõe dados harmonizados de 34 países, em WGS84 e sob CC BY 4.0. A camada Ap baixada contém todos os campos químicos em uma única feição, apesar de existir uma subcamada cartográfica por elemento.
2. **GEMAS Gr — candidato imediato.** Pastagem permanente, 0–10 cm, 2.118 amostras descritas pelo projeto. Deve ficar em tabela separada de Ap ou trazer `medium/depth` como covariável.
3. **EGDI/EuroGeoSurveys — catálogo/infraestrutura.** É fonte importante para serviços europeus, mas GEMAS foi preferido porque a instância GSI forneceu feições completas, licença clara e schema verificável sem automação de navegador.

### Reino Unido

1. **G-BASE — amostras adquiridas.** As páginas oficiais dão acesso livre apenas a exemplos. As tabelas nacionais de pontos são licenciadas sob solicitação. Grades nacionais e do sudoeste da Inglaterra são abertas em resolução de 500 m, porém são superfícies interpoladas, não amostras laboratoriais novas.
2. **Tellus Northern Ireland — candidato.** Pontos geoquímicos e aerogeofísica podem complementar o Reino Unido, mas devem ser obtidos do GSNI/OpenDataNI com licença e mídia de amostragem registradas.
3. **BGS Mineral Reconnaissance Programme/mineral occurrences — candidato auxiliar.** Útil como ocorrência/depósito; não confundir com composição química G-BASE.

## Compatibilidade com SACM

SACM e estas bases respondem a perguntas relacionadas, mas medem populações diferentes:

| Dimensão | SACM | NGSA | GEMAS | G-BASE sample | OZMIN |
| --- | --- | --- | --- | --- | --- |
| Unidade | rocha mineralizada/depósito | sedimento/regolito de bacia | solo agrícola raso | solo/sedimento | ocorrência/depósito |
| Escala | depósito/distrito | bacia continental | regional continental | local/regional | ponto cadastral |
| Química | `ppm`/`pct`, melhores valores e métodos variados | `mg/kg`, Total/AR/MMI | AR + XRF/total | métodos G-BASE | não é química |
| Coordenadas | geográficas | GDA94 | WGS84 | British National Grid | GDA94 |

Não é cientificamente seguro concatenar todas as linhas e chamar isso de uma única distribuição de “composição mineral”. O pipeline deve guardar, no mínimo, `dataset`, `country`, `region`, `sample_medium`, `depth`, `grain_fraction`, `digestion`, `method`, `unit`, `lod`, `censor_flag`, `sample_id`, `site_id`, `longitude`, `latitude` e `crs_original`.

Para alvos comuns, comece com Ag, As, Au, Cu, Fe, Li, Mn, Mo, Ni, Pb, Sb, Sn, U, W e Zn, mas crie uma matriz de compatibilidade por **elemento + digestão + unidade**. `mg/kg` e `ppm` em massa são numericamente equivalentes, enquanto percentual deve ser convertido por `1% = 10.000 mg/kg`. Essa equivalência de unidade não torna métodos analíticos diferentes equivalentes.

Uma abordagem defensável é ter duas tarefas:

- regressão de fundo regional: NGSA + GEMAS + G-BASE, com método/mídia controlados;
- transferência depósito–fundo: treinar/ajustar em SACM e medir até onde as assinaturas generalizam para pontos regionais, usando OZMIN apenas como validação espacial auxiliar.

## Folds para regiões nunca vistas

O split deve ocorrer antes da extração de imagens e antes de qualquer imputação/normalização aprendida.

1. **Outer fold continental:** deixe Austrália, Europa, Reino Unido, Estados Unidos ou Brasil completamente fora do treino. O país/continente de teste não participa do ajuste de hiperparâmetros.
2. **GEMAS por país:** `GroupKFold`/`LeaveOneGroupOut` em `COUNTRY`. Para países com poucos pontos, forme blocos previamente declarados (Nórdicos, Bálticos, Balcãs), sem agrupar com base no desempenho.
3. **Austrália por estado e bacia:** agrupe todas as frações, profundidades e duplicatas de um `SITEID`; teste `leave-one-state-out`. Um fold espacial por bacia/província é ainda melhor quando os polígonos forem incorporados.
4. **SACM por depósito/distrito:** nunca separe amostras do mesmo depósito entre treino e teste. Use depósito/distrito como grupo, depois reserve estados/províncias inteiros.
5. **Buffer espacial:** exclua do treino pontos dentro de um raio definido de pontos de validação. O raio deve refletir a escala: dezenas de quilômetros para NGSA/GEMAS e menor apenas para levantamentos densos como G-BASE.
6. **Teste congelado:** crie um manifesto com URL, data, tamanho, SHA-256 e grupos de teste. Nenhuma nova fonte da região congelada entra no datalake até o experimento final terminar.

O desenho mais forte para a tese seria treinar em SACM + subconjuntos de NGSA/GEMAS, validar em países/estados internos e manter um país europeu e um estado australiano completamente selados. Uma avaliação ainda mais rigorosa mantém um continente inteiro fora. Reporte erro por elemento, cobertura de intervalo de incerteza, distância ao domínio de treino e desempenho por mídia/método; uma média global pode ocultar falhas graves de transferência.

## Aquisição reprodutível

As URLs diretas, tamanhos e hashes estão nos READMEs de `datasets/australia`, `datasets/europa` e `datasets/reino_unido`. GEMAS foi paginado em 2.000 + 113 feições e validado por unicidade de `OBJECTID`. A API atual OZMIN não foi chamada milhares de vezes para evitar carga desnecessária no serviço; o ZIP legado de carvão e as amostras atuais deixam explícita a diferença entre subconjunto antigo e API atual incompleta.

### Metadados/dicionários presentes

| Dataset | Arquivo de decodificação | Status |
| --- | --- | --- |
| NGSA | `datasets/australia/ngsa/schema_inferred.json` | Inferido do CSV e documentação oficial; chaves, métodos, unidades, códigos, CRS e censura. |
| OZMIN legado/API | `datasets/australia/ozmin/schema_inferred.json` + `schema.json` | Inferido para ZIP de carvão; oficial para API atual. |
| GEMAS | `datasets/europa/gemas/layer_schema.json` + `GEMAS_field_manual_2008_038.pdf` + `schema_inferred.json` | Schema e manual oficiais, suplemento semântico inferido. |
| G-BASE | `datasets/reino_unido/bgs_gbase_sample/GBASEforSWEnglandUserGuide.pdf` + `schema_inferred.json` | Guia oficial e versão semântica inferida legível por máquina. |
