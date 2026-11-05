# Leitura orientada — Kutzke, Eichstaedt e Kahnt

**Situação:** leitura e redação pelo autor pendentes.

## Roteiro de leitura — sugestões da IA

**Organização deste arquivo:** mantenha o roteiro, as observações sobre a revisão e as propostas da IA, quando solicitadas, antes de “Anotações do autor”. Essa última seção fica no fim do arquivo para permitir a continuidade da escrita sem interrupções. A proposta da IA é cumulativa: preserve os trechos aprovados e atualize-a até a conclusão indicada pelo autor; ao final, deixe apenas o subtópico numerado, seu título e o texto consolidado, sem o rótulo de versão da IA, crases, anotações do autor ou seções de apoio, após conferir a incorporação do conteúdo aprovado e de suas fontes.

**Foco:** Vários alvos geoquímicos a partir de espectros; abre o bloco de composição química.

**Artigo para consulta:** [Potential of hyperspectral-based geochemical predictions with neural networks for strategic and regional exploration improvement](https://doi.org/10.1080/08120099.2022.2094465).

Este roteiro orienta a leitura e as anotações. A redação da fundamentação teórica e da análise acadêmica será feita pelo autor; os itens abaixo não constituem texto pronto para o TCC.

### Roteiro na ordem de escrita do guia

Os tópicos seguem a estrutura de `templates/guia-trabalhos-relacionados.md` (seções 1.1 e 1.2): problema e objetivo, dados, método e avaliação, resultados e limitações e relação com este TCC. Cada etapa indica onde procurar no artigo e o que registrar; as etapas 1 a 4 correspondem aos parágrafos de apresentação, dados e método e resultados, e a etapa 5, ao parágrafo de comparação.

**Ênfase do guia (seção 1.3):** artigo de sensoriamento remoto (1.3.1), com espectros hiperespectrais de testemunhos, não de satélite: sensores e variáveis, dados de referência e procedimento de validação.

**Posição no capítulo 3 (seção 3.3):** bloco de composição química, que começa aqui. Antes: Yang et al. (3.2), que fecha o bloco de classificação. Depois: Zhang et al. (3.4), que leva a predição geoquímica a dados de satélite.

#### 1. Problema e objetivo

- [ ] **Introduction; Motivation; Literature review and theoretical background:** qual é a motivação e que relação entre espectros e geoquímica é investigada?

#### 2. Dados utilizados

- [ ] **Geological context and data; Material:** de onde vêm os testemunhos (mais de 700 km, em intervalos de 1 m) e as análises, e como sua qualidade e compatibilidade são verificadas?
- [ ] Quais elementos são alvos (Au, Ag, Cu, Fe, U, Ni, Pb, Sn, Sb, As e Bi)?
- [ ] **Mineral como atributo, química como alvo:** as abundâncias minerais derivadas dos espectros entram como atributos e as análises químicas como rótulos. Registre essa separação, coerente com D01.

#### 3. Método e avaliação

- [ ] **Methodology; tabela 1:** como os teores são convertidos em classes por limiares econômicos, como os dados são divididos (60/20/20) e o que as métricas representam?
- [ ] Que tipo de alvo cada elemento gera: teor contínuo ou classe definida por limiar? Anote como essa conversão liga a classificação à composição química e o que se perde em relação a prever o teor.

#### 4. Resultados e limitações

- [ ] **Dependency of results based on the amount of data for learning:** como a quantidade de amostras se relaciona com os resultados?
- [ ] Quais elementos tiveram melhor e pior resultado? A viabilidade pode variar por elemento também no TCC.
- [ ] **Influence of knowledge of geological domains on predictions; tabelas 2 a 4:** quais comparações entre crátons usam medidas reais e quais comparam previsões de modelos?
- [ ] **Potential for resource estimation in Australia; tabela 5; Discussion; Conclusions:** como separar potencial de investigação de confirmação geológica ou estimativa de recursos?

#### 5. Relação com este TCC

- [ ] **Transição da classificação para a composição:** como a conversão de teores em classes conecta este estudo ao bloco anterior (Costa e Yang)?
- [ ] **Domínios geológicos:** a influência do conhecimento dos domínios retoma o contexto geológico usado por Costa.
- [ ] **Do testemunho ao satélite:** quais diferenças entre espectros hiperespectrais de testemunhos (subsuperfície) e reflectância Sentinel-2 da superfície limitam o uso desta evidência? Use-as para preparar a passagem a Zhang.
- [ ] **Transferência entre crátons:** a comparação entre previsões permite calcular acurácia externa contra medidas independentes? Guarde para o bloco de generalização (Huang).
- [ ] Use o modelo de comparação da seção 1.4 do guia, sem antecipar resultados.

### Conceitos para você estudar antes de escrever o capítulo 2

- [ ] Espectroscopia hiperespectral de testemunhos e referência geoquímica.
- [ ] Teores contínuos, limiares de teor e classes de classificação.
- [ ] Domínio geológico, transferência e referência externa independente.

### Antes de redigir

- [ ] Anotar as páginas, seções, tabelas ou figuras que sustentam cada informação que você pretende usar.
- [ ] Separar o que os autores propõem, executam e demonstram; registrar também os limites da avaliação.
- [ ] Identificar conceitos que exigem consultar as referências originais, preservando suas URLs completas.
- [ ] Redigir com suas palavras, citando as fontes; discutir como o estudo se aproxima e se diferencia das tarefas do seu TCC.

### Anotações do autor

Espaço reservado às suas notas de leitura e ao seu rascunho.
