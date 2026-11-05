# Leitura orientada — Huang et al.

**Situação:** proposta de texto da IA redigida; revisão pelo autor pendente.

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

### Proposta de texto — versão da IA

Texto redigido integralmente pela IA a pedido do autor em 4 de novembro de 2026, a partir do `artigo.md`. Números, autoria e data conferidos pela IA na página original com o MCP do Playwright em 4 de novembro de 2026; falta a revisão de redação pelo autor.

```markdown
## 3.7 TabPFN em espectros MIR de solo com validação externa

[Huang et al. (2026)](https://www.sciencedirect.com/science/article/pii/S0016706126002089) investigaram se o TabPFN pode ser utilizado como ferramenta genérica de predição em bibliotecas espectrais de solo de diferentes tamanhos. Os autores utilizaram espectros MIR de 11.564 amostras dos Estados Unidos para prever carbono total, pH e fósforo extraível pelo método Olsen, propriedades de previsibilidade alta, média e baixa a partir desses espectros. As 620 amostras do Texas formaram o teste interno, e 387 amostras do leste da Austrália, medidas em outro laboratório, foram utilizadas como teste externo, apenas para o carbono total.

O TabPFN foi aplicado com as configurações padrão, recebendo os exemplos de treinamento como contexto, sem alteração dos parâmetros do modelo pré-treinado. Os autores o compararam com PLSR, Cubist e CNN, utilizando sete conjuntos de treinamento, de 46 a 10.944 amostras, definidos pelo tamanho e pela semelhança espectral com o Texas, observada por PCA. O desempenho foi medido principalmente pelo R² e pelo RMSE, e os intervalos de predição do TabPFN também foram avaliados.

Na predição do carbono total, o TabPFN reduziu o RMSE, em média, em 74% em relação ao PLSR e em 39% em relação ao Cubist. Com o conjunto da Flórida, de tamanho médio e espectralmente distinto do Texas, obteve R² de 0,92 no teste interno, contra 0,35 do Cubist. Na validação externa, com o maior conjunto de treinamento, alcançou R² de 0,97, contra 0,91 do Cubist e 0,92 da CNN; com os conjuntos pequenos, porém, o Cubist foi superior. Nenhum modelo previu adequadamente o fósforo. Os autores reconhecem que os espectros australianos eram semelhantes aos norte-americanos, exigindo uma generalização apenas moderada, e que o pré-treinamento não dispensa dados de treinamento representativos.

O estudo se relaciona com este TCC por avaliar o TabPFN em dados espectrais e medir o desempenho em uma região que não participou do treinamento, o que não ocorre nas partições aleatórias de Barkov et al. (2026). A diferença está nos dados e nas tarefas: os autores utilizaram espectros MIR medidos em laboratório para prever propriedades do solo, enquanto este trabalho se propõe a avaliar o desempenho do TabPFN na classificação litológica e na predição da composição química a partir de dados espectrais de satélite. Por isso, os resultados não demonstram a transferência do modelo para essas tarefas. Como este trabalho também se propõe a integrar e harmonizar bases de diferentes regiões, a influência do tamanho e da semelhança espectral observada pelos autores reforça a necessidade de avaliar o possível ganho de generalização em regiões reservadas para teste.
```

### Anotações do autor

Espaço reservado às suas notas de leitura e ao seu rascunho.
