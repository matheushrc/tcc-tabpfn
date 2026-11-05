# Leitura orientada — Yang, Huang e Lu

**Situação:** leitura e redação pelo autor pendentes.

## Roteiro de leitura — sugestões da IA

**Organização deste arquivo:** mantenha o roteiro, as observações sobre a revisão e as propostas da IA, quando solicitadas, antes de “Anotações do autor”. Essa última seção fica no fim do arquivo para permitir a continuidade da escrita sem interrupções. A proposta da IA é cumulativa: preserve os trechos aprovados e atualize-a até a conclusão indicada pelo autor; ao final, deixe apenas o subtópico numerado, seu título e o texto consolidado, sem o rótulo de versão da IA, crases, anotações do autor ou seções de apoio, após conferir a incorporação do conteúdo aprovado e de suas fontes.

**Foco:** Classificação com TabPFN e atributos Sentinel-2 por pixel; segunda seção do bloco de classificação litológica.

**Artigo para consulta:** [Mapping of Crop Planting Structures Under Limited Training Samples Using TabPFN and Sentinel-2 Time Series Data](https://www.mdpi.com/2072-4292/18/11/1857).

Este roteiro orienta a leitura e as anotações. A redação da fundamentação teórica e da análise acadêmica será feita pelo autor; os itens abaixo não constituem texto pronto para o TCC.

### Roteiro na ordem de escrita do guia

Os tópicos seguem a estrutura de `templates/guia-trabalhos-relacionados.md` (seções 1.1 e 1.2): problema e objetivo, dados, método e avaliação, resultados e limitações e relação com este TCC. Cada etapa indica onde procurar no artigo e o que registrar; as etapas 1 a 4 correspondem aos parágrafos de apresentação, dados e método e resultados, e a etapa 5, ao parágrafo de comparação.

**Ênfase do guia (seção 1.3):** artigo sobre TabPFN (1.3.2), com dados de satélite (1.3.1): tarefa, tamanho e características do conjunto, modelos comparados, validação, tratamento da distribuição espacial das amostras e resultados.

**Posição no capítulo 3 (seção 3.2):** bloco de classificação litológica. Antes: Costa et al. (3.1), mapeamento litológico com Random Forest em Carajás. Depois: Kutzke et al. (3.3), que abre o bloco de composição química.

#### 1. Problema e objetivo

- [ ] **1. Introduction; 2.1. Study Area:** qual é o problema (mapear culturas em terreno montanhoso, com campos fragmentados, nuvens e poucas amostras) e qual é o objetivo do estudo?
- [ ] Por que a escassez de amostras de treinamento é tratada como limitação central?

#### 2. Dados utilizados

- [ ] **2.2. Sentinel-2 Data; 2.5. Construction of the Multidimensional Classification Feature Set:** quais bandas, datas, índices de vegetação, texturas e coordenadas formam a tabela, e como cada pixel vira uma linha (68 atributos antes da seleção)?
- [ ] **2.3. Sample Data:** quais são as classes, quantas amostras há no treinamento (1.999) e na validação (858) e de onde vêm os rótulos (campo, VANT, imagens de alta resolução e correspondência fenológica por EVI)?
- [ ] **Ligação com Costa:** Costa usa um mapa geológico como referência; aqui os rótulos têm origens diversas. Anote essa diferença à luz da distinção do TCC entre rótulos independentes e mapas derivados.

#### 3. Método e avaliação

- [ ] **2.6. Feature Space Optimization Based on RFE; 2.7. Crop Classification Model Construction:** como a eliminação recursiva reduz os atributos para 44 e como o TabPFN e os modelos de comparação (RF, XGBoost e CatBoost) são configurados?
- [ ] **2.8. Accuracy Assessment Metrics:** o que medem a acurácia global, o kappa e o F1 macro?
- [ ] **2.9–2.11:** como funcionam a validação sem as amostras de EVI, a remoção das coordenadas e as zonas de exclusão de 50, 100 e 300 m?
- [ ] **Ligação com Costa:** Costa escolheu o Random Forest entre cinco algoritmos; anote como o Yang compara o TabPFN com o Random Forest e outros dois modelos na mesma tabela.

#### 4. Resultados e limitações

- [ ] **3.3; 3.7; tabelas 13 e 14:** desempenho de cada modelo com todos os atributos e com os 44 selecionados.
- [ ] **3.8; figura 7; tabela 15:** diferença entre os modelos com 10%, 20% e 30% do treinamento.
- [ ] **3.4–3.6; tabelas 11 e 12:** o que mudam a validação sem EVI, as zonas de exclusão e a retirada das coordenadas?
- [ ] **4.3–4.5; 5. Conclusions:** quais limitações os autores reconhecem (coordenadas podem reduzir a transferência; outros anos, regiões e sistemas ainda não testados)? Separe essas limitações das suas observações.

#### 5. Relação com este TCC

- [ ] **Coordenadas:** Costa compara mapas com e sem coordenadas; Yang mede a queda ao retirá-las. O que os dois indicam sobre o risco de o modelo reconhecer o lugar em vez do material?
- [ ] **Superfície observada:** Costa descartou o Landsat-8 pela vegetação; para Yang a vegetação é o próprio alvo. Por que isso torna a litologia por satélite mais difícil que a classificação de culturas?
- [ ] **Validação espacial:** zonas de exclusão dentro da mesma área equivalem a testar em uma região não usada no ajuste? Guarde a observação para o bloco de generalização (Barkov e Huang).
- [ ] **Fechamento do bloco:** o que Costa e Yang, juntos, indicam para o protocolo de classificação do TCC (modelo de comparação, coordenadas, tamanho do treinamento)?
- [ ] Quais procedimentos (tabela por pixel, comparação com modelos convencionais, redução do treinamento) podem orientar a classificação litológica do TCC, e por que culturas agrícolas diferem de litologias como alvo?
- [ ] Use o modelo de comparação da seção 1.4 do guia, sem antecipar resultados.

### Conceitos para você estudar antes de escrever o capítulo 2

- [ ] Séries temporais Sentinel-2, índices de vegetação e atributos de textura.
- [ ] Seleção de atributos por eliminação recursiva (RFE).
- [ ] Classificação com TabPFN, acurácia global, kappa e F1 macro.
- [ ] Autocorrelação espacial, zonas de exclusão (*buffers*) e uso de coordenadas como atributos.

### Antes de redigir

- [ ] Anotar as páginas, seções, tabelas ou figuras que sustentam cada informação que você pretende usar.
- [ ] Separar o que os autores propõem, executam e demonstram; registrar também os limites da avaliação.
- [ ] Identificar conceitos que exigem consultar as referências originais, preservando suas URLs completas.
- [ ] Redigir com suas palavras, citando as fontes; discutir como o estudo se aproxima e se diferencia das tarefas do seu TCC.

### Anotações do autor

Espaço reservado às suas notas de leitura e ao seu rascunho.
