# 3.3 Integração de dados orbitais e geoquímicos em rejeitos de mineração

[Zhang et al. (2023)](https://www.sciencedirect.com/science/article/pii/S2666544123000059) desenvolveram um método para estimar a concentração de ouro ainda presente no depósito de rejeitos de uma mina de ouro em Witwatersrand, na África do Sul.

Os autores analisaram imagens dos satélites Landsat-8 e Sentinel-2 e utilizaram um modelo geoestatístico construído a partir de análises de amostras para representar os teores de ouro. Em seguida, realizaram a fusão de dados entre esse modelo e os dados espectrais do Sentinel-2, formando o conjunto utilizado na comparação de cinco MLAs: kNN, SVM, _Random Forest_, AdaBoost e redes neurais artificiais. A seleção dos modelos e a avaliação das previsões foram realizadas por validação cruzada em 10 partes, utilizando o coeficiente de determinação (R²), o erro absoluto mediano e o erro percentual absoluto médio. Os autores também relatam resultados de validação cruzada baseada em blocos, obtidos em 100 execuções.

Entre os algoritmos avaliados, AdaBoost apresentou os melhores resultados, com R² de 0,917 e erro percentual absoluto médio de 2,7%. Os modelos permitiram gerar mapas de concentração de ouro com resolução espacial de 10 metros. Os autores destacam que a confiabilidade das previsões depende da semelhança entre os materiais presentes na área de aplicação e aqueles representados nos dados de treinamento.

Assim como este trabalho, o estudo associa dados espectrais de satélite a análises geoquímicas para predizer teores. Diferentemente dele, que comparou algoritmos para estimar ouro em uma única instalação de rejeitos, este trabalho avaliará o TabPFN na previsão de ocorrências minerais e na predição de diversos elementos e óxidos em diferentes regiões.
