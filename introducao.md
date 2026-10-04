# 1 INTRODUÇÃO

## 1.1 APRESENTAÇÃO

Nos últimos anos, estudos têm aplicado _machine learning_ a dados de sensoriamento remoto para apoiar o mapeamento geológico e a estimativa de informações geoquímicas. Na Província Mineral de Carajás, por exemplo, métodos de _machine learning_ foram empregados no mapeamento litológico com dados geofísicos, de relevo e de sensoriamento remoto (Costa et al., 2019: <https://doi.org/10.29396/jgsb.2019.v2.n1.3>). Outro estudo combinou dados Landsat-8 e Sentinel-2 com análises geoquímicas para estimar a concentração de ouro em uma instalação de rejeitos (Zhang et al., 2023: <https://doi.org/10.1016/j.aiig.2023.01.005>). O sensoriamento remoto permite observar grandes áreas, inclusive locais de difícil acesso, e pode ajudar a selecionar pontos para investigação posterior. As previsões obtidas, contudo, precisam ser verificadas com dados geológicos e análises físicas.

As informações espectrais registradas por sensores remotos dependem da interação entre a radiação eletromagnética e os materiais presentes na superfície terrestre. Características de absorção, como posição e profundidade, podem estar relacionadas à composição dos materiais; estudos também mostram relações entre dados espectrais e variáveis geoquímicas, embora essa relação dependa do sensor, da superfície observada e dos dados de referência (Bai e Zhao, 2023: <https://www.mdpi.com/2072-4292/15/4/930>; Zhang et al., 2023: <https://doi.org/10.1016/j.aiig.2023.01.005>).

O TabPFN é um _foundation model_ para dados tabulares, pré-treinado com conjuntos de dados sintéticos. Durante a inferência, recebe os exemplos de treinamento como contexto para fazer previsões sobre novos exemplos, podendo ser aplicado a tarefas de classificação e regressão sem que seus parâmetros precisem ser treinados do zero para cada conjunto de dados (Hollmann et al., 2025: <https://www.nature.com/articles/s41586-024-08328-6>). Aplicações recentes já investigam o TabPFN em problemas próximos, como a previsão de propriedades do solo a partir de dados espectrais e a caracterização geotécnica (<https://arxiv.org/abs/2608.00608>; <https://doi.org/10.1016/j.geoai.2025.100040>). Esses estudos mostram que o uso do modelo em dados relacionados ao solo e à geociência já começou. Ainda assim, permanece relevante investigar seu comportamento na classificação litológica e na predição de composição mineral usando dados espectrais obtidos por satélite, objetivos específicos deste trabalho.

Este trabalho propõe-se a avaliar o desempenho do TabPFN na classificação litológica e na predição da composição mineral a partir de dados espectrais de satélite. A avaliação será realizada com base nos valores observados das amostras e em procedimentos de validação adequados à distribuição espacial dos dados. Busca-se, assim, verificar se o modelo pode apoiar uma triagem inicial de áreas para investigação, sem substituir a coleta e a análise física em campo.

## 1.2 PROBLEMA DE PESQUISA

Em que medida o TabPFN pode classificar litologias e predizer a composição mineral a partir de dados espectrais de satélite, e até que ponto suas previsões podem auxiliar na priorização de áreas para validação física em campo?

## 1.3 HIPÓTESE DE PESQUISA

A hipótese deste trabalho é que os dados espectrais de satélite contêm informações que permitem ao TabPFN produzir previsões de litologia e composição mineral com capacidade preditiva mensurável em amostras não utilizadas no ajuste do modelo. Considera-se também que essas previsões podem apoiar a priorização de áreas para validação física, desde que sua incerteza e suas limitações sejam consideradas.

## 1.4 OBJETIVOS

## 1.4.1 Objetivos gerais

Avaliar o desempenho e a aplicabilidade do TabPFN na classificação litológica e na predição da composição mineral a partir de dados espectrais de satélite.

## 1.4.2 Objetivos específicos

- Definir e preparar os dados espectrais e geológicos utilizados no estudo, incluindo as variáveis de entrada e os alvos de classificação litológica e predição da composição mineral;
- Aplicar o TabPFN às tarefas propostas, utilizando dados espectrais de satélite para gerar previsões de litologia e composição mineral;
- Avaliar as previsões com métricas adequadas e validação que considere a distribuição espacial das amostras, analisando o potencial e as limitações do modelo para priorizar áreas para validação física.

## 1.5 JUSTIFICATIVA

O Brasil detém a segunda maior reserva de terras raras do mundo, mas responde por apenas 1% da produção global; além disso, apenas 30% do território brasileiro está mapeado (fonte original: <https://g1.globo.com/jornal-nacional/noticia/2026/07/11/brasil-tem-2a-maior-reserva-de-terras-raras-do-mundo-mas-so-1percent-da-producao-global.ghtml>). Esse cenário tem levado o poder público a atuar diretamente sobre a lacuna: em setembro de 2026, o governo federal sancionou uma política nacional voltada à ampliação da pesquisa, extração e processamento de minerais críticos e estratégicos, prevendo até R$ 7 bilhões em instrumentos de incentivo e um aumento expressivo — de R$ 8 milhões para R$ 300 milhões — no orçamento destinado à investigação do subsolo brasileiro (fonte original: <https://www.jornalhoraextra.com.br/destaques/brasil-cria-politica-para-ampliar-producao-de-minerais-criticos>). Nesse contexto, o desenvolvimento de métodos mais eficientes para a classificação litológica e a predição de composição mineral a partir de dados de sensoriamento remoto se torna especialmente relevante, uma vez que pode contribuir para acelerar o mapeamento geológico do país e subsidiar decisões estratégicas relacionadas à exploração desses recursos.

O TabPFN será investigado por ser um modelo voltado para dados tabulares, como os formados por bandas espectrais e índices de sensoriamento remoto. Assim, o trabalho busca verificar se essa abordagem pode apoiar o mapeamento inicial de áreas de interesse, sem substituir a confirmação geológica e ambiental em campo (fonte original: <https://www.nature.com/articles/s41586-024-08328-6>).

Do ponto de vista legal e institucional, o mapeamento de informações geológicas e minerais está relacionado às atribuições da Agência Nacional de Mineração (ANM), criada pela Lei nº 13.575/2017 para promover a gestão dos recursos minerais da União, além de regular e fiscalizar as atividades de aproveitamento desses recursos (fonte original: <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2017/lei/l13575.htm>). O Plano Nacional de Mineração 2050 também reconhece a necessidade de ampliar o conhecimento geológico do território brasileiro e destaca a importância dos minerais críticos e estratégicos para a transição energética, a segurança alimentar, a tecnologia e a soberania nacional (fonte original: <https://www.gov.br/mme/pt-br/assuntos/secretarias/geologia-mineracao-e-transformacao-mineral/pnm-2050/sobre-o-pnm-2050>). Portanto, uma ferramenta de triagem baseada em dados espectrais pode contribuir para organizar etapas iniciais de investigação, embora não substitua os procedimentos legais, ambientais e técnicos exigidos para a pesquisa e a lavra mineral.

Em termos práticos, a prospecção tradicional depende de levantamentos de campo, análises laboratoriais e deslocamento de equipes, atividades que podem ser demoradas e custosas quando aplicadas a grandes áreas. O uso de sensoriamento remoto associado a modelos preditivos permite analisar uma quantidade maior de pontos e indicar onde a coleta física pode ser mais informativa. Dessa forma, o resultado esperado não é confirmar a existência de uma jazida, mas apoiar a seleção de áreas para investigação posterior.


