# 3.5 TabPFN e composições de solo exposto do Sentinel-2

[Chen et al. (2026)](https://www.nature.com/articles/s41598-025-33682-4) avaliaram o TabPFN no mapeamento do carbono orgânico do solo em áreas agrícolas da região de solos negros do nordeste da China. Os autores apontam duas dificuldades: separar a reflectância do solo exposto dos efeitos da vegetação, dos resíduos de culturas e da umidade, e depender de modelos que exigem muitos dados, enquanto os levantamentos de solo costumam ter poucas amostras.

Foram coletadas 174 amostras superficiais de solo, de 0 a 20 cm de profundidade, e o carbono orgânico foi determinado em laboratório. Os atributos vieram de imagens Sentinel-2 de abril e maio de 2021 a 2023, antes do plantio, quando o solo fica exposto. Os autores selecionaram os pixels com índice de vegetação por diferença normalizada (NDVI) entre 0,1 e 0,4 e compararam duas composições multitemporais: o percentil 50 (P50), equivalente à mediana, e o percentil 90 (P90), que busca o solo mais seco. Além das bandas e de índices espectrais, foram usadas variáveis climáticas e topográficas de outras fontes.

O TabPFN foi comparado a uma CNN e ao XGBoost em 100 iterações de _bootstrap_, com validação nas amostras não sorteadas, utilizando o R² e a raiz do erro quadrático médio (RMSE). Com a composição P50, o TabPFN obteve R² médio de 0,78 e RMSE de 1,90 g/kg, superior à CNN (R² de 0,74) e ao XGBoost (R² de 0,72). Com a composição P90, todos os modelos tiveram desempenho um pouco menor.

Os autores reconhecem que a extensão da área e o número de amostras limitam a transferência do modelo para outras regiões e que o NDVI não separa o solo exposto dos resíduos de culturas. A avaliação reamostrou amostras de uma mesma região, sem teste em uma região externa.

Assim como este trabalho, o estudo aplica o TabPFN a dados do Sentinel-2 e controla a cobertura vegetal da superfície observada. Diferentemente dele, que prevê carbono orgânico do solo com apoio de variáveis climáticas e topográficas, este trabalho predirá teores de elementos e óxidos e ocorrências minerais a partir dos dados espectrais.
