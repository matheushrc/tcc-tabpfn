# Leitura orientada — Chen et al.

**Situação:** proposta de texto da IA redigida; revisão pelo autor pendente.

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

### Proposta de texto — versão da IA

Texto redigido integralmente pela IA a pedido do autor em 4 de novembro de 2026, a partir do `artigo.md`. Números, autoria e data conferidos pela IA na página original com o MCP do Playwright em 4 de novembro de 2026; falta a revisão de redação pelo autor.

```markdown
## 3.5 TabPFN e composições de solo exposto do Sentinel-2

[Chen et al. (2026)](https://www.nature.com/articles/s41598-025-33682-4) avaliaram o TabPFN no mapeamento do carbono orgânico do solo em áreas agrícolas da região de solos negros do nordeste da China. Os autores apontam duas dificuldades: separar a reflectância do solo exposto dos efeitos da vegetação, dos resíduos de culturas e da umidade, e depender de modelos que exigem muitos dados, enquanto os levantamentos de solo costumam ter poucas amostras.

Foram coletadas 174 amostras superficiais de solo, de 0 a 20 cm de profundidade, e o carbono orgânico foi determinado em laboratório. Os atributos vieram de imagens Sentinel-2 de abril e maio de 2021 a 2023, antes do plantio, quando o solo fica exposto. Os autores selecionaram os pixels com índice de vegetação por diferença normalizada (NDVI) entre 0,1 e 0,4 e compararam duas composições multitemporais: o percentil 50 (P50), equivalente à mediana, e o percentil 90 (P90), que busca o solo mais seco. Além das bandas e de índices espectrais, foram usadas variáveis climáticas e topográficas de outras fontes.

O TabPFN foi comparado a uma CNN e ao XGBoost em 100 iterações de _bootstrap_, com validação nas amostras não sorteadas, utilizando o R² e a raiz do erro quadrático médio (RMSE). Com a composição P50, o TabPFN obteve R² médio de 0,78 e RMSE de 1,90 g/kg, superior à CNN (R² de 0,74) e ao XGBoost (R² de 0,72). Com a composição P90, todos os modelos tiveram desempenho um pouco menor.

Os autores reconhecem que a extensão da área e o número de amostras limitam a transferência do modelo para outras regiões e que o NDVI não separa o solo exposto dos resíduos de culturas. A avaliação reamostrou amostras de uma mesma região, sem teste em uma região externa.

O estudo se relaciona com este TCC por aplicar o TabPFN a dados espectrais do Sentinel-2 com poucas amostras e por controlar a condição da superfície observada, o que reforça a necessidade de considerar a cobertura vegetal na seleção das áreas e das amostras deste trabalho. A diferença está no alvo e nos dados: o carbono orgânico é uma propriedade do solo, e não um teor de elemento ou óxido, e os autores combinam os dados espectrais com variáveis climáticas e topográficas. Este trabalho se propõe a avaliar o desempenho do TabPFN na classificação litológica e na predição da composição química a partir de dados espectrais de satélite, integrando e harmonizando bases de diferentes regiões e avaliando o desempenho em regiões reservadas para teste.
```

**Sigla RMSE (E04):** esta proposta apresenta a sigla como “raiz do erro quadrático médio (RMSE)”, porque a 3.5 vem antes da 3.6 no capítulo. Hoje a sigla é apresentada na 3.6 (Barkov), já incorporada a `tcc/markdown/` e ao LaTeX. Ao incorporar a 3.5, trocar na 3.6 “a raiz do erro quadrático médio (RMSE)” por “o RMSE” no `fundamentacao-teorica.md` da pasta 06, em `tcc/markdown/03-trabalhos-relacionados.md` e em `tcc/latex/capitulos/03-trabalhos-relacionados.tex`. Antes disso, a troca deixaria a sigla sem apresentação no capítulo. Na mesma ocasião, se a 3.3 (Kutzke) já estiver incorporada, trocar também “redes neurais convolucionais” por “CNN” na 3.6, pois a sigla é apresentada na 3.3.

### Anotações do autor

Espaço reservado às suas notas de leitura e ao seu rascunho.
