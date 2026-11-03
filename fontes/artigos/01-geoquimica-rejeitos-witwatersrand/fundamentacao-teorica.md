# Leitura orientada — Zhang et al.

## Roteiro de leitura — sugestões da IA

**Organização deste arquivo:** mantenha o roteiro, as observações sobre a revisão e as propostas da IA, quando solicitadas, antes de “Anotações do autor”. Essa última seção fica no fim do arquivo para permitir a continuidade da escrita sem interrupções. A proposta da IA é cumulativa: preserve os trechos aprovados e atualize-a até a conclusão indicada pelo autor; ao final, deixe apenas o subtópico numerado, seu título e o texto consolidado, sem o rótulo de versão da IA, crases, anotações do autor ou seções de apoio, após conferir a incorporação do conteúdo aprovado e de suas fontes.

**Foco:** Integração orbital e geoquímica.

**Artigo para consulta:** [Deriving big geochemical data from high-resolution remote sensing data via machine learning: Application to a tailing storage facility in the Witwatersrand goldfields](https://www.sciencedirect.com/science/article/pii/S2666544123000059).

Este roteiro orienta a leitura e as anotações. A redação da fundamentação teórica e da análise acadêmica será feita pelo autor; os itens abaixo não constituem texto pronto para o TCC.

### Conceitos para você estudar antes de escrever o capítulo 2

- [ ] Reflectância e resolução espacial de Landsat e Sentinel-2.
- [ ] Modelagem geoestatística, interpolação e referências laboratoriais.
- [ ] Regressão supervisionada e validação espacial.

### Seções para ler e perguntas para suas anotações

| Seção ou elemento do artigo | O que procurar e registrar |
| --- | --- |
| 1. Introduction | Que problema de integração de dados motiva o estudo e a que material ele se aplica? |
| 2.1. Remote sensing data | Qual é o papel de cada satélite, quais datas são utilizadas e como os dados são alinhados? |
| 2.2. Geochemical data source and training data | De onde vêm as análises de ouro e como elas originam os valores utilizados como alvo? |
| 2.3. Machine learning-based predictive modelling | Quais atributos, modelos, métricas e procedimentos de validação são usados? |
| 3. Results; 4.1. Deriving geochemistry from remote sensing data | Quais resultados têm suporte nas avaliações e de que semelhanças entre materiais dependem? |
| 4.2; 4.3; 5. Conclusions | Quais aplicações são demonstradas e quais são possibilidades discutidas pelos autores? |

### Perguntas para você preparar a análise do estudo no capítulo 3

- [ ] Como distinguir análises laboratoriais, interpolações e previsões neste estudo?
- [ ] A evidência permite discutir teor de ouro, identificação mineral ou proporções de minerais?
- [ ] Que critérios de alinhamento e independência dos testes você levaria à discussão do seu TCC?

### Antes de redigir

- [ ] Anotar as páginas, seções, tabelas ou figuras que sustentam cada informação que você pretende usar.
- [ ] Separar o que os autores propõem, executam e demonstram; registrar também os limites da avaliação.
- [ ] Identificar conceitos que exigem consultar as referências originais, preservando suas URLs completas.
- [ ] Redigir com suas palavras, citando as fontes; discutir como o estudo se aproxima e se diferencia das tarefas do seu TCC.


### Anotações do autor

#### 3 TRABALHOS RELACIONADOS

##### 3.1 DERIVING BIG GEOCHEMICAL DATA FROM HIGH-RESOLUTION REMOTE SENSING DATA VIA MACHINE LEARNING: APPLICATION TO A TAILING STORAGE FACILITY IN THE WITWATERSRAND GOLDFIELDS

[Zhang et al. (2023)](https://www.sciencedirect.com/science/article/pii/S2666544123000059) desenvolveram um método para estimar a concentração de ouro ainda presente no depósito de rejeitos de uma mina de ouro em Witwatersrand, na África do Sul.

Os autores analisaram imagens dos satélites Landsat-8 e Sentinel-2 e utilizaram um modelo geoestatístico construído a partir de análises de amostras para representar os teores de ouro. Em seguida, realizaram a fusão de dados entre esse modelo e os dados espectrais do Sentinel-2, formando o conjunto utilizado na comparação de cinco algoritmos de aprendizado de máquina: kNN, SVM, Random Forest, AdaBoost e redes neurais artificiais. A seleção dos modelos e a avaliação das previsões foram realizadas por validação cruzada em 10 partes, utilizando o coeficiente de determinação (R²), o erro absoluto mediano e o erro percentual absoluto médio. Os autores também relatam resultados de validação cruzada baseada em blocos, obtidos em 100 execuções.

Entre os algoritmos avaliados, AdaBoost apresentou os melhores resultados, com coeficiente de determinação (R²) de 0,917 e erro percentual absoluto médio de 2,7%. Os modelos permitiram gerar mapas de concentração de ouro com resolução espacial de 10 metros. Os autores destacam que a confiabilidade das previsões depende da semelhança entre os materiais presentes na área de aplicação e aqueles representados nos dados de treinamento.

O estudo se relaciona com o presente trabalho por utilizar dados espectrais de satélite para predizer uma variável geoquímica. A principal diferença está no modelo e nas tarefas investigadas: enquanto Zhang et al. avaliaram diferentes algoritmos para estimar o teor de ouro em rejeitos de mineração, este trabalho propõe avaliar o TabPFN na classificação litológica e na predição de composição mineral. Dessa forma, o artigo oferece um exemplo de integração entre dados espectrais e dados de referência que pode orientar a preparação dos dados e a análise dos resultados deste TCC.
