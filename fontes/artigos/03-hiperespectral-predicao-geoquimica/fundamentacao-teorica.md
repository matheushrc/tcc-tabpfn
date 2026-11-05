# Leitura orientada — Kutzke, Eichstaedt e Kahnt

**Situação:** proposta de texto da IA redigida; revisão pelo autor pendente.

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

### Proposta de texto — versão da IA

Texto redigido integralmente pela IA a pedido do autor em 4 de novembro de 2026, a partir do `artigo.md`. Números, autoria e data conferidos pela IA na página original com o MCP do Playwright em 4 de novembro de 2026; falta a revisão de redação pelo autor.

```markdown
## 3.3 Predição geoquímica a partir de testemunhos de sondagem

[Kutzke, Eichstaedt e Kahnt (2022)](https://doi.org/10.1080/08120099.2022.2094465) avaliaram o uso de uma rede neural convolucional (CNN) para prever teores de elementos químicos em testemunhos de sondagem a partir de espectros hiperespectrais medidos nesses testemunhos. A motivação é que as análises geoquímicas são caras e cobrem apenas trechos escolhidos pelos geólogos, enquanto o escaneamento hiperespectral cobre o testemunho inteiro.

Os autores utilizaram dados públicos da Austrália, reunidos pela AuScope National Virtual Core Library e pelos serviços geológicos estaduais. Os atributos de entrada foram as abundâncias minerais estimadas a partir dos espectros no infravermelho de ondas curtas e no infravermelho termal, em intervalos de 1 m, de mais de 2.700 furos. Os rótulos vieram de análises químicas de elementos como ouro, prata, cobre, ferro, urânio e níquel: dos cerca de 70 milhões de registros geoquímicos disponíveis, 110.000 foram associados a 703.250 intervalos de 1 m.

Os teores não foram previstos como valores contínuos. Para cada elemento, os autores definiram limiares a partir dos percentis superiores da base e converteram os teores em classes, com o mesmo número de amostras acima e abaixo do limiar. Os dados foram divididos aleatoriamente em 60% para treinamento, 20% para verificação e 20% para teste, e o desempenho foi medido pela acurácia no conjunto de teste. Na abordagem de duas classes, as acurácias variaram de 79,59% para o cobre a 94,90% para o bismuto, e com três classes a acurácia para o ouro caiu para cerca de 64%. Treinar o modelo separadamente por domínios geológicos não melhorou significativamente os resultados.

Os autores também treinaram o modelo com dados do Cráton Gawler e o aplicaram ao Cráton Yilgarn. Como essa aplicação foi feita sem registros geoquímicos do Yilgarn, as previsões foram comparadas com as de outro modelo, treinado com toda a Austrália, e não com análises independentes. As semelhanças acima de 90%, exceto para o ouro de menor teor, indicam concordância entre modelos, e não acurácia na nova região.

O estudo se relaciona com este TCC por prever a composição química a partir de dados espectrais e por discutir a transferência entre regiões geológicas. A diferença está nos dados: os autores utilizaram espectros medidos em testemunhos de subsuperfície, convertidos em abundâncias minerais, enquanto este trabalho se propõe a avaliar o desempenho do TabPFN na classificação litológica e na predição da composição química a partir de dados espectrais de satélite, que registram a superfície. O trabalho também se propõe a integrar e harmonizar bases de diferentes regiões e a avaliar os modelos em regiões reservadas para teste.
```

**Divergência na fonte:** o resumo e a seção *Material* citam estanho (Sn) entre os elementos extraídos, mas as tabelas 1 e 5 trazem zinco (Zn), com limiar de 68 ppm, e nenhuma linha de Sn. A divergência foi conferida no HTML original da Taylor & Francis em 4 de novembro de 2026 e é do próprio artigo, não da conversão. Por isso, a proposta não cita Sn nem Zn. Se o autor quiser mencionar um deles, deve citar o zinco pelos valores das tabelas e registrar que o texto do artigo cita o estanho.

**Terminologia (E09), pesquisada em 4 de novembro de 2026:**

- **Testemunho de sondagem (_drill core_):** termo técnico usual da geologia brasileira para o cilindro de rocha extraído na sondagem rotativa. Aparece no [resumo sobre a Litoteca de Caçapava do Sul do SGB](https://rigeo.sgb.gov.br/bitstream/doc/17106/1/ID8940_110204_52_resumoLitoteca_vieroetal.pdf), que também o usa como palavra-chave no [RIGeo](https://rigeo.sgb.gov.br/handle/doc/17106?locale=en); no [Plano Estratégico 2020–2024 do SGB](https://sgb.gov.br/documents/d/guest/plano_estrategico_2020_2024_jul22-pdf); em [notícia da UNIPAMPA sobre aula prática](https://desativados.unipampa.edu.br/volawsdados/cacapava2008-2017/noticias/355-alunos-do-do-curso-superior-de-tecnologia-em-mineracao-fazem-trabalho-pratico-em-acervo-da-cprm%3Fformat=pdf); e no [IGE-Unicamp](https://portal-dev.ige.unicamp.br/es/node/2180), em imageamento hiperespectral de testemunhos de poços. Equivale a “testigo de sondeo” em espanhol, segundo o [UBTERM](https://www.ub.edu/ubterm/?p=74072). “Núcleo” aparece mais em petróleo e em traduções informais. Tradução mantida.
- **Infravermelho de ondas curtas (SWIR):** usado em [Teixeira et al., INPE/SBSR 2017](https://dataserver-coids.inpe.br/queimadas/queimadas/Publicacoes-Impacto/material3os/2017_Teixeira_etal_AdaptacaoIndicesQueimadaSWIR_XVIIISBSR_DE3os.pdf), em [Pacheco e Almeida, USP/SBSR 2009](https://repositorio.usp.br/bitstreams/332a7ba5-c0f1-4388-97ca-45d32e16e4f1) e em [trabalho da UFC sobre Santa Quitéria](https://repositorio.ufc.br/handle/riufc/64532?mode=full), conferidos no texto. Tradução adotada.
- **Infravermelho termal (TIR):** usado em trabalhos de geociências da UFRGS, como [artigo no Boletim de Ciências Geodésicas](https://revistas.ufpr.br/bcg/article/view/46104) e [comparação de métodos com o ASTER no SBSR](https://proceedings.science/sbsr/papers/comparacao-de-metodos-de-recuperacao-de-emissividade-em-atmosferas-umidas-com-dados-do-infravermelho-termal-do-sensor-as). A variante “infravermelho térmico” aparece em páginas traduzidas do [Google Earth Engine](https://developers.google.com/earth-engine/datasets/catalog/NASA_ASTER_GED_AG100_003?hl=pt-br). As fontes divergem, e as ocorrências de “termal” vêm em parte do mesmo grupo de pesquisa; mantido “termal”, comum em geociências, sem apresentá-lo como consenso.

**Sigla CNN (E04):** esta proposta apresenta “rede neural convolucional (CNN)”, primeira ocorrência no capítulo; a 3.5 e a 3.7 usam só a sigla. Ao incorporar a 3.3, trocar na 3.6 (Barkov) “redes neurais convolucionais” por “CNN” no `fundamentacao-teorica.md` da pasta 06, em `tcc/markdown/03-trabalhos-relacionados.md` e em `tcc/latex/capitulos/03-trabalhos-relacionados.tex`.

### Anotações do autor

Espaço reservado às suas notas de leitura e ao seu rascunho.
