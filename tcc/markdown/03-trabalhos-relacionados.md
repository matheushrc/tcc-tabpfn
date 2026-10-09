# 3 TRABALHOS RELACIONADOS

## 3.1 Integração de dados orbitais e geoquímicos em rejeitos de mineração

[Zhang et al. (2023)](https://www.sciencedirect.com/science/article/pii/S2666544123000059) desenvolveram um método para estimar a concentração de ouro ainda presente no depósito de rejeitos de uma mina de ouro em Witwatersrand, na África do Sul.

Os autores analisaram imagens dos satélites Landsat-8 e Sentinel-2 e utilizaram um modelo geoestatístico construído a partir de análises de amostras para representar os teores de ouro. Em seguida, realizaram a fusão de dados entre esse modelo e os dados espectrais do Sentinel-2, formando o conjunto utilizado na comparação de cinco algoritmos de aprendizado de máquina: kNN, SVM, Random Forest, AdaBoost e redes neurais artificiais. A seleção dos modelos e a avaliação das previsões foram realizadas por validação cruzada em 10 partes, utilizando o coeficiente de determinação (R²), o erro absoluto mediano e o erro percentual absoluto médio. Os autores também relatam resultados de validação cruzada baseada em blocos, obtidos em 100 execuções.

Entre os algoritmos avaliados, AdaBoost apresentou os melhores resultados, com coeficiente de determinação (R²) de 0,917 e erro percentual absoluto médio de 2,7%. Os modelos permitiram gerar mapas de concentração de ouro com resolução espacial de 10 metros. Os autores destacam que a confiabilidade das previsões depende da semelhança entre os materiais presentes na área de aplicação e aqueles representados nos dados de treinamento.

O estudo se relaciona com o presente trabalho por utilizar dados espectrais de satélite para predizer uma variável geoquímica. A principal diferença está no modelo e nas tarefas investigadas: enquanto Zhang et al. avaliaram diferentes algoritmos para estimar o teor de ouro em rejeitos de mineração, este trabalho propõe avaliar o TabPFN na classificação litológica e na predição de composição mineral. Dessa forma, o artigo oferece um exemplo de integração entre dados espectrais e dados de referência que pode orientar a preparação dos dados e a análise dos resultados deste TCC.

## 3.2 TabPFN em bibliotecas espectrais de solo

[Barkov et al. (2026)](https://arxiv.org/html/2608.00608v1) avaliaram o TabPFN na predição de propriedades do solo a partir de espectros no visível e infravermelho próximo (vis-NIR) e no infravermelho médio (MIR). Foram utilizadas duas coleções: LimeSoDa, com 13 conjuntos pequenos e 39 tarefas de regressão, e Open Soil Spectral Library (OSSL), com 46 tarefas e conjuntos de 14.166 a 82.573 amostras. Os alvos incluíram carbono, pH, argila e carbonatos, determinados por análises laboratoriais.

Os autores compararam o TabPFN 2.5 com regressão linear, regressão por mínimos quadrados parciais (PLSR), Random Forest, Cubist e redes neurais convolucionais. Também avaliaram a redução de dimensionalidade por PCA e PLS, utilizando validação cruzada aninhada e a raiz do erro quadrático médio (RMSE). O TabPFN combinado com variáveis latentes de PLS apresentou o melhor desempenho agregado nas duas coleções. Na OSSL, obteve o menor RMSE em 45,7% das tarefas.

As principais limitações foram o custo de inferência e a avaliação com partições aleatórias de amostras provenientes da mesma população, que não demonstra generalização para novas regiões ou instrumentos. A OSSL reúne dados harmonizados de diferentes laboratórios, mas o estudo não testa se a diversidade de sensores, isoladamente, melhora a predição.

Enquanto Barkov et al. (2026) fazem uma análise comparativa de seis modelos de aprendizado de máquina, este trabalho se propõe a fazer uma análise aprofundada do TabPFN na classificação litológica e na predição da composição mineral a partir de dados espectrais de satélite. O trabalho também se propõe a montar um conjunto de dados próprio, pela integração e harmonização de bases existentes de diferentes regiões, conforme a disponibilidade de referências adequadas. O possível ganho de generalização será avaliado em regiões reservadas para teste.
