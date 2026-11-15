# Guia simples da metodologia (TCC I)

> **Guia de escrita preparado pela IA, não é texto do TCC.** Esta é a versão enxuta para o pré-projeto. Ela fecha só o que já está decidido e deixa o resto aberto, mas com o critério de escolha escrito. A versão detalhada está em `fontes/metodologia/guia-metodologia-completo.md`. As decisões citadas estão em `docs/decisoes-projeto.md`.

## Regra geral

No TCC I, a metodologia é um plano. Tudo o que depende de inspecionar os dados pode ficar em aberto, desde que o texto diga **como** será decidido. Por exemplo:

- "o limiar de vegetação será definido a partir da distribuição de NDVI nas áreas selecionadas";
- "serão mantidos os alvos com número suficiente de amostras em ao menos duas regiões".

Evite "a definir" sem critério.

Siga o modelo do [Natanael](../../templates/natanael/markdown/04-metodologia.md): um parágrafo de abertura e depois as etapas. Use alíneas "a)" (N03) ou seções curtas, e o tempo de proposta ("serão", "pretende-se").

## Abertura

Escreva um parágrafo que retome o objetivo geral (1.4.1), diga que os capítulos 2 e 3 orientaram as escolhas e anuncie as etapas.

## Etapas

### 1. Seleção e inspeção dos dados

**Já definido:**

- bases mundiais (D02) e bases brasileiras do coorientador (D03);
- rótulos litológicos e teores químicos de laboratório (não proporções minerais);
- preferência por referências independentes, e não por mapas derivados de imagem.

**Pode ficar aberto. O critério a escrever é:** entram as bases com coordenadas confiáveis, procedência documentada e método analítico conhecido. Os alvos químicos serão escolhidos pela cobertura de amostras (D09).

### 2. Imagens Sentinel-2

**Já definido:** Sentinel-2 de nível 2A (reflectância de superfície), nas mesmas áreas das amostras (D04).

**Pode ficar aberto. O critério a escrever é:** as datas, as bandas, os filtros de nuvem e vegetação e eventuais índices serão definidos conforme a cobertura das áreas, priorizando a superfície exposta (Grebby 2011).

### 3. Construção dos conjuntos tabulares

**Já definido:** cada amostra será associada aos valores de reflectância por integração espacial, e o procedimento será documentado (D05).

**Pode ficar aberto. O critério a escrever é:** a janela de extração, a harmonização de classes e unidades e o tratamento de valores abaixo do limite de detecção. Vale citar a natureza composicional dos óxidos como questão a avaliar.

### 4. Modelos

**Já definido:**

- TabPFN-3.5 (D20), com classificador para a litologia e regressor para cada elemento ou óxido;
- os exemplos de treino entram como contexto.

**Pode ficar aberto. O critério a escrever é:** a comparação será feita com linhas de base baseadas em árvores, como _Random Forest_ e XGBoost (cap. 2). Os hiperparâmetros serão ajustados sem usar o teste.

### 5. Validação e métricas

**Já definido:**

- validação cruzada espacial (Roberts et al. 2017);
- teste em região não usada no ajuste (D07);
- comparação entre uma e várias regiões de treino na mesma região externa (D06);
- métricas de classificação: acurácia, métricas por classe e F1 macro (D19);
- métricas de regressão: RMSE, MAE e R².

**Pode ficar aberto. O critério a escrever é:** o tamanho dos blocos e a região externa serão definidos conforme a distribuição espacial dos dados, antes de qualquer ajuste.

### 6. Disponibilização (opcional)

Escreva a intenção de publicar no Kaggle os derivados com redistribuição permitida (D08).

## Antes de entregar

Só um item precisa estar resolvido: confirmar com o orientador que esse nível de abertura é aceito no TCC I.
