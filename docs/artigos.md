# Estudos do capítulo 3

Dono dos motivos da seleção e dos limites de cada estudo de Trabalhos Relacionados. A pasta, o estado da análise e a autoria de cada texto estão em `fontes/README.md`; as decisões sobre a seleção e os motivos das remoções, em D17, D18 e D24 de `docs/decisoes-projeto.md` e no histórico do registro; os estudos removidos ficam em `fontes/artigos-descartados/`. O orientador pediu de 6 a 8 trabalhos relacionados.

A ordem segue as pastas `fontes/artigos/01`–`07` e as subseções 3.1–3.7: previsão de ocorrências por classificação (1–2), composição química (3–5) e harmonização e generalização entre regiões (6–7). Em cada bloco, os estudos vão do mais distante ao mais próximo da proposta.

## Estudos selecionados

### 1. Franca-Rocha et al. (2025) — prospectividade de ferro com Sentinel-2

[Identifying High-Potential Zones for Iron Mineralization in Bahia, Brazil, Using a Spectral Angle Mapper–Random Forest Integrated Framework](https://www.mdpi.com/2075-163X/15/11/1119). *Minerals*, 15(11), 1119; publicado em 27 de outubro de 2025. DOI: 10.3390/min15111119. BibTeX: `francarocha2025`.

Classifica cada pixel de um mosaico Sentinel-2 L2A da Bahia com _Random Forest_, a partir de amostras reclassificadas pelo _Spectral Angle Mapper_, e confronta o mapa com os processos da ANM e as ocorrências do SGB. É o precedente brasileiro mais próximo: reflectância Sentinel-2 por pixel e processos minerários como referência. **Limite:** uma única substância (ferro), amostras derivadas de duas minas e teste sorteado na mesma área, sem separação espacial.

### 2. Yang, Huang e Lu (2026) — classificação com TabPFN e Sentinel-2

[Mapping of Crop Planting Structures Under Limited Training Samples Using TabPFN and Sentinel-2 Time Series Data](https://www.mdpi.com/2072-4292/18/11/1857). *Remote Sensing*, 18(11), 1857; publicado em 5 de junho de 2026. DOI: 10.3390/rs18111857.

Classifica culturas agrícolas em 10 m com atributos de séries temporais Sentinel-2 (bandas, índices de vegetação, textura e coordenadas), selecionados por eliminação recursiva, e compara TabPFN com Random Forest, XGBoost e CatBoost na mesma divisão. Com 1.999 amostras de treinamento e 858 de validação, o TabPFN alcança acurácia global de 96,27% e F1 macro de 0,956; em subamostragens repetidas, mantém acurácia média de 90,60% com 30% do treinamento e 82,89% com 10%. A divisão principal 7:3 é aleatória estratificada, mas os autores acrescentam validação com zonas de exclusão de 50, 100 e 300 m em torno das amostras de treinamento (acurácia entre 0,958 e 0,962) e uma ablação das coordenadas, cuja remoção reduz a acurácia de 0,963 para 0,938. É o precedente mais próximo do protocolo de classificação proposto: atributos orbitais por pixel em formato tabular, comparação com modelos convencionais, robustez com poucas amostras e controle do uso de coordenadas. **Limite:** as classes são culturas, observadas sobretudo pela vegetação, e não substâncias minerais; não há teste em outra região ou ano, e os próprios autores indicam que as coordenadas podem reduzir a transferência e que a aplicabilidade a outros anos, regiões e sistemas ainda precisa ser testada.

### 3. Kutzke, Eichstaedt e Kahnt (2022) — diversos alvos geoquímicos

[Potential of hyperspectral-based geochemical predictions with neural networks for strategic and regional exploration improvement](https://doi.org/10.1080/08120099.2022.2094465). *Australian Journal of Earth Sciences*, 69(8), 1197–1206; publicado online em 13 de julho de 2022. DOI: 10.1080/08120099.2022.2094465. BibTeX: `kutzke2022`.

Relaciona atributos e abundâncias minerais derivados de varreduras hiperespectrais de testemunhos a referências geoquímicas, prevendo classes de teor definidas por limiares. Além da divisão aleatória 60/20/20, aplica um modelo treinado em Gawler ao cráton Yilgarn. **Limite:** essa transferência é comparada com previsões do modelo australiano geral, sem análises geoquímicas independentes de Yilgarn; semelhança entre previsões não equivale a acurácia externa. Não utiliza TabPFN ou satélite e não prevê proporções minerais. Sustenta investigar múltiplos alvos, sem garantir viabilidade para todos.

### 4. Zhang et al. (2023) — integração orbital e geoquímica

[Deriving big geochemical data from high-resolution remote sensing data via machine learning: Application to a tailing storage facility in the Witwatersrand goldfields](https://www.sciencedirect.com/science/article/pii/S2666544123000059). *Artificial Intelligence in Geosciences*, 4, 9–21. DOI: 10.1016/j.aiig.2023.01.005. BibTeX: `zhang2023`.

Relaciona atributos orbitais a um modelo geoestatístico derivado de análises de ouro em rejeitos. É uma ponte direta entre referências laboratoriais, localização e espectros para estimar teor. **Limite:** rejeitos de uma instalação não representam solos naturais mundiais nem proporções minerais. Interpolações não são novas análises independentes. Landsat-8 auxilia o alinhamento histórico e Sentinel-2 fornece os atributos preditivos; isso não estabelece superioridade geral sobre Landsat, especialmente Landsat-5.

### 5. Chen et al. (2026) — TabPFN com Sentinel-2

[Integrating transformer-based learning and Sentinel-2 bare soil composites for soil organic carbon mapping in the black soil region of Northeast China](https://www.nature.com/articles/s41598-025-33682-4). *Scientific Reports*, 16, 3784; publicado em 5 de janeiro de 2026. DOI: 10.1038/s41598-025-33682-4. BibTeX: `chen2026`.

Integra composições multitemporais de solo exposto e variáveis ambientais com 174 amostras. TabPFN com composição P50 apresenta R² de 0,78 e RMSE de 1,90 g/kg para carbono orgânico, superando CNN e XGBoost no estudo. Orienta extração orbital e controle da superfície. **Limite:** carbono orgânico do solo não equivale aos teores de elementos ou óxidos previstos neste TCC. A reamostragem local não substitui teste em regiões externas nem garante resultado para substâncias minerais.

### 6. Barkov et al. (2026) — bibliotecas harmonizadas

[From field-scale to large-scale spectral libraries: Tabular foundation models in soil spectroscopy](https://arxiv.org/html/2608.00608v1). Preprint arXiv:2608.00608v1, submetido em 1 de agosto de 2026. DOI: 10.48550/arXiv.2608.00608. BibTeX: `barkov2026`.

Compara modelos e representações espectrais em 85 tarefas de regressão com LimeSoDa e OSSL, incluindo TabPFN. Fundamenta diferentes escalas de dados e preparação dos atributos. **Limite:** usa espectros vis-NIR/MIR de amostras, não imagens orbitais; os alvos são propriedades do solo. Variabilidade entre instrumentos não demonstra benefício causal de misturar sensores. Partições aleatórias não respondem, por si, à hipótese de transferência entre regiões. Trata-se de preprint.

### 7. Huang et al. (2026) — teste externo

[Zero-shot inference with Tabular Prior-data Fitted Network (TabPFN) for soil MIR spectral analysis](https://www.sciencedirect.com/science/article/pii/S0016706126002089). *Geoderma*, 471, 117880; julho de 2026, publicado online em 29 de maio de 2026. DOI: 10.1016/j.geoderma.2026.117880. BibTeX: `huang2026`.

Compara TabPFN, PLSR, Cubist e CNN para carbono total, pH e fósforo extraível por Olsen. Utiliza treinamento KSSL e testes no Texas (620 amostras) e leste da Austrália (387), variando tamanho e semelhança espectral do treinamento. É especialmente relevante para D06–D07 pelo teste externo. **Limite:** MIR de amostras e propriedades do solo não demonstram transferência orbital ou mineralógica. A declaração de disponibilidade orienta solicitar acesso aos dados ao KSSL.


## Busca

É uma revisão dirigida, não sistemática. A busca de outubro de 2026 fez consultas em 25 idiomas, mas os estudos confirmados são quase todos em inglês. A busca complementar de 4 de novembro de 2026, com Playwright e buscador web, não encontrou estudo que aplique o TabPFN a teores de elementos, terras raras, prospectividade ou litologia a partir de satélite. Isso delimita a busca; não prova que tais estudos não existam.

Foram verificados e não selecionados:
- [Schmidinger et al. (2026)](https://arxiv.org/abs/2509.09408), sobre coordenadas no mapeamento de solo;
- [Barkov et al. (2026)](https://arxiv.org/abs/2508.09888), que se sobrepõe ao estudo 6;
- [Kasenov et al. (2026)](https://www.mdpi.com/1999-4893/19/4/302), que prevê Au, Cu e Li sem TabPFN;
- o [mapeamento de solo no norte do Cazaquistão (2026)](https://www.mdpi.com/2077-0472/16/11/1239), que cita o TabPFN sem avaliá-lo.
