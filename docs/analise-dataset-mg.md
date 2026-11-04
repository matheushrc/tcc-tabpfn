# Análise inicial do dataset de Minas Gerais

Inspeção em 3 de novembro de 2026 de `datasets/Datasets_MG_Proj_Samuel`, recebido pelo autor do coorientador. Este documento apresenta constatações e sugestões da IA, sem alterar os objetivos do TCC ou comprovar experimentos de treinamento. Os arquivos de entrada foram apenas lidos.

## Conclusão de viabilidade

O material oferece referências cartográficas para investigar classificação litológica a partir de imagens espectrais de satélite ainda a obter (D01, D03–D05). Não contém uma tabela georreferenciada de proporções minerais ou teores geoquímicos medidos que permita avaliar diretamente a predição quantitativa da composição. As bibliotecas espectrais são medições laboratoriais, não imagens orbitais das áreas mineiras.

## Inventário conferido

| Material | Conteúdo verificado | Uso possível e limite |
| --- | --- | --- |
| `Geologia/geologia_MG.shp` | 2.313 polígonos, 193 códigos de unidade; campos `NOME_UNIDA`, `SIGLA_UNID`, `LITOTIPO1`, `LITOTIPO2`, `CLASSE_ROC` e outros | Fonte de rótulos cartográficos. Uma unidade pode reunir várias rochas, sem delimitar cada ocorrência no interior do polígono. |
| `Areas_Mineracao/requerimentos_minerarios_MG_2026.shp` | 54.788 registros e 52.500 processos distintos; campos `SUBS`, `FASE`, `ANO`, `AREA_HA` e outros | Contexto administrativo e seleção exploratória de áreas; não fornece teor, abundância mineral ou localização exata de afloramentos. |
| `Assinaturas_Espectrais/` | 27 pares `.hdr`/`.sli`, com 1.783 espectros ao todo; bibliotecas USGS, JPL, JHU, IGCP e vegetação | Comparação de assinaturas e experimentos laboratoriais auxiliares. A contagem inclui medições repetidas e materiais não minerais; não equivale a 1.783 amostras independentes de Minas Gerais. |
| `Topografia_DEM/MODELO_DIGITAL_DO_TERRENO_SRTM_MG.tif` | Uma banda de elevação, 13.430 × 10.427 células; espaçamento angular aproximado de 3 segundos de arco | Relevo, declividade e controle topográfico, após conferir unidades e valores de fundo. Não contém reflectância multiespectral. |
| `Geofisica/` | 2.597 linhas de estruturas/falhamentos e 828 lineamentos geofísicos | Contexto estrutural; não são grades numéricas de magnetometria ou radiometria. |
| `Drenagem/` e `Vetor_do_Estado_de_MG/` | 13.274 linhas de drenagem e um polígono estadual | Delimitação, máscaras e contexto espacial. |

Os seis shapefiles estão em SIRGAS 2000 (EPSG:4674); o raster está em WGS 84 (EPSG:4326). A integração exige tratar os sistemas de referência e escolher um sistema métrico adequado para distâncias, áreas e margens de exclusão. Não foram encontrados arquivos de imagens Landsat ou Sentinel-2, nem tabelas de amostras laboratoriais georreferenciadas nesta pasta.

## O que os polígonos realmente informam

Nos processos minerários, `SUBS` contém uma substância cadastrada por registro. Há 211 valores distintos, incluindo `DADO NÃO CADASTRADO` em 3.461 registros. Não foram encontrados percentuais nem mais de uma substância distinta por processo nessa exportação. Há fases de requerimento, autorização, concessão e outras; o nome da pasta não significa que todos os polígonos sejam minas em operação. A [ANM descreve o SIGMINE como um cadastro de áreas de processos minerários](https://www.gov.br/anm/pt-br/assuntos/exploracao-mineral/sistemas-de-exploracao-mineral).

Uma substância cadastrada não demonstra predominância, distribuição homogênea, teor ou reserva em toda a área. `AREA_HA` é área, não proporção mineral; `ANO` é associado ao processo e não comprova data de coleta de uma amostra.

Na geologia, os campos são listas qualitativas de litotipos, não proporções minerais. Por exemplo, a unidade Nova Lima registra `Metamáfica, Metagrauvaca, Xisto` em `LITOTIPO1`, e outras rochas em `LITOTIPO2`. Esses atributos pertencem à unidade cartografada: não dizem qual rocha ocupa cada pixel, nem em que porcentagem. Não foi encontrada documentação local que permita interpretar a ordem das listas como abundância quantitativa.

## Classificação litológica: caminho mais próximo da proposta

Sugestão da IA, ainda não adotada como protocolo:

1. Confirmar com o coorientador origem, edição, escala, legenda, critérios de mapeamento e licença da camada geológica. O arquivo QGIS de metadados não informa título, resumo ou links de origem; não atribuir uma edição ou escala apenas pela aparência dos campos.
2. Definir uma legenda com significado geológico e número de exemplos adequado. As 193 unidades não equivalem a 193 litologias simples; 37 unidades têm apenas um polígono e 89 têm menos de cinco. Há 506 polígonos com `LITOTIPO1` vazio, embora todos tenham pelo menos um dos dois campos de litotipos preenchido. Não completar o primeiro campo pelo segundo sem conferir o significado da legenda.
3. Obter imagens Sentinel-2 e extrair reflectância em amostras espacialmente distribuídas, após controle de nuvens, sombras, vegetação, água e mudanças de superfície. A [documentação da missão](https://sentiwiki.copernicus.eu/web/s2-mission) distingue as resoluções nativas das bandas; reamostrar não cria detalhe espacial novo.
4. Priorizar áreas e classes com relação defensável entre superfície observada e unidade mapeada. Tratar contatos, unidades mistas e escala cartográfica como fontes de incerteza.
5. Separar treino e teste por áreas e grupos espaciais, evitando pixels próximos ou do mesmo polígono nos dois conjuntos. Conferir que as classes avaliadas estejam representadas no treinamento. Comparar inicialmente atributos espectrais; avaliar relevo ou outros atributos em experimentos separados, se autorizados.
6. Interpretar a avaliação contra o mapa como concordância com referência cartográfica. A comprovação geológica independente exige observações de campo ou outras referências independentes. Milhões de pixels com o mesmo rótulo de mapa não representam milhões de amostras geológicas independentes.

## Bibliotecas espectrais e dados mineralógicos

O arquivo `usgs_min.hdr` descreve 481 espectros em 420 comprimentos de onda, aproximadamente de 0,395 a 2,56 micrômetros; o README identifica medições de laboratório e referencia a biblioteca USGS de 1993. A biblioteca JPL tem 430 espectros distribuídos em três granulometrias. A IGCP tem 139 espectros nos cinco instrumentos, com 30 nomes de amostras distintos após normalização de caixa; o README descreve a repetição de materiais em instrumentos diferentes. Esses números não são contagens de localidades brasileiras.

Alguns nomes USGS contêm proporções de misturas, como `Hematite 2%+98%Qtz GDS76` e misturas caulinita/esmectita. São exemplos laboratoriais pontuais, sem associação espacial aos polígonos mineiros, e não constituem uma tabela completa de abundâncias para regressão regional. Seria necessário recuperar documentação e referências quantitativas de cada amostra antes de usá-los como alvos.

Possibilidades auxiliares: comparar assinaturas de materiais, investigar separabilidade de classes e simular bandas do sensor a partir de espectros laboratoriais. A simulação deve considerar as respostas espectrais por banda, disponibilizadas pela [Copernicus](https://sentinels.copernicus.eu/-/sentinel-2-spectral-response-functions-update), e somente a faixa efetivamente coberta por cada biblioteca. Por exemplo, a biblioteca JHU de minerais começa em aproximadamente 2,079 micrômetros e não permite reconstruir as bandas visíveis do Sentinel-2. Medições do mesmo espécime em instrumentos ou granulometrias diferentes devem ser agrupadas na avaliação para evitar vazamento.

Treinar com espectros de laboratório reamostrados não equivale a treinar com observações reais de satélite; a transferência precisaria ser avaliada. Misturas sintéticas poderiam formar um experimento de simulação, mas seus percentuais seriam definidos pela simulação e não proporções medidas no terreno. Esse experimento, se desejado, exigiria decisão explícita e não substitui automaticamente a avaliação prevista em D01.

## Qualidade e pendências

- As 2.313 geometrias da camada geológica passaram na verificação de validade geométrica com Shapely. Isso não verifica a exatidão geológica, sobreposições entre polígonos ou qualidade da cartografia.
- Os 27 binários espectrais têm tamanhos compatíveis com seus cabeçalhos; não foram encontrados valores não finitos. Há valores negativos em parte das bibliotecas de solo/vegetação, valores acima de um em parte da IGCP/USGS e comprimentos de onda não estritamente crescentes na biblioteca de neve: conferir os casos antes de normalizar ou interpolar, sem cortar valores automaticamente.
- O raster tem 67.749.052 células de valor zero entre 140.034.610 células, sem valor de ausência declarado. É preciso distinguir fundo de elevação válida antes de calcular atributos ou estatísticas por área; a interpretação do fundo não foi confirmada.
- Para a composição química (alvo de D01, esclarecido em 4 de novembro de 2026), solicitar referências com identificação da amostra, coordenadas, data, material/profundidade, método analítico e teores de elementos ou óxidos. Proporções minerais não são alvo do trabalho.
- Confirmar licença de uso e redistribuição antes de atender à intenção de publicação de D08.

Inspeção executada: inventário, leitura de todos os esquemas e registros vetoriais, cabeçalhos e binários espectrais, metadados e valores do raster. Não houve extração de imagens orbitais, ajuste de modelos, validação preditiva ou confirmação de campo. Dependências usadas na inspeção foram executadas em ambiente temporário, sem alterar as dependências do projeto.
