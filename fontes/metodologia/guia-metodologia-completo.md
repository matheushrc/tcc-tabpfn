# 4 METODOLOGIA

> **Guia completo de escrita (IA), não é texto do TCC. Versão enxuta para o TCC I: `fontes/metodologia/guia-metodologia-simples.md`.** O guia indica o que o capítulo precisa conter, as decisões que cabem ao autor e onde encontrar o material de apoio. Substitua cada bloco pelo seu texto à medida que as decisões forem tomadas. Decisões citadas: `docs/decisoes-projeto.md`. Regras editoriais: `ABNT.md`.

## Como o Natanael estruturou a metodologia

O capítulo 4 de [Natanael](../../templates/natanael/markdown/04-metodologia.md) é curto e tem duas partes:

1. Um parágrafo de abertura que explica de onde o trabalho partiu (a revisão da literatura) e anuncia as etapas.
2. Uma lista de cinco fases. Cada fase tem um nome no infinitivo ("Analisar...", "Criar...", "Testar...") e de uma a duas frases sobre o que é feito e com que finalidade.

O que vale reaproveitar:

- a abertura que liga a metodologia à revisão bibliográfica;
- as fases em ordem cronológica, cada uma com uma finalidade explícita;
- o tempo verbal de proposta ("deve-se", "faz-se"), adequado a um TCC I em que nada foi executado.

O que não vale copiar:

- o nível de detalhe. A metodologia do Natanael não declara dados, métricas nem critérios de validação, porque o trabalho dele era uma ferramenta. Este trabalho é experimental, então precisa dizer com que dados, comparado a quê, medido como e validado como;
- os marcadores "•". O ABNT.md (N03) exige alíneas "a)", "b)", com o texto anterior terminando em ":", cada item em minúscula e terminando em ";", e o último em ".";
- o formato "Fase N:". Em vez dele, use seções 4.1, 4.2… (N02) quando uma fase precisar de mais de um parágrafo, e uma lista de alíneas no parágrafo de abertura para anunciar as fases.

## Estrutura sugerida

Proposta da IA. Ajuste a ordem e os nomes como preferir.

### Abertura do capítulo (sem número de seção)

**Escreva:** um parágrafo que retome o objetivo geral (1.4.1) e diga que a revisão (cap. 2) e os trabalhos relacionados (cap. 3) orientaram as escolhas. Termine com ":" e anuncie as etapas em alíneas, uma por seção abaixo.

### 4.1 Obtenção e inspeção dos dados

**Escreva:**

- quais bases serão usadas: as mundiais (D02) e as brasileiras do coorientador (D03);
- o que cada base fornece: rótulos litológicos, teores químicos ou ambos;
- a procedência dos rótulos: campo ou laboratório vs mapa derivado de imagem (ver "Distinções");
- para a química: o meio amostrado (rocha, solo ou sedimento), a digestão, o método analítico, as unidades e o suporte (pontual ou de bacia).

**Você precisa decidir ou levantar (pendências 1 e 2):**

- [ ] Quais bases entram de fato. Hoje não há tabela química georreferenciada no dataset de MG (`docs/lacunas-dataset-mg.md`).
- [ ] Quais elementos ou óxidos serão alvos (D09: a maior abrangência viável; terras raras como recorte de reserva).
- [ ] Os critérios de exclusão de amostras (profundidade, material transportado, áreas mineradas).

**Apoio:** `docs/analise-dataset-mg.md`, `docs/datasets-suporte-espacial.md`, `docs/fonte-sgb-geoquimica.md`.

### 4.2 Aquisição e pré-processamento das imagens Sentinel-2

**Escreva:**

- o nível de processamento: 2A (reflectância de superfície), citando a seção 2.2;
- as bandas usadas e a reamostragem para uma resolução comum (10 m e 20 m; SWIR em 20 m);
- o critério de datas em relação às amostras;
- os filtros de qualidade: nuvens (máscara de cena) e vegetação (limiar de NDVI; Grebby 2011 indica que acima de ~10% de cobertura vegetal o espectro da rocha é mascarado);
- os índices ou razões de bandas, se forem usados (van der Meer 2014).

**Você precisa decidir (pendência 3):**

- [ ] A fonte das imagens (Copernicus Browser, Google Earth Engine, Microsoft Planetary Computer…) e o período.
- [ ] Se haverá composição temporal (mediana de várias datas) ou uma única cena.
- [ ] O limiar de vegetação e de nuvens.
- [ ] Os atributos extras além das bandas (índices, razões).

### 4.3 Integração espacial e construção dos conjuntos tabulares

**Escreva:**

- como ponto ou polígono vira linha da tabela: pixel único, média de uma janela 3×3 ou estatística por polígono (D05);
- como os rótulos de mapa serão amostrados, se forem usados, e por que isso não é validação independente;
- a harmonização entre bases: unidades, nomes de classes litológicas (tabela de correspondência) e valores abaixo do limite de detecção;
- o tamanho final de cada conjunto: linhas, atributos, classes e alvos.

**Você precisa decidir:**

- [ ] A janela de extração e a regra para pixels mistos.
- [ ] O esquema de classes litológicas comum entre regiões.
- [ ] O tratamento de valores abaixo do limite de detecção.
- [ ] Pendência 6: tratar a natureza composicional dos óxidos (log-razões como CLR ou ILR) ou apenas discuti-la como limitação. Faltam fontes; a IA pode pesquisá-las se você pedir.

### 4.4 Modelos

**Escreva:**

- TabPFN-3.5, com a versão exata (D20): pacote `tabpfn` 9.2.0, pesos `tabpfn-v3.5-20260909`;
- `TabPFNClassifier` para a litologia e `TabPFNRegressor` para a química, com um modelo por elemento ou óxido, porque o regressor aceita uma única variável resposta;
- os dados de treino entram como contexto, sem reajuste de pesos (ver "Distinções"; ajuste fino só por decisão explícita);
- os limites do modelo e o hardware (GPU do servidor da universidade);
- os modelos de comparação e seus hiperparâmetros.

**Você precisa decidir (pendência 4):**

- [ ] Os modelos de comparação. A revisão já fundamenta _Random Forest_ (Breiman 2001) e XGBoost (Chen e Guestrin 2016), e Grinsztajn et al. (2022) justificam árvores como linha de base forte. Lembre que D10 reserva CNN e modelos básicos aos colegas.
- [ ] Como ajustar os hiperparâmetros das linhas de base (padrão vs busca), sempre sem usar o conjunto de teste.
- [ ] Se compara o TabPFN-3.5-Fast (sugestão da IA, não decidido).
- [ ] Confirmar a GPU do servidor.

### 4.5 Protocolo de validação

**Escreva:**

- a validação cruzada espacial por blocos ou regiões (Roberts et al. 2017), justificada por Tobler (1970) e por Ploton et al. (2020): R² de 0,53 na divisão aleatória contra 0,14 na espacial;
- o teste em região externa, definida antes de qualquer ajuste (D07);
- o experimento de D06: treino com uma região vs com várias, testado na **mesma** região externa e com os demais controles iguais;
- a área de aplicabilidade (Meyer e Pebesma 2021), se for usada;
- como impedir vazamento: normalização e seleção de atributos ajustadas só no treino; amostras vizinhas no mesmo grupo.

**Você precisa decidir:**

- [ ] O tamanho dos blocos (ou "uma região = um grupo") e o número de dobras.
- [ ] Qual região será a externa.
- [ ] Se a área de aplicabilidade entra no escopo.

### 4.6 Métricas de avaliação

**Escreva:**

- classificação:
  - a matriz de confusão;
  - a acurácia global e as métricas por classe;
  - o F1 macro com a fórmula declarada (D19):

    $$F1_{macro} = \frac{1}{K}\sum_{k=1}^{K} \frac{2\,P_k R_k}{P_k + R_k}$$

  - a justificativa para não usar kappa (Foody 2020);
- regressão: RMSE, MAE e R², avisando que o R² pode ser negativo (Chicco et al. 2021). Reporte por alvo e por região;
- como as comparações serão feitas: média e desvio entre dobras, e se haverá teste estatístico.

**Você precisa decidir:**

- [ ] Se usa um teste de significância entre modelos ou apenas a comparação descritiva.
- [ ] Se reporta a incerteza (o TabPFN fornece quantis no regressor).

### 4.7 Disponibilização dos dados (opcional nesta versão)

**Escreva:** o que será publicado no Kaggle, a documentação que acompanha e o que fica de fora por licença (D08).

**Você precisa levantar (pendência 5):** a licença de redistribuição de cada fonte.

### 4.8 Ferramentas e reprodutibilidade

**Escreva:**

- a linguagem e as bibliotecas com versão (Python, `tabpfn`, scikit-learn, xgboost, rasterio ou Earth Engine);
- o controle de sementes;
- o repositório do código.

## Lembretes de redação

- Use tempo de proposta ("serão utilizados", "pretende-se"). Nada foi executado ainda (AGENTS.md: proposto ≠ executado).
- Não introduza siglas já definidas (E04): TabPFN, XGBoost, RMSE, MAE, R², MSI, ESA, CNN. Defina na primeira ocorrência as novas, como NDVI, CLR e GPU.
- Aplique itálico aos termos em inglês (E11), inclusive _Random Forest_ e _in-context learning_.
- Cite no formato do Markdown, "[Autor (ano)](URL)", reaproveitando as fontes do capítulo 2. Fontes novas precisam de entrada no `bibliografia.bib` quando forem para o LaTeX.
- Uma figura com o fluxo das etapas (dados → Sentinel-2 → integração → modelos → validação) ajuda muito e é comum em metodologias experimentais.
