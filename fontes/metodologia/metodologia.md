# 4 METODOLOGIA

Este trabalho parte da revisão bibliográfica e da análise dos trabalhos relacionados, que orientaram a escolha dos dados, dos rótulos, dos modelos de comparação e das métricas de avaliação. A classificação litológica e a predição da composição química serão aplicadas a elementos e regiões delimitados, priorizando os elementos de terras raras, e o recorte final será definido conforme a disponibilidade de referências adequadas e os resultados das avaliações preliminares. As etapas previstas são:

a) identificação dos conjuntos de dados e dos rótulos utilizados nos trabalhos relacionados;

b) construção do conjunto de dados brasileiro;

c) aplicação do TabPFN e dos modelos de comparação;

d) avaliação dos resultados com métricas de classificação e de regressão;

e) disponibilização dos conjuntos derivados no Kaggle.

## 4.1 IDENTIFICAÇÃO DOS CONJUNTOS DE DADOS E DOS RÓTULOS

Serão identificados os conjuntos de dados utilizados pelos autores dos trabalhos relacionados, com seus atributos (cabeçalhos) e rótulos: classes litológicas, no caso da classificação, e teores de elementos ou óxidos medidos em laboratório, no caso da regressão. Também serão registradas a procedência dos rótulos, o material amostrado e o método analítico, para distinguir referências de campo ou de laboratório de rótulos extraídos de mapas existentes. Essa estrutura servirá de modelo para organizar os dados brasileiros.

## 4.2 CONSTRUÇÃO DO CONJUNTO DE DADOS BRASILEIRO

O conjunto de dados que servirá de entrada para o TabPFN e para o treinamento dos demais modelos será construído a partir dos dados de áreas brasileiras fornecidos pelo coorientador, seguindo a estrutura de atributos e rótulos identificada na etapa anterior. Cada amostra será associada aos valores de reflectância de imagens Sentinel-2 da mesma área. Serão utilizadas imagens de nível 2A, que fornecem a reflectância de superfície ([ESA, c2026b](https://sentiwiki.copernicus.eu/web/s2-processing)). As datas, as bandas e os limiares de nuvens e de vegetação serão definidos conforme a cobertura das áreas selecionadas, priorizando a superfície exposta, já que a cobertura vegetal pode mascarar a resposta espectral das rochas ([Grebby et al., 2011](https://nora.nerc.ac.uk/id/eprint/12796/)). Os conjuntos de outras regiões do mundo serão harmonizados com a mesma estrutura e associados a imagens Sentinel-2 pelo mesmo procedimento.

Com o conjunto montado, será realizado um estudo de ablação de atributos (_feature ablation_), que consiste em retirar grupos de atributos, como bandas ou índices espectrais, e medir o efeito dessa retirada no desempenho dos modelos, sem alterar o TabPFN pré-treinado. Procedimento semelhante foi adotado por [Yang, Huang e Lu (2026)](https://www.mdpi.com/2072-4292/18/11/1857), que retiraram as coordenadas geográficas do conjunto de atributos para verificar se o desempenho do TabPFN dependia delas. Esse estudo permitirá identificar quais atributos contribuem para as previsões.

## 4.3 MODELOS

O TabPFN, na versão 3.5, será aplicado à classificação litológica e à predição da composição química, recebendo os exemplos de treinamento como contexto, sem que seus parâmetros sejam treinados novamente. Como o modelo de regressão prevê uma variável por vez, será ajustado um modelo para cada elemento ou óxido.

Para comparação, serão treinados nos mesmos dados modelos utilizados nos trabalhos relacionados, como _Random Forest_ ([Breiman, 2001](https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf)), XGBoost, SVM, kNN e PLSR, que representam diferentes famílias de algoritmos. A seleção final dependerá da compatibilidade de cada modelo com os dados construídos.

## 4.4 AVALIAÇÃO

Para avaliar a capacidade de generalização, os dados serão divididos considerando sua distribuição espacial: amostras próximas tendem a ser semelhantes, e uma divisão aleatória pode superestimar o desempenho ([Roberts et al., 2017](https://nsojournals.onlinelibrary.wiley.com/doi/full/10.1111/ecog.02881)). Por isso, pretende-se reservar para teste regiões que não participem do ajuste dos modelos, definidas antes de qualquer treinamento.

Para avaliar se a integração de dados de diferentes regiões melhora a generalização, os modelos serão treinados com dados de uma única região e com dados de múltiplas regiões, e testados na mesma região externa. Os resultados serão registrados mesmo que não haja ganho de desempenho.

Na classificação litológica, serão utilizadas a acurácia global e o F1 macro, apresentados na seção 2.6. O F1 macro será calculado como a média aritmética dos F1 de cada classe, conforme [Opitz e Burst (2021)](https://arxiv.org/abs/1911.03347), atribuindo o mesmo peso a classes com diferentes quantidades de amostras ([Sokolova; Lapalme, 2009](https://www.sciencedirect.com/science/article/pii/S0306457309000259)). Na predição da composição química, serão utilizados o RMSE ([Chai; Draxler, 2014](https://gmd.copernicus.org/articles/7/1247/2014/)), o MAE ([Willmott; Matsuura, 2005](https://www.int-res.com/abstracts/cr/v30/n1/p79-82/)) e o R² ([Chicco; Warrens; Jurman, 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8279135/)).

## 4.5 DISPONIBILIZAÇÃO DOS DADOS

Os conjuntos derivados da integração e da harmonização serão disponibilizados no Kaggle, acompanhados de documentação sobre a procedência, as transformações e as limitações dos dados. Serão publicados apenas os conjuntos cuja redistribuição seja permitida pelas licenças das fontes originais; para os demais, serão documentados os procedimentos de obtenção e preparação.

## Anotações do autor

Notas da reunião com o orientador:

Vou identificar os datasets, adaptalos com dados brasileiros (Pegar um dataset que já foi treinado para fazer isso e usar os cabeçalhos desses para aplicar nos datasets brasileiros), utilizarei as principais métricas em machine learning (vai ser utilizado acurácia, F1 score, usar referências ou explicar a fórmula)
Escrever delimitando sem delimitar de verdade (só terras raras) vou fazer o trabalho para minérios selecionados, (na banca eu digo que vou fazer para terras raras, mas vamos avaliar os resultados)
"A classificacao litologica e a regressão química do solo será aplicada para minérios e regiões delimitadas.

Metodologia reescrita:

Para criar o dataset brasileiro que servira de entrada para o tabpf e de treinamento dos outros modelos de machine learning irei identificar os rotulos usados pelos autores dos trabalhos relacionadados e fazer ablation no dataset
Com o dataset montadado começarei a realizar o treinamento de outros modelos de ia para comparação com o tabpfn, (talvez fazer com todos os que os autores usaram?) No uso deles para realizar a classificacao litologica e a regressão química do solo será aplicada para minérios e regiões delimitadas E para comparar utilizarei as principais metricas em machine learning( vai ser utilizada acuracia, f1 score, ...) (meu professor disse que qualquer termo que eu mencionar aqui pode ser explicado na propria metodologia, se vc achar que fica muito grande existe a possibilidade de colocar na revisão bibliografica)
