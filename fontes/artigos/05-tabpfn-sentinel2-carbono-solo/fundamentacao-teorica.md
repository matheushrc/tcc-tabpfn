# Leitura orientada — Chen et al.

**Situação:** leitura e redação pelo autor pendentes.

## Roteiro de leitura — sugestões da IA

**Organização deste arquivo:** mantenha o roteiro, as observações sobre a revisão e as propostas da IA, quando solicitadas, antes de “Anotações do autor”. Essa última seção fica no fim do arquivo para permitir a continuidade da escrita sem interrupções. A proposta da IA é cumulativa: preserve os trechos aprovados e atualize-a até a conclusão indicada pelo autor; ao final, deixe apenas o subtópico numerado, seu título e o texto consolidado, sem o rótulo de versão da IA, crases, anotações do autor ou seções de apoio, após conferir a incorporação do conteúdo aprovado e de suas fontes.

**Foco:** TabPFN com dados orbitais Sentinel-2 em regressão; fecha o bloco de composição química.

**Artigo para consulta:** [Integrating transformer-based learning and Sentinel-2 bare soil composites for soil organic carbon mapping in the black soil region of Northeast China](https://www.nature.com/articles/s41598-025-33682-4).

Este roteiro orienta a leitura e as anotações. A redação da fundamentação teórica e da análise acadêmica será feita pelo autor; os itens abaixo não constituem texto pronto para o TCC.

### Roteiro na ordem de escrita do guia

Os tópicos seguem a estrutura de `templates/guia-trabalhos-relacionados.md` (seções 1.1 e 1.2): problema e objetivo, dados, método e avaliação, resultados e limitações e relação com este TCC. Cada etapa indica onde procurar no artigo e o que registrar; as etapas 1 a 4 correspondem aos parágrafos de apresentação, dados e método e resultados, e a etapa 5, ao parágrafo de comparação.

**Ênfase do guia (seção 1.3):** artigo sobre TabPFN (1.3.2), com dados de satélite (1.3.1): tarefa, tamanho do conjunto, modelos comparados, validação, sensores e variáveis e dados de referência.

**Posição no capítulo 3 (seção 3.5):** bloco de composição química, que termina aqui. Antes: Zhang et al. (3.4), Sentinel-2 e Landsat-8 com teores de ouro interpolados por krigagem e modelos convencionais. Depois: Barkov et al. (3.6), que abre o bloco de harmonização e generalização.

#### 1. Problema e objetivo

- [ ] **Abstract; Introduction:** quais são as duas limitações que o estudo enfrenta (obter reflectância de solo exposto e depender de modelos que exigem muitos dados) e qual é o objetivo?

#### 2. Dados utilizados

- [ ] **Study area; Soil sampling and laboratory analysis:** qual é o alvo, quantas amostras há (174), em que profundidade (0–20 cm) e como a referência laboratorial é obtida?
- [ ] **Sentinel-2 imagery and preprocessing:** quais períodos, filtros e bandas são usados, como o limiar de NDVI de 0,1 a 0,4 seleciona o solo exposto e o que são as composições P50 e P90?
- [ ] **Environmental covariates; tabela 1:** quais atributos vêm do satélite e quais vêm de outras fontes?
- [ ] **Ligação com Zhang:** Zhang treina com valores interpolados; aqui as amostras são analisadas diretamente. Por que isso importa para o alvo químico do TCC?

#### 3. Método e avaliação

- [ ] **SOC modeling:** como são configurados TabPFN, CNN e XGBoost? Note que a CNN recebe um vetor por pixel, e não recortes de imagem (Discussion).
- [ ] Como funciona a avaliação por 100 iterações de bootstrap e quais métricas são usadas?
- [ ] **Model Interpretation and mapping:** como são obtidos o SHAP e o mapa de previsões?

#### 4. Resultados e limitações

- [ ] **Model performance comparison; Effect of image compositing strategies:** desempenho de cada modelo com P50 e P90 (R² de 0,78 e RMSE de 1,90 g/kg para TabPFN com P50).
- [ ] **Mechanistic insights from SHAP interpretation:** por que B12 e a precipitação se destacam?
- [ ] **Methodological implications, limitations, and future perspectives; Conclusions:** quais condições de solo e amostragem restringem as conclusões? Separe as limitações dos autores das suas observações.

#### 5. Relação com este TCC

- [ ] **Do modelo convencional ao TabPFN:** compare a escolha de modelos de Zhang com a comparação TabPFN, CNN e XGBoost de Chen.
- [ ] **Solo exposto:** o controle da vegetação responde ao problema visto em Costa (Landsat-8 descartado) e em Yang (vegetação como alvo). O que poderia ser aplicado à seleção de pixels do TCC?
- [ ] **Profundidade:** compare 0–20 cm com a superfície observada pelo satélite e com a profundidade, ainda não confirmada, das amostras de solo do SGB.
- [ ] **Alvo diferente:** por que carbono orgânico e teores de elementos ou óxidos precisam ser tratados como alvos diferentes?
- [ ] **Atributos não espectrais:** anote para decidir se o TCC usará apenas dados espectrais.
- [ ] **Validação:** o bootstrap é aleatório e local, sem zonas de exclusão nem teste em outra região. Guarde para o bloco de generalização.
- [ ] **Fechamento do bloco:** o que Kutzke, Zhang e Chen, juntos, indicam sobre prever composição a partir de espectros e o que ainda falta para alvos químicos com Sentinel-2?
- [ ] Use o modelo de comparação da seção 1.4 do guia, sem antecipar resultados.

### Conceitos para você estudar antes de escrever o capítulo 2

- [ ] Solo exposto, composições multitemporais e índices espectrais.
- [ ] Covariáveis ambientais, resolução espacial e reamostragem.
- [ ] Regressão com TabPFN, bootstrap e interpretação por SHAP.

### Antes de redigir

- [ ] Anotar as páginas, seções, tabelas ou figuras que sustentam cada informação que você pretende usar.
- [ ] Separar o que os autores propõem, executam e demonstram; registrar também os limites da avaliação.
- [ ] Identificar conceitos que exigem consultar as referências originais, preservando suas URLs completas.
- [ ] Redigir com suas palavras, citando as fontes; discutir como o estudo se aproxima e se diferencia das tarefas do seu TCC.

### Anotações do autor

Espaço reservado às suas notas de leitura e ao seu rascunho.
