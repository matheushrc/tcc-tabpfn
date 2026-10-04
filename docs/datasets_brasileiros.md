# Datasets brasileiros de áreas de exploração mineral

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
