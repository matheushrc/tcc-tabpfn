# 4 METODOLOGIA

Este trabalho parte da revisão bibliográfica e da análise dos trabalhos relacionados, que orientaram a escolha dos dados, dos rótulos, dos modelos de comparação e das métricas de avaliação. A previsão de ocorrências minerais consistirá em prever a substância mineral registrada nos processos minerários ativos da ANM em todo o Brasil, considerando as substâncias metálicas, inclusive os metais de transição, e o silício, e priorizando os elementos de terras raras. A predição da composição química e o recorte final serão definidos conforme a disponibilidade de referências adequadas e os resultados das avaliações preliminares. As etapas previstas são:

a) identificação dos conjuntos de dados e dos rótulos utilizados nos trabalhos relacionados;

b) construção do conjunto de dados brasileiro;

c) aplicação do TabPFN e dos modelos de comparação;

d) avaliação dos resultados com métricas de classificação e de regressão;

e) disponibilização dos conjuntos derivados no Kaggle.

## 4.1 IDENTIFICAÇÃO DOS CONJUNTOS DE DADOS E DOS RÓTULOS

Serão identificados os conjuntos de dados utilizados pelos autores dos trabalhos relacionados, com seus atributos (cabeçalhos) e rótulos: a classe de minério ou substância, no caso da classificação, e teores de elementos ou óxidos medidos em laboratório, no caso da regressão. Também serão registradas a procedência dos rótulos, o material amostrado e o método analítico, para distinguir referências de campo ou de laboratório de rótulos administrativos, como os processos minerários da ANM, em que um requerimento não comprova a ocorrência do minério. No conjunto brasileiro, o rótulo será a substância declarada nos processos da ANM, e a forma de agrupar os nomes sinônimos e os minerais-minério, assim como as fases dos processos aceitas como rótulo, ainda será definida. As ocorrências minerais registradas pelo SGB, por serem observações de campo independentes dos processos, serão usadas na validação. Essa estrutura servirá de modelo para organizar os dados brasileiros.

## 4.2 CONSTRUÇÃO DO CONJUNTO DE DADOS BRASILEIRO

O conjunto de dados que servirá de entrada para o TabPFN e para o treinamento dos demais modelos será construído a partir de bases nacionais públicas, como as áreas dos processos minerários da ANM e as ocorrências minerais, a geoquímica e os mapas geológicos do SGB, seguindo a estrutura de atributos e rótulos identificada na etapa anterior. Cada amostra será associada aos valores de reflectância de imagens Sentinel-2 da mesma área. Serão utilizadas imagens de nível 2A, que fornecem a reflectância de superfície ([ESA, c2026b](https://sentiwiki.copernicus.eu/web/s2-processing)). As datas, as bandas e os limiares de nuvens e de vegetação serão definidos conforme a cobertura das áreas selecionadas, priorizando a superfície exposta, já que a cobertura vegetal pode mascarar a resposta espectral das rochas ([Grebby et al., 2011](https://nora.nerc.ac.uk/id/eprint/12796/)). Os conjuntos de outras regiões do mundo serão harmonizados com a mesma estrutura e associados a imagens Sentinel-2 pelo mesmo procedimento.

Com o conjunto montado, será realizado um estudo de ablação de atributos (_feature ablation_), que consiste em retirar grupos de atributos, como bandas ou índices espectrais, teores geoquímicos do SGB, unidade geológica e, opcionalmente, elevação e declividade, e medir o efeito dessa retirada no desempenho dos modelos, sem alterar o TabPFN pré-treinado. Procedimento semelhante foi adotado por [Yang, Huang e Lu (2026)](https://www.mdpi.com/2072-4292/18/11/1857), que retiraram as coordenadas geográficas do conjunto de atributos para verificar se o desempenho do TabPFN dependia delas. Esse estudo permitirá identificar quais atributos contribuem para as previsões. Atributos de localização, como coordenadas e relevo, serão tratados com cautela, pois podem permitir ao modelo reconhecer a região em vez da resposta espectral. Os teores geoquímicos associados a cada amostra virão do ponto de coleta mais próximo ou de interpolação, e não de uma medida no próprio pixel.

## 4.3 MODELOS

O TabPFN, na versão 3.5, será aplicado à previsão de ocorrências minerais e à predição da composição química, recebendo os exemplos de treinamento como contexto, sem que seus parâmetros sejam treinados novamente. Como o modelo de regressão prevê uma variável por vez, será ajustado um modelo para cada elemento ou óxido.

Para comparação, serão treinados nos mesmos dados modelos utilizados nos trabalhos relacionados, como _Random Forest_ ([Breiman, 2001](https://www.stat.berkeley.edu/~breiman/randomforest2001.pdf)), XGBoost, SVM, kNN e PLSR, que representam diferentes famílias de algoritmos. A seleção final dependerá da compatibilidade de cada modelo com os dados construídos.

## 4.4 AVALIAÇÃO

Para avaliar a capacidade de generalização, os dados serão divididos considerando sua distribuição espacial: amostras próximas tendem a ser semelhantes, e uma divisão aleatória pode superestimar o desempenho ([Roberts et al., 2017](https://nsojournals.onlinelibrary.wiley.com/doi/full/10.1111/ecog.02881)). Por isso, será adotada a validação cruzada por blocos espaciais em todo o Brasil, em que cada bloco reservado para teste não participa do ajuste dos modelos; o tamanho dos blocos será definido antes de qualquer treinamento.

Para avaliar se a integração de dados de diferentes regiões melhora a generalização, os modelos serão treinados com dados de uma única região e com dados de múltiplas regiões, e testados na mesma região externa. Os resultados serão registrados mesmo que não haja ganho de desempenho.

Na previsão de ocorrências minerais, serão utilizadas a acurácia global e o F1 macro, apresentados na seção 2.6. O F1 macro será calculado como a média aritmética dos F1 de cada classe, conforme [Opitz e Burst (2021)](https://arxiv.org/abs/1911.03347), atribuindo o mesmo peso a classes com diferentes quantidades de amostras ([Sokolova; Lapalme, 2009](https://www.sciencedirect.com/science/article/pii/S0306457309000259)). Na predição da composição química, serão utilizados o RMSE ([Chai; Draxler, 2014](https://gmd.copernicus.org/articles/7/1247/2014/)), o MAE ([Willmott; Matsuura, 2005](https://www.int-res.com/abstracts/cr/v30/n1/p79-82/)) e o R² ([Chicco; Warrens; Jurman, 2021](https://pmc.ncbi.nlm.nih.gov/articles/PMC8279135/)).

## 4.5 DISPONIBILIZAÇÃO DOS DADOS

Os conjuntos derivados da integração e da harmonização serão disponibilizados no Kaggle, acompanhados de documentação sobre a procedência, as transformações e as limitações dos dados. Serão publicados apenas os conjuntos cuja redistribuição seja permitida pelas licenças das fontes originais; para os demais, serão documentados os procedimentos de obtenção e preparação.
