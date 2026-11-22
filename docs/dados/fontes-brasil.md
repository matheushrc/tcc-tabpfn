# Datasets brasileiros de áreas de exploração mineral

Dono da descrição das bases públicas brasileiras (ANM e SGB): o que cada uma oferece e seus limites. O que foi baixado e as contagens estão em `docs/dados/dataset-brasil.md`.

Pesquisa realizada em 16 de agosto de 2026 a partir do catálogo de dados abertos da Agência Nacional de Mineração (ANM).

## Resultado

Entre as bases publicadas pela ANM, o **Sistema de Informações Geográficas da Mineração (SIGMINE)** é a única que atende ao objetivo de obter a localização e a delimitação geográfica, em escala nacional, das áreas associadas aos processos minerários.

O SIGMINE não representa cada área por apenas um ponto GPS. Ele fornece a **poligonal completa** de cada processo minerário, ou seja, a sequência de coordenadas que delimita a área. Essa representação é mais precisa do que uma única latitude e longitude.

## Comparação das bases da ANM

| Base | Informação geográfica | Cobertura e limitação |
| --- | --- | --- |
| **SIGMINE** | Polígonos georreferenciados em Shapefile e KML/KMZ | Processos minerários ativos e inativos em todo o Brasil, além de arrendamentos, áreas de servidão, bloqueios, proteção de fonte e reservas garimpeiras. É a base recomendada. |
| **Sistema Integrado de Gestão de Barragens de Mineração (SIGBM)** | Localização georreferenciada das barragens; também existem serviços de pontos e manchas de inundação | Contém somente estruturas relacionadas a barragens, não todas as áreas de mineração. |
| **Oferta Pública e Leilão de Áreas (SOPLE)** | Identifica áreas que compõem o estoque de disponibilidade e os resultados das rodadas | Abrange apenas áreas em oferta ou disponibilidade. Não representa o conjunto nacional de processos minerários. |
| **Cadastro Mineiro (SCM)** | Atributos cadastrais, incluindo processo, regime, fase, substância, titular, município e área concedida | É útil para complementar o SIGMINE, mas não é a fonte principal das poligonais. A associação pode ser feita pelo número do processo. |
| **Requerimento Eletrônico de Pesquisa Mineral (REPEM)** | Dados cadastrais e de localidade dos requerimentos eletrônicos | Abrange somente requerimentos realizados nessa plataforma e não oferece a cobertura geográfica consolidada de todos os processos. |
| **Declaração de Investimentos em Pesquisa Mineral (DIPEM)** | Município e unidade federativa | Os dados são agregados por Brasil, UF ou município e não delimitam precisamente cada área de pesquisa. |
| **Anuário Mineral Brasileiro (AMB/RAL)** | Identificação administrativa e municipal associada à produção declarada | Útil para identificar atividade produtiva, mas não fornece diretamente a poligonal de cada área. |
| **CFEM, SICOP, TAH, Dívida Ativa, Participa ANM, SAD e Protocolo Digital** | Dados financeiros, processuais ou administrativos | Não são bases nacionais de geometria das áreas minerárias. |

## SIGMINE

O catálogo da ANM descreve o SIGMINE como o conjunto das poligonais de:

- processos minerários ativos;
- processos minerários inativos;
- arrendamentos;
- áreas de servidão;
- áreas de bloqueio;
- áreas de proteção de fonte;
- reservas garimpeiras.

Os arquivos são gerados diariamente. Os processos ativos são disponibilizados em Shapefile e KML/KMZ; os processos inativos são disponibilizados em Shapefile. Há arquivos por unidade federativa e arquivos consolidados para o Brasil.

### Referência espacial

Os metadados do serviço geográfico oficial informam:

- datum: **SIRGAS 2000**;
- código de referência: **EPSG:4674**;
- projeção: coordenadas geodésicas;
- parâmetros: latitude e longitude;
- representação: vetorial;
- extensão geográfica: território nacional;
- frequência de atualização: diária.

Por serem polígonos, as coordenadas ficam armazenadas na geometria do Shapefile ou KML, e não necessariamente em colunas chamadas `latitude` e `longitude`.

### Downloads

- [Processos minerários ativos — Brasil (Shapefile ZIP)](https://dadosabertos.anm.gov.br/SIGMINE/PROCESSOS_MINERARIOS/BRASIL.zip)
- [Processos minerários inativos — Brasil (Shapefile ZIP)](https://dadosabertos.anm.gov.br/SIGMINE/PROCESSOS_MINERARIOS/PROCESSOS_INATIVOS.zip)
- [Diretório de processos minerários por estado e para todo o Brasil](https://dadosabertos.anm.gov.br/SIGMINE/PROCESSOS_MINERARIOS/)
- [Diretório geral do SIGMINE](https://dadosabertos.anm.gov.br/SIGMINE/)
- [Serviço REST geográfico da ANM](https://geo.anm.gov.br/arcgis/rest/services/SIGMINE/dados_anm/FeatureServer)

## Limitação conceitual: processo minerário não é necessariamente uma mina em operação

As poligonais do SIGMINE representam **áreas registradas em processos minerários**. Um processo ativo pode estar, por exemplo, em requerimento, autorização de pesquisa, disponibilidade ou lavra. Portanto, a base não deve ser interpretada diretamente como um inventário de áreas fisicamente escavadas ou de minas que estejam produzindo no momento.

Para selecionar somente empreendimentos com evidência de produção, recomenda-se:

1. usar o SIGMINE para obter a geometria e o número do processo;
2. associar o número do processo aos microdados do Cadastro Mineiro para recuperar regime, fase, substâncias e titulares;
3. associar o processo aos dados do Anuário Mineral Brasileiro/Relatório Anual de Lavra para verificar produção declarada no período de interesse.

O próprio suporte da ANM informa que o Shapefile do SIGMINE contém somente a primeira substância atribuída a cada processo. Quando um processo possui diversas substâncias, os microdados do Cadastro Mineiro são necessários para recuperar a relação completa.

## Obtenção de uma latitude e longitude por área

Quando a aplicação exigir apenas um ponto por processo, pode-se calcular um ponto representativo a partir de cada polígono. É preferível usar uma operação como `representative_point()`/`point_on_surface`, pois ela garante um ponto dentro da área. O centroide geométrico pode ficar fora de polígonos côncavos ou multipartes.

Para análises espaciais, deve-se preservar a geometria original sempre que possível. Converter toda a área para um único ponto elimina informações importantes sobre extensão, fronteiras, interseções e proximidade.

## SIGBM como base georreferenciada complementar

O SIGBM também contém localização geográfica, mas seu objeto é o cadastro de **barragens de mineração**. A ANM publica um CSV de barragens e serviços WFS, WMS e REST com os pontos das estruturas. O dashboard público também oferece manchas de inundação de estudos de ruptura hipotética.

Essa base pode complementar o SIGMINE em análises de segurança, mas não deve ser usada como inventário de todas as áreas de exploração mineral.

## Fontes oficiais

- [ANM — catálogo de bases de dados abertos](https://www.gov.br/anm/pt-br/acesso-a-informacao/dados-abertos/bases-de-dados)
- [Portal Brasileiro de Dados Abertos — SIGMINE](https://dados.gov.br/dados/conjuntos-dados/sistema-de-informacoes-geograficas-da-mineracao-sigmine)
- [ANM — serviço REST do SIGMINE e metadados espaciais](https://geo.anm.gov.br/arcgis/rest/services/SIGMINE/dados_anm/FeatureServer)
- [Portal Brasileiro de Dados Abertos — Cadastro Mineiro](https://dados.gov.br/dados/conjuntos-dados/sistema-de-cadastro-mineiro)
- [Portal Brasileiro de Dados Abertos — Barragens de Mineração](https://dados.gov.br/dados/conjuntos-dados/barragens-de-mineracao)
- [ANM — dashboard público de barragens](https://geo.anm.gov.br/portal/apps/dashboards/4a9d32d667b14b5ba23f66b3ecc88a65)
- [ANM — arquivos abertos do SIGBM](https://dadosabertos.anm.gov.br/SIGBM/)
- [Portal Brasileiro de Dados Abertos — SOPLE](https://dados.gov.br/dados/conjuntos-dados/oferta-publica-e-leilao-de-areas-sople)
- [Portal Brasileiro de Dados Abertos — DIPEM](https://dados.gov.br/dados/conjuntos-dados/dipem)
- [Portal Brasileiro de Dados Abertos — REPEM](https://dados.gov.br/dados/conjuntos-dados/requerimento-eletronico-de-pesquisa-mineral-repem)

## Base de Dados Geoquímica do SGB

Pesquisa da IA em 4 de novembro de 2026, feita para responder à lacuna de análises químicas, hoje em `docs/dados/dataset-brasil.md`: existe um dataset oficial brasileiro com análises laboratoriais que informem teores de vários minerais por amostra? São constatações e sugestões, não decisões do autor. Atualização no mesmo dia: o autor esclareceu que o alvo do TCC é a composição química (D01); para esse alvo, as tabelas de interesse são as de análises químicas, especialmente a de solo, e a mineralometria passa a ser apenas apoio. A plataforma foi aberta com o MCP do Playwright e os serviços foram consultados diretamente.

### Fonte encontrada

A Base de Dados Geoquímica do Serviço Geológico do Brasil (SGB) é oficial, pública e atualizada continuamente; as camadas consultadas estão identificadas como “Geoquímica Exploratória – Jul/2026” e “Geoquímica Ambiental – Jul/2026”.

- Plataforma: <https://geoportal.sgb.gov.br/geoquimica>
- Serviço ArcGIS consultável (exploratória): <https://geoportal.sgb.gov.br/server/rest/services/geologia/geoq_externa/MapServer>
- Serviço ArcGIS consultável (ambiental): <https://geoportal.sgb.gov.br/server/rest/services/gestaoterritorial/geoq_externa_amb/MapServer>
- Lançamento: [MundoGEO, 29 de agosto de 2025](https://mundogeo.com/2025/08/29/servico-geologico-do-brasil-lanca-nova-plataforma-para-acesso-a-dados-geoquimicos/), com dados de 138 projetos georreferenciados.

O aviso da plataforma informa que a base está em atualização contínua e que os valores podem variar com o método analítico e a época da análise; a documentação de cada projeto está no RIGeo.

### Mineralometria: vários minerais por amostra

A tabela “Resultados analíticos de Mineralometria” informa, para cada amostra de concentrado de bateia (minerais pesados), a proporção de vários minerais ao mesmo tempo. Há 134 minerais distintos na base, como magnetita, hematita, ilmenita, zircão, monazita, ouro, cianita e turmalina.

Exemplo conferido no projeto “Mapeamento Geoquímico do Quadrilátero Ferrífero e seu Entorno”, amostra de campo `4070-MR-B-0005` (lat −20,069; lon −44,537), analisada em 2009 pela SGS Geosol, leitura “Mineralometria Semiquantitativa”: magnetita S40, limonita S40, ilmenita S15, hematita S3, zircão S3 e outros 11 minerais com S1.

Os valores são classes semiquantitativas, não percentuais exatos. Segundo [Lins e Castro (2010), CPRM](https://rigeo.sgb.gov.br/bitstream/doc/15957/1/P60_CassianoCastroetal_ConcentradoBateia.pdf):

| Código | Faixa |
| --- | --- |
| S1 | < 1% |
| S3 | 1–5% |
| S15 | 5–25% |
| S40 | 25–50% |
| S60 | 50–75% |
| S85 | > 75% |

Os códigos X, Y e Z também aparecem na base; seu significado não foi confirmado.

### Volume conferido

Contagens obtidas no serviço em 4 de novembro de 2026, quando o recorte era MG; as contagens nacionais usadas em D24 estão em `docs/dados/dataset-brasil.md`. O retângulo usado (lon −51,1 a −39,8; lat −22,95 a −14,2) envolve Minas Gerais e inclui partes de estados vizinhos.

| Tabela | Brasil | Retângulo de MG | O que mede |
| --- | --- | --- | --- |
| Mineralometria (resultados) | 676.847 resultados | 6.677 amostras | Classes de proporção de minerais |
| Solo | 851.216 resultados | 4.272 amostras | Teores de elementos químicos |
| Sedimento de corrente | — | 35.854 amostras | Teores de elementos químicos |
| Rocha | — | 7.048 amostras | Teores de elementos químicos |
| Concentrado de bateia | — | 7.808 amostras | Teores de elementos químicos |

O projeto do Quadrilátero Ferrífero tem 1.136 amostras de mineralometria. Outros projetos com mineralometria na região incluem Vazante-Paracatu, Serra Negra/Salitre (fosfato), Lítio Fase 2 e Jequitinhonha.

### Ressalvas para o TCC

1. **Não é solo da área de mineração.** A mineralometria vem de sedimento de rio concentrado e representa a bacia a montante do ponto, não o pixel onde foi coletado. A associação natural com o Sentinel-2 seria por bacia de drenagem, e não ponto a pixel; a drenagem da BCIM do IBGE (`datasets/brasil/Drenagem/`, ver `docs/dados/dataset-brasil.md`) pode apoiar essa delimitação.
2. **O solo tem química elementar.** Permite prever teores de elementos (Fe, Al, Mn…), que correspondem ao alvo de composição química de D01 (permanência em D24); na proposta vigente, a geoquímica do SGB entra como atributo (D24). É a tabela mais diretamente útil desta base, por ser de amostra pontual.
3. **Relação com as áreas de mineração.** As áreas de processos minerários da ANM (SIGMINE, baixado em escala nacional; ver `docs/dados/dataset-brasil.md`) são requeridas pelas empresas. Não foi encontrada base pública com as análises apresentadas nesses processos. A base do SGB é o levantamento público oficial de apoio à prospecção, mas não foi verificado se é usada formalmente para delimitar áreas da ANM.
4. **Datas.** A base é atualizada continuamente, mas cada amostra tem a data da sua análise (por exemplo, 2009 no Quadrilátero Ferrífero).

### Outras fontes encontradas

- [Atlas Geoquímico de Minas Gerais](https://agenciagov.ebc.com.br/noticias/202608/atlas-geoquimico-de-minas-gerais-reune-dados-sobre-a-distribuicao-de-elementos-quimicos-no-solo-agua-e-sedimentos-sgb) (SGB, 2026): cerca de 10 mil amostras de sedimento, solo e água, campo de 2009 a 2013; química elementar.
- [BDSolos e PronaSolos, da Embrapa](https://www.alice.cnptia.embrapa.br/alice/bitstream/doc/1026056/1/2015043.pdf): perfis de solo do país; não foi confirmado se há dados mineralógicos exportáveis.
- [CODEMGE](https://www.agenciaminas.mg.gov.br/noticia/governo-de-minas-passa-a-disponibilizar-levantamentos-aerogeofisicos-do-estado-gratuitamente/): aerogeofísica e mapas geológicos de MG, sem geoquímica de solo.
- [GeoSGB](https://geosgb.sgb.gov.br/geosgb/about_geosgb_en.html): não respondeu durante a pesquisa (conexão recusada).
