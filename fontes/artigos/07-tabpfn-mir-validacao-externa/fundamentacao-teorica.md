# Leitura orientada — Huang et al.

**Situação:** leitura e redação pelo autor pendentes.

## Roteiro de leitura — sugestões da IA

**Organização deste arquivo:** mantenha o roteiro, as observações sobre a revisão e as propostas da IA, quando solicitadas, antes de “Anotações do autor”. Essa última seção fica no fim do arquivo para permitir a continuidade da escrita sem interrupções. A proposta da IA é cumulativa: preserve os trechos aprovados e atualize-a até a conclusão indicada pelo autor; ao final, deixe apenas o subtópico numerado, seu título e o texto consolidado, sem o rótulo de versão da IA, crases, anotações do autor ou seções de apoio, após conferir a incorporação do conteúdo aprovado e de suas fontes.

**Foco:** Validação externa, incerteza e interpretação; fecha o capítulo no bloco de harmonização e generalização.

**Artigo para consulta:** [Zero-shot inference with Tabular Prior-data Fitted Network (TabPFN) for soil MIR spectral analysis](https://www.sciencedirect.com/science/article/pii/S0016706126002089).

Este roteiro orienta a leitura e as anotações. A redação da fundamentação teórica e da análise acadêmica será feita pelo autor; os itens abaixo não constituem texto pronto para o TCC.

### Roteiro na ordem de escrita do guia

Os tópicos seguem a estrutura de `templates/guia-trabalhos-relacionados.md` (seções 1.1 e 1.2): problema e objetivo, dados, método e avaliação, resultados e limitações e relação com este TCC. Cada etapa indica onde procurar no artigo e o que registrar; as etapas 1 a 4 correspondem aos parágrafos de apresentação, dados e método e resultados, e a etapa 5, ao parágrafo de comparação.

**Ênfase do guia (seção 1.3):** artigo sobre TabPFN (1.3.2), com espectros MIR de laboratório, não de satélite: tarefa, tamanho e características dos conjuntos, modelos comparados, validação e resultados.

**Posição no capítulo 3 (seção 3.7):** bloco de harmonização e generalização, que termina aqui e encerra o capítulo. Antes: Barkov et al. (3.6), TabPFN em bibliotecas espectrais de diferentes escalas e instrumentos com partições aleatórias. Depois: capítulo 4 (metodologia).

#### 1. Problema e objetivo

- [ ] **1. Introduction:** qual dúvida sobre a generalização do TabPFN em bibliotecas espectrais de tamanhos variados o estudo investiga?

#### 2. Dados utilizados

- [ ] **2.1. Dataset:** quais propriedades (carbono total, pH e fósforo por Olsen), coleções e grupos de treinamento e teste são usados?
- [ ] Qual coleção é o teste interno (Texas, 620 amostras) e qual fica inteira fora do treinamento (leste da Austrália, 387)?

#### 3. Método e avaliação

- [ ] **2.2. TabPFN:** o que é pré-treinado e como funciona a inferência em contexto?
- [ ] **2.3. Baselines and model evaluation:** quais comparadores são usados (PLSR, Cubist e CNN), como variam o tamanho e a semelhança espectral do treinamento e como as métricas são calculadas?
- [ ] **2.4. Uncertainty quantification; 2.5. SHAP:** como são obtidos intervalos e explicações, e o que cada instrumento pode avaliar?

#### 4. Resultados e limitações

- [ ] **3.1. Model performance; tabela 2:** como tamanho e semelhança espectral se relacionam com os resultados internos?
- [ ] **3.2. External validation; tabela 3; figuras 2 a 4:** como o desempenho é medido na coleção externa?
- [ ] **3.3; 3.4:** boa cobertura dos intervalos equivale a baixo erro preditivo?
- [ ] **3.5; 4. Conclusions; Appendix A:** quais limites de cobertura, interpretação e transferência os autores reconhecem?

#### 5. Relação com este TCC

- [ ] **O passo além de Barkov:** Barkov avalia escalas e instrumentos com partições aleatórias; Huang deixa uma coleção inteira fora do treinamento. O que torna esse teste externo e quais controles equivalentes o TCC precisaria documentar?
- [ ] **Pendências dos blocos anteriores:** zonas de exclusão na mesma área (Yang), transferência sem medidas independentes (Kutzke) e bootstrap local (Chen). Huang é o único dos sete estudos com desempenho medido em uma região externa.
- [ ] **Tamanho e semelhança do treinamento:** relacione com a hipótese do TCC de que integrar regiões pode ajudar, sem pressupor que sempre ajuda (D06, D07).
- [ ] **Incerteza:** como os intervalos poderiam apoiar o objetivo de priorizar áreas para investigação física?
- [ ] **Limite de transferência:** que diferenças entre MIR de laboratório e reflectância Sentinel-2 impedem transportar os resultados diretamente?
- [ ] **Fechamento do capítulo:** identifique a combinação que nenhum dos sete estudos cobre (TabPFN, dados espectrais de satélite, litologia e composição química e teste entre regiões), sem afirmar originalidade absoluta, já que a busca foi dirigida.
- [ ] Use o modelo de comparação da seção 1.4 do guia, sem antecipar resultados.

### Conceitos para você estudar antes de escrever o capítulo 2

- [ ] Inferência em contexto e diferenças entre ajuste e inferência.
- [ ] Diferença de distribuição, teste interno e validação externa.
- [ ] Intervalos preditivos, cobertura e interpretação por SHAP.

### Antes de redigir

- [ ] Anotar as páginas, seções, tabelas ou figuras que sustentam cada informação que você pretende usar.
- [ ] Separar o que os autores propõem, executam e demonstram; registrar também os limites da avaliação.
- [ ] Identificar conceitos que exigem consultar as referências originais, preservando suas URLs completas.
- [ ] Redigir com suas palavras, citando as fontes; discutir como o estudo se aproxima e se diferencia das tarefas do seu TCC.

### Anotações do autor

Espaço reservado às suas notas de leitura e ao seu rascunho.
