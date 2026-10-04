# Artigos com _novelty factor_ para o TCC

Pesquisa realizada em 21 de agosto de 2026. O recorte considera a pergunta atual do projeto: estimar teores/composição elemental a partir de assinaturas espectrais de satélite e geoquímica histórica, com aplicação à identificação de áreas prospectivas.

## Como esta lista foi montada

O “novelty factor” abaixo não é uma métrica bibliométrica. É uma avaliação de quanto cada trabalho ajuda a construir uma contribuição original e defensável para este TCC. Foram priorizados artigos que fazem pelo menos uma destas coisas:

- predizem concentração/teor, em vez de apenas presença de depósito;
- fundem satélite, espectro, geoquímica e contexto geológico;
- modelam relações espaciais com GNN ou _knowledge graph_;
- tratam mudança de região/sensor, poucos rótulos, pseudo-ausências ou incerteza;
- fornecem um caso brasileiro comparável.

Salvo quando indicado como **preprint**, os itens da lista são artigos revisados por pares. Teses, dissertações e produtos técnicos brasileiros aparecem em uma seção separada.

## Ordem de leitura sugerida

| Ordem | Artigo                                                  | Por que ler                                                | Relevância para a novidade |
| ----: | ------------------------------------------------------- | ---------------------------------------------------------- | -------------------------- |
|     1 | Zhang et al. (2023), _Deriving big geochemical data..._ | Precedente mais direto de satélite → teor de Au            | Muito alta                 |
|     2 | Bai & Zhao (2023)                                       | Fusão ASTER–geoquímica por regressão                       | Muito alta                 |
|     3 | Kutzke et al. (2022)                                    | Espectro → vários elementos simultaneamente                | Muito alta                 |
|     4 | Sihombing et al. (2024)                                 | GNN espacial aplicada diretamente à prospectividade        | Muito alta                 |
|     5 | Zhang et al. (2022)                                     | Predição de concentrações ausentes com validação espacial  | Muito alta                 |
|     6 | Santos et al. (2023)                                    | Espectro + geoquímica em depósito de ouro brasileiro       | Muito alta                 |
|     7 | Nathwani et al. (2022)                                  | Cuidados com dados composicionais, censura e generalização | Alta                       |
|     8 | Bilal et al. (2026)                                     | Satélite + PU learning + correção de viés + spatial CV     | Muito alta                 |
|     9 | Zheng et al. (2023)                                     | Adaptação de domínio condicionada ao espaço                | Alta                       |
|    10 | GFM4MPM (2024)                                          | Pré-treino auto-supervisionado e poucos rótulos            | Alta, mas é preprint       |

## Leitura prioritária — precedentes mais próximos da hipótese

### 1. Satélite multiespectral para estimar teor de ouro

**Zhang, S. E.; Nwaila, G. T.; Bourdeau, J. E.; Ghorbani, Y.; Carranza, E. J. M. (2023).** “Deriving big geochemical data from high-resolution remote sensing data via machine learning: Application to a tailing storage facility in the Witwatersrand goldfields”. _Artificial Intelligence in Geosciences_, 4, 9–21. [DOI e texto](https://doi.org/10.1016/j.aiig.2023.01.005).

- **O que faz:** funde teor de Au legado, Landsat-8 e Sentinel-2; compara modelos de ML e gera um mapa de concentração de ouro em grade de 10 m.
- **Novelty factor:** demonstra a inversão quantitativa `assinatura orbital → dado geoquímico`, não só classificação de alteração ou presença de depósito.
- **Limitação:** trabalha em uma instalação de rejeitos exposta, pequena e relativamente homogênea, com apenas Au como alvo. A geoquímica é aumentada geoestatisticamente, o que exige cuidado com vazamento espacial.
- **Uso no TCC:** deve ser a principal referência de trabalho relacionado. A extensão original seria sair de rejeitos/alvo único para depósitos naturais e regressão multielementar sob _spatial split_.

### 2. Fusão de ASTER e geoquímica por regressão

**Bai, S.; Zhao, J. (2023).** “A New Strategy to Fuse Remote Sensing Data and Geochemical Data with Different Machine Learning Methods”. _Remote Sensing_, 15(4), 930. [DOI e texto](https://doi.org/10.3390/rs15040930).

- **O que faz:** usa ASTER a 15 m para desagregar camadas geoquímicas originalmente a 2 km; compara regressão linear, Random Forest e SVR.
- **Novelty factor:** trata a imagem como evidência para produzir geoquímica espacialmente detalhada, não apenas como mais uma camada de classificação.
- **Limitação:** _downscaling_ de superfícies geoquímicas interpoladas não equivale a prever amostras independentes de depósitos.
- **Uso no TCC:** oferece um pipeline simples e reproduzível para os baselines RF/SVR/XGBoost/TabPFN e mapas contínuos por elemento.

### 3. Predição multielementar a partir de espectros

**Kutzke, A.; Eichstaedt, H.; Kahnt, R. (2022).** “Potential of hyperspectral-based geochemical predictions with neural networks for strategic and regional exploration improvement”. _Australian Journal of Earth Sciences_, 69(8), 1197–1206. [DOI](https://doi.org/10.1080/08120099.2022.2094465).

- **O que faz:** usa mais de 700 km de testemunhos hiperespectrais pareados com geoquímica para predizer Au, Ag, Cu, Fe, U, Ni, Pb, Sn, Sb, As e Bi.
- **Novelty factor:** é o precedente mais claro para `espectro → vetor de teores`, exatamente o tipo de saída multialvo proposto.
- **Limitação:** espectroscopia de testemunho tem resolução e relação sinal–ruído muito superiores às de Sentinel/Landsat; não demonstra que o mesmo seja possível em pixels orbitais mistos.
- **Uso no TCC:** ajuda a escolher elementos-alvo e a justificar uma comparação entre regressão independente e multialvo/composicional.

### 4. Inversão de Cu com hiperespectral e ML

**Ma, X.; Wang, J.; Zhou, K.; Zhang, W.; Zhang, Z.; De Maeyer, P.; Van de Voorde, T. (2024).** “New data-driven estimation of metal element in rocks using a hyperspectral data and geochemical data”. _Ore Geology Reviews_, 165, 105877. [DOI e texto](https://doi.org/10.1016/j.oregeorev.2024.105877).

- **O que faz:** estima Cu em faces frescas de rocha, testando derivadas espectrais, _continuum removal_, seleção de bandas, PLSR, SVR, MLP, RF e GBRT.
- **Novelty factor:** mostra que preparação espectral mineralogicamente informada pode ser tão importante quanto a escolha do algoritmo.
- **Limitação:** é espectroscopia proximal e de um único elemento; atmosfera, vegetação e mistura espacial não estão presentes.
- **Uso no TCC:** fundamenta a ablação `bandas brutas × índices × seleção de atributos` e impede tratar Sentinel-2 como se fosse um espectrômetro hiperespectral.

### 5. Predição de elementos ausentes em geoquímica legada

**Zhang, S. E.; Bourdeau, J. E.; Nwaila, G. T.; Ghorbani, Y. (2022).** “Advanced geochemical exploration knowledge using machine learning: Prediction of unknown elemental concentrations and operational prioritization of Re-analysis campaigns”. _Artificial Intelligence in Geosciences_, 3, 86–100. [DOI e texto](https://doi.org/10.1016/j.aiig.2022.10.003).

- **O que faz:** aprende relações entre análises antigas e modernas para reconstruir concentrações elementares ausentes e priorizar reanálises; inclui validação espacial por regiões cartográficas.
- **Novelty factor:** aproxima-se da esparsidade heterogênea do NGDOD e avalia se o modelo generaliza para uma região deixada de fora.
- **Limitação:** os preditores são outras concentrações geoquímicas, não bandas de satélite; os alvos são tratados principalmente por elemento.
- **Uso no TCC:** referência central para cobertura por elemento, máscaras de alvos ausentes e comparação entre _random CV_ e _spatial CV_.

### 6. Caso brasileiro: espectro e geoquímica no depósito Pequizão

**Santos, A. M.; Silva, A. M.; Toledo, C. L. B.; et al. (2023).** “New near-mine prospecting approach using multivariate analysis and reflectance spectroscopy to define surface footprint: A case study of the Pequizão Gold Deposit, Crixás Greenstone Belt, Central Brazil”. _Journal of Geochemical Exploration_, 250, 107243. [DOI](https://doi.org/10.1016/j.gexplo.2023.107243); [registro UnB](https://repositorio.unb.br/handle/10482/47743).

- **O que faz:** integra 939 amostras de solo, espectroscopia de reflectância, DRX, geoquímica, PCA, _clustering_ e _ensemble learning_ para identificar vetores superficiais de Au.
- **Novelty factor:** trata regolito tropical e mostra que intemperismo, mineralogia e associações multielementares podem formar um sinal prospectivo útil no Brasil.
- **Limitação:** usa espectroscopia proximal de solo, não imagem orbital.
- **Uso no TCC:** é a melhor ponte brasileira para interpretação das _features_, escolha de alvos e discussão do deslocamento EUA → Brasil.

## Modelagem espacial, poucos rótulos e validação confiável

### 7. GNN para prospectividade mineral

**Sihombing, F. M. H.; Palin, R. M.; Hughes, H. S. R.; Robb, L. J. (2024).** “Improved mineral prospectivity mapping using graph neural networks”. _Ore Geology Reviews_, 172, 106215. [DOI](https://doi.org/10.1016/j.oregeorev.2024.106215); [texto aberto em Oxford](https://ora.ox.ac.uk/objects/uuid:cd710a18-9b40-4231-b193-4e6366dcc156).

- **O que faz:** converte litologia, geoquímica e ocorrências de Cu, Fe e Sn do sul do Reino Unido em grafo e compara GNN com ML tabular.
- **Novelty factor:** amostras deixam de ser independentes; o modelo aprende relações entre vizinhos, unidades e fronteiras geológicas.
- **Limitação:** classificação binária com pontos “estéreis”; o resultado depende fortemente de como o grafo e os negativos são construídos.
- **Uso no TCC:** comparar os mesmos atributos em RF/XGBoost/TabPFN e GNN; testar arestas por distância contra distância + similaridade espectral/geologia.

### 8. Satélite, viés de amostragem, PU learning e validação espacial

**Bilal, M. A.; Hlyniana, K.; Wang, Y.; Akhter, M. P.; Sheng, S. (2026).** “Integrated Geoscientific Data with Sampling Bias Correction for Porphyry Copper Prospectivity Mapping”. _Remote Sensing_, 18(13), 2091. [DOI e texto](https://doi.org/10.3390/rs18132091).

- **O que faz:** integra ASTER, Landsat 8, relevo, geologia, falhas e proxies de esforço de levantamento; usa positive–unlabeled learning, ponderação por propensão, _stacking_ sem vazamento e _spatial block CV_.
- **Novelty factor:** modela explicitamente que depósitos conhecidos são _presence-only_ e preferencialmente amostrados; acessibilidade pode prever descoberta sem representar mineralização.
- **Limitação:** grade continental de 1 km, classificação e ganho absoluto modesto em PR-AUC; é muito recente e ainda precisa de replicação.
- **Uso no TCC:** referência para auditar viés de amostragem, separar grupos por depósito/região e evitar confiar em AUC de divisão aleatória.

### 9. Positive–Unlabeled learning específico para MPM

**Xiong, Y.; Zuo, R. (2021).** “A positive and unlabeled learning algorithm for mineral prospectivity mapping”. _Computers & Geosciences_, 147, 104667. [DOI](https://doi.org/10.1016/j.cageo.2020.104667); [código](https://github.com/CUG-MG-GROUP/PUL-for-MPM).

- **O que faz:** trata depósitos como positivos e o restante como não rotulado, comparando com OCSVM, ANN e regressão logística.
- **Novelty factor:** evita declarar automaticamente como negativo tudo o que ainda não foi descoberto.
- **Limitação:** a hipótese SCAR e a avaliação aleatória podem ser irreais em exploração espacial.
- **Uso no TCC:** sustenta a decisão de preferir regressão e, se houver baseline binário, fornece um baseline PU reproduzível.

### 10. Auto-supervisão para poucos depósitos

**Daruna, A.; Zadorozhnyy, V.; Lukoczki, G.; Chiu, H.-P. (2024).** “GFM4MPM: Towards Geospatial Foundation Models for Mineral Prospectivity Mapping”. **Preprint; não tratar como revisado por pares.** [arXiv:2406.12756](https://arxiv.org/abs/2406.12756).

- **O que faz:** pré-treina um encoder com _masked image modeling_ em geodados multimodais não rotulados e depois ajusta para depósitos Pb–Zn; inclui PU learning, incerteza e explicações.
- **Novelty factor:** aproveita a abundância de imagens sem rótulos antes de usar os poucos depósitos conhecidos.
- **Limitação:** preprint, arquitetura pesada e alvo binário; não resolve diretamente regressão composicional.
- **Uso no TCC:** inspira uma versão reduzida: autoencoder/MAE nos patches Sentinel-2 e encoder congelado antes do regressor.

### 11. Knowledge graph geológico

**Yan, Q.; Zhao, J.; Xue, L.; et al. (2024).** “Mineral Prospectivity Mapping Based on Spatial Feature Classification with Geological Map Knowledge Graph Embedding: Case Study of Gold Ore Prediction at Wulonggou, Qinghai Province”. _Natural Resources Research_, 33, 2385–2406. [DOI e texto](https://doi.org/10.1007/s11053-024-10386-6).

- **O que faz:** representa pontos, linhas, polígonos e atributos de mapas como entidades/relações; combina embeddings, CNN e GCN com geoquímica e magnetometria.
- **Novelty factor:** injeta relações como `dentro de`, `próximo de` e contexto semântico, em vez de limitar o grafo à distância euclidiana.
- **Limitação:** pipeline complexo, difícil de reproduzir e sujeito a circularidade na expansão de positivos.
- **Uso no TCC:** inspira um grafo heterogêneo simples: amostra, depósito, unidade litológica e tipo de depósito.

### 12. Incerteza causada pelas escolhas do workflow

**Zhang, S. E.; Lawley, C. J. M.; Bourdeau, J. E.; Nwaila, G. T.; Ghorbani, Y. (2024).** “Workflow-Induced Uncertainty in Data-Driven Mineral Prospectivity Mapping”. _Natural Resources Research_, 33, 995–1023. [DOI e texto](https://doi.org/10.1007/s11053-024-10322-8).

- **O que faz:** varia dimensionalidade, algoritmo e métrica de ajuste, medindo como modelos tabularmente semelhantes produzem mapas espacialmente diferentes.
- **Novelty factor:** mostra que a escolha do workflow é uma fonte de incerteza própria e que boa métrica não garante mapa estável.
- **Uso no TCC:** produzir média, dispersão e consenso espacial entre TabPFN, RF/XGBoost, GNN, sementes e construções de grafo.

## Composição e transferência entre domínios

### 13. Dados composicionais em exploração geoquímica

**Nathwani, C. L.; Wilkinson, J. J.; Fry, G.; et al. (2022).** “Machine learning for geochemical exploration: classifying metallogenic fertility in arc magmas and insights into porphyry copper deposit formation”. _Mineralium Deposita_, 57, 1143–1166. [DOI e texto](https://doi.org/10.1007/s00126-021-01086-9).

- **O que faz:** aplica CLR, PCA e vários classificadores a geoquímica de sistemas pórfiro Cu, discutindo fechamento composicional, censura, ausências e generalização.
- **Novelty factor:** mostra por que percentuais/ppm não devem ser tratados ingenuamente como variáveis euclidianas independentes.
- **Uso no TCC:** testar CLR/ILR nos alvos, política explícita para zeros/limites de detecção e reconstrução da composição após a previsão.

### 14. Transferência espacial explícita

**Zheng, Y.; Deng, H.; Wu, J.; et al. (2023).** “Space-associated domain adaptation for three-dimensional mineral prospectivity modeling”. _International Journal of Digital Earth_, 16, 2885–2911. [DOI](https://doi.org/10.1080/17538947.2023.2241432).

- **O que faz:** usa uma variante espacial de maximum mean discrepancy para alinhar voxels rasos rotulados e profundos não rotulados em um depósito de ouro.
- **Novelty factor:** incorpora posição ao alinhamento de domínios, em vez de tentar casar apenas distribuições de atributos.
- **Limitação:** classificação 3D em um único depósito; não é transferência continental ou entre sensores.
- **Uso no TCC:** medir divergência entre regiões/sensores antes da transferência e posicionar a novidade como passagem de “onde” para “quanto”.

### 15. Transfer learning e incerteza entre cinturões minerais

**Lauzon, D.; Gloaguen, E. (2024).** “Quantifying uncertainty and improving prospectivity mapping in mineral belts using transfer learning and Random Forest: A case study of copper mineralization in the Superior Craton Province, Quebec, Canada”. _Ore Geology Reviews_, 166, 105918. [DOI e texto](https://doi.org/10.1016/j.oregeorev.2024.105918).

- **O que faz:** transfere assinaturas de cinturões bem conhecidos para áreas remotas e gera 200 realizações para estimar média e desvio-padrão.
- **Novelty factor:** avalia transferência em zonas geológicas reais e torna visível a instabilidade decorrente dos negativos/modelos.
- **Uso no TCC:** desenho `modelo local × modelo transferido` e _leave-one-region-out_ com mapas de incerteza.

### 16. Transferência entre sensores hiperespectrais

**Feng, X.; Huang, J.; Chen, X.; et al. (2026).** “Research on hyperspectral remote sensing alteration mineral mapping using an improved ViT model”. _Computers & Geosciences_, 206, 106037. [DOI](https://doi.org/10.1016/j.cageo.2025.106037).

- **O que faz:** propõe um ViT com embeddings espectrais agrupados e demonstra transferência entre SASI e GF-5, com construção semiautomática de amostras e validação de campo.
- **Novelty factor:** enfrenta simultaneamente rótulos caros e generalização entre fontes.
- **Limitação:** SASI/GF-5 são hiperespectrais e muito mais próximos entre si que Sentinel-2 e Landsat MSS.
- **Uso no TCC:** referência para discutir honestamente o risco extremo do estudo histórico de Serra Pelada.

## Fusão multimodal e sensoriamento remoto para prospectividade

### 17. CNN com imagem e geoquímica para cobre pórfiro

**Fu, Y.; Cheng, Q.; Jing, L.; Ye, B.; Fu, H. (2023).** “Mineral Prospectivity Mapping of Porphyry Copper Deposits Based on Remote Sensing Imagery and Geochemical Data in the Duolong Ore District, Tibet”. _Remote Sensing_, 15(2), 439. [DOI e texto](https://doi.org/10.3390/rs15020439).

- **O que faz:** integra imagem hiperespectral, multiespectral e elementos geoquímicos em CNN, comparada a SVM e RF.
- **Novelty factor:** demonstra fusão espectral–geoquímica espacial em um sistema mineral real.
- **Limitação:** alvo binário e provável sensibilidade à escolha de negativos/split espacial.
- **Uso no TCC:** referência para patches ao redor dos pontos NGDOD e comparação `pixel tabular × patch CNN × fusão`.

### 18. Comparação entre Landsat e ASTER para alteração

**Farahbakhsh, E.; Goel, D.; Pimparkar, D.; Müller, R. D.; Chandra, R. (2025).** “Convolutional Neural Networks for Mineral Prospecting Through Alteration Mapping with Remote Sensing Data”. _PFG – Journal of Photogrammetry, Remote Sensing and Geoinformation Science_, 93, 379–400. [DOI e texto](https://doi.org/10.1007/s41064-025-00344-z).

- **O que faz:** compara CNN, KNN, SVM e MLP em Landsat 8/9 e ASTER para alterações ferruginosa, argílica e propilítica.
- **Novelty factor:** mostra empiricamente que o melhor sensor depende do mineral/alteração alvo.
- **Uso no TCC:** orienta bandas, índices e ablação por sensor; também reforça que nem todos os elementos terão sinal orbital recuperável.

## Artigos brasileiros para contextualização

### 19. Carajás: desbalanceamento e SMOTE

**Prado, E. M. G.; Souza Filho, C. R.; Carranza, E. J. M.; Motta, J. G. (2020).** “Modeling of Cu-Au prospectivity in the Carajás mineral province (Brazil) through machine learning: Dealing with imbalanced training data”. _Ore Geology Reviews_, 124, 103611. [DOI](https://doi.org/10.1016/j.oregeorev.2020.103611); [código associado](https://github.com/Eliasmgprado/GeologicalComplexity_SMOTE).

- **O que faz:** avalia SVM, SMOTE e subamostragem em 400 configurações para Cu–Au, delineando seis novos alvos.
- **Novelty factor:** quantifica, em uma província brasileira de classe mundial, como o balanço de positivos/negativos muda o mapa.
- **Limitação:** classificação sem bandas orbitais ou teor; SMOTE não transforma uma pseudo-ausência em ausência geologicamente conhecida.
- **Uso no TCC:** benchmark nacional e argumento para o framing de regressão que evita negativos artificiais.

### 20. Carajás: mineral systems + Random Forest

**Oliveira, J. K. M.; Silva, A. M.; Tavares, F. M.; Costa, I. S. L. (2025).** “Mapping Cu–Au mineral potential (IOCG and Cu–Au polymetallic) in the Northern Copper Belt, Carajás Mineral Province: A data-driven, mineral systems-based approach”. _Ore Geology Reviews_, 185, 106770. [DOI](https://doi.org/10.1016/j.oregeorev.2025.106770).

- **O que faz:** integra geologia, gravimetria, magnetometria, gamaespectrometria, estruturas e ocorrências do SGB em modelos RF separados por sistema mineral e em um mapa combinado.
- **Novelty factor:** conecta teoria de sistemas minerais, modelagem supervisionada e verificação de campo no Brasil.
- **Limitação:** CV estratificada e pontos negativos podem inflar generalização; _Prediction–Area_ não substitui teste em blocos espaciais independentes.
- **Uso no TCC:** melhor ponte para transformar conhecimento geológico em tipos de aresta e avaliar RF versus GNN no contexto brasileiro.

### 21. Carajás: coordenadas como atalho espacial

**Costa, I. S. L.; Tavares, F. M.; Oliveira, J. K. M. (2019).** “Predictive lithological mapping through machine learning methods: a case study in the Cinzento Lineament, Carajás Province, Brazil”. _Journal of the Geological Survey of Brazil_, 2(1), 26–36. [DOI](https://doi.org/10.29396/jgsb.2019.v2.n1.3); [registro SGB](https://rigeo.sgb.gov.br/handle/doc/25024).

- **O que faz:** usa RF com magnetometria, MVI, relevo e sensoriamento remoto para prever litologias, comparando modelos com e sem coordenadas.
- **Novelty factor:** explicita o dilema entre capturar contexto espacial e simplesmente memorizar localização.
- **Uso no TCC:** ablação `sem coordenadas × coordenadas como feature × coordenadas apenas nas arestas da GNN`, sempre sob validação espacial.

## Literatura brasileira complementar — não confundir com artigos

- **Meloni, R. E. (2024).** _Mapeamento de potencial mineral para depósitos de urânio na Província Uranífera de Lagoa Real usando machine learning_. Dissertação, UNICAMP. [DOI/repositório](https://doi.org/10.47749/T/UNICAMP.2024.1407820). Usa XGBoost, agrupamento espacial e interpretação em uma província brasileira real.
- **Gaia, S. M. S. (2021).** _Mapeamento preditivo de favorabilidade para ouro na porção central da Província Mineral do Tapajós, Pará_. Dissertação, UNICAMP. [RIGeo/SGB](https://rigeo.sgb.gov.br/handle/doc/22195). Compara lógica Fuzzy, pesos de evidência e SVM.
- **Oliveira, L. A. B. (2022).** _Modelagem geoquímica e mineralógica dos reservatórios carbonáticos do pré-sal da Bacia de Santos através de perfis de poços e inteligência artificial_. Dissertação, USP. [DOI/repositório](https://doi.org/10.11606/D.3.2022.tde-22022022-092113). Precedente brasileiro de saídas contínuas multielementares e mineralógicas, embora a entrada seja perfil de poço.
- **Almeida, B. D. R. (2024).** _Aplicação de técnicas de análise estatística multivariada e machine learning para o mapeamento do footprint geoquímico da mineralização de ouro no distrito mineiro de Jacobina_. Dissertação, UnB. [Repositório/Oasisbr](https://repositorio.unb.br/handle/10482/49937). Usa dados composicionais, PCA e SOM em três corpos mineralizados.
- **Naleto, J. L. C. (2018).** _Mapeamento hiperespectral de associações minerais relacionadas ao depósito de ouro de Pedra Branca, Maciço de Troia, Ceará_. Dissertação, UNICAMP. [Texto no SGB](https://rigeo.sgb.gov.br/bitstream/doc/20678/1/dissertacao_mapeamento_hiperespectral.pdf). Útil para interpretar proxies espectrais em regolito brasileiro; não usa ML.
- **SGB/CPRM (2024).** _Mapa de Favorabilidade para Urânio da Província Uranífera de Lagoa Real_. Produto técnico. [Mapa no RIGeo](https://rigeo.sgb.gov.br/jspui/bitstream/doc/24865/2/mapa_favo_uranio_lagoa_real.pdf). Integra submodelos geoquímicos, geofísicos e estruturais com XGBoost e agrupamento espacial.

## A lacuna de pesquisa encontrada

Foi encontrado que:

- satélite multiespectral + ML já foi usado para estimar **teor de Au em rejeitos**;
- espectroscopia hiperespectral já foi usada para estimar **Cu** e **vários elementos em testemunhos**;
- GNN, _knowledge graph_, PU learning, auto-supervisão e adaptação de domínio já aparecem separadamente em MPM;
- no Brasil há aplicações fortes em Carajás, Crixás, Tapajós, Lagoa Real e Jacobina.

Nesta busca, porém, não apareceu um artigo que reúna simultaneamente:

1. imagens orbitais multiespectrais como entrada;
2. uma base nacional/continental de amostras ou depósitos naturais como supervisão;
3. previsão conjunta de um vetor de teores/composição elemental;
4. validação rigorosa fora da região e fora do sensor/época.

Portanto, uma formulação de novidade defensável é:

> Avaliar regressão multialvo composicional de dados geoquímicos de depósitos naturais a partir de assinaturas orbitais, comparando modelos tabulares e espaciais sob validação por região e análise explícita de mudança de sensor.

Isso é mais preciso do que afirmar que “ninguém previu teor por satélite”, pois essa afirmação seria falsa diante de Zhang et al. (2023).

## Experimentos que mais aumentariam a contribuição

1. **Alvos:** comparar regressão independente por elemento com regressão conjunta após CLR/ILR, incluindo tratamento explícito de valores abaixo do limite de detecção.
2. **Validação:** comparar divisão aleatória, grupos por depósito e blocos/regiões espaciais. Todo scaler, imputação e seleção de atributos deve ser ajustado dentro do fold.
3. **Modelos:** RF/XGBoost/TabPFN como baselines contra uma GNN com vizinhança geográfica; depois adicionar arestas por similaridade espectral ou unidade geológica.
4. **Ablations:** bandas brutas, índices mineralógicos, patches/embeddings e fusão com contexto geológico.
5. **Incerteza:** ensembles/sementes e mapa de consenso, não somente R²/MAE médio.
6. **Serra Pelada:** tratar Landsat MSS histórico como estudo qualitativo de extrapolação extrema, não como validação quantitativa equivalente. O depósito aluvial pode não ter assinatura superficial pré-mineração recuperável.

## Observação sobre as fontes brasileiras e a CAPES

A busca complementar cobriu resultados indexados do Portal de Periódicos CAPES, SciELO, Oasisbr/IBICT, RIGeo/SGB e repositórios da UnB, UNICAMP e USP. O Portal CAPES informou que, fora da rede institucional, a pesquisa fica restrita ao conteúdo gratuito e que o acervo assinado requer login CAFe. A tentativa de usar o navegador automatizado não pôde iniciar por indisponibilidade do servidor gráfico nesta sessão; por isso, não foi alegado acesso a registros fechados. As referências brasileiras acima foram confirmadas em DOI, periódico ou repositório institucional aberto.
