# Revisão bibliográfica — sete estudos prioritários

Atualizada em 4 de novembro de 2026; a seleção de 9 de outubro de 2026 reunia oito estudos (ver “Revisão da seleção em 4 de novembro de 2026”). Consolida a lista anterior e a pesquisa multilíngue de TabPFN. A seleção prioriza aderência e complementaridade com D01–D07: litologia, composição química, integração orbital, harmonização e generalização regional. Não implica implementar todos os métodos citados.

## Estudos selecionados

A ordem acompanha as pastas numeradas de `fontes/artigos/` e as subseções do capítulo 3, definidas em 4 de novembro de 2026: classificação litológica (1–2), composição química (3–5) e harmonização e generalização entre regiões (6–7), seguindo o título e o problema de pesquisa. Em cada bloco, os estudos vão do mais distante ao mais próximo da proposta. A numeração não indica que todas as análises já estejam redigidas; o estado de cada uma está em `fontes/README.md`.

### 1. Costa, Tavares e Oliveira (2019) — litologia no Brasil

[Predictive lithological mapping through machine learning methods: a case study in the Cinzento Lineament, Carajás Province, Brazil](https://jgsb.sgb.gov.br/index.php/journal/article/view/63). *Journal of the Geological Survey of Brazil*, 2(1), 26–36. DOI: 10.29396/jgsb.2019.v2.n1.3. BibTeX: `costa2019`.

Aplica Random Forest a dados remotos e geofísicos, comparando mapas litológicos com e sem coordenadas, com 1.400 amostras de treinamento. É o precedente brasileiro mais diretamente ligado à classificação proposta. Orienta a comparação com um modelo convencional e a análise da localização. **Limite:** não usa TabPFN nem prevê composição química. Coordenadas exigem avaliação que diferencie reconhecimento local de transferência para outra região.

### 2. Yang, Huang e Lu (2026) — classificação com TabPFN e Sentinel-2

[Mapping of Crop Planting Structures Under Limited Training Samples Using TabPFN and Sentinel-2 Time Series Data](https://www.mdpi.com/2072-4292/18/11/1857). *Remote Sensing*, 18(11), 1857; publicado em 5 de junho de 2026. DOI: 10.3390/rs18111857.

Classifica culturas agrícolas em 10 m com atributos de séries temporais Sentinel-2 (bandas, índices de vegetação, textura e coordenadas), selecionados por eliminação recursiva, e compara TabPFN com Random Forest, XGBoost e CatBoost na mesma divisão. Com 1.999 amostras de treinamento e 858 de validação, o TabPFN alcança acurácia global de 96,27% e F1 macro de 0,956; em subamostragens repetidas, mantém acurácia média de 90,60% com 30% do treinamento e 82,89% com 10%. A divisão principal 7:3 é aleatória estratificada, mas os autores acrescentam validação com zonas de exclusão de 50, 100 e 300 m em torno das amostras de treinamento (acurácia entre 0,958 e 0,962) e uma ablação das coordenadas, cuja remoção reduz a acurácia de 0,963 para 0,938. É o precedente mais próximo do protocolo de classificação proposto: atributos orbitais por pixel em formato tabular, comparação com modelos convencionais, robustez com poucas amostras e controle do uso de coordenadas, questão também presente em Costa. **Limite:** as classes são culturas, observadas sobretudo pela vegetação, e não litologias; não há teste em outra região ou ano, e os próprios autores indicam que as coordenadas podem reduzir a transferência e que a aplicabilidade a outros anos, regiões e sistemas ainda precisa ser testada.

### 3. Kutzke, Eichstaedt e Kahnt (2022) — diversos alvos geoquímicos

[Potential of hyperspectral-based geochemical predictions with neural networks for strategic and regional exploration improvement](https://doi.org/10.1080/08120099.2022.2094465). *Australian Journal of Earth Sciences*, 69(8), 1197–1206; publicado online em 13 de julho de 2022. DOI: 10.1080/08120099.2022.2094465. BibTeX: `kutzke2022`.

Relaciona atributos e abundâncias minerais derivados de varreduras hiperespectrais de testemunhos a referências geoquímicas, prevendo classes de teor definidas por limiares. Além da divisão aleatória 60/20/20, aplica um modelo treinado em Gawler ao cráton Yilgarn. **Limite:** essa transferência é comparada com previsões do modelo australiano geral, sem análises geoquímicas independentes de Yilgarn; semelhança entre previsões não equivale a acurácia externa. Não utiliza TabPFN ou satélite e não prevê proporções minerais. Sustenta investigar múltiplos alvos, sem garantir viabilidade para todos.

### 4. Zhang et al. (2023) — integração orbital e geoquímica

[Deriving big geochemical data from high-resolution remote sensing data via machine learning: Application to a tailing storage facility in the Witwatersrand goldfields](https://www.sciencedirect.com/science/article/pii/S2666544123000059). *Artificial Intelligence in Geosciences*, 4, 9–21. DOI: 10.1016/j.aiig.2023.01.005. BibTeX: `zhang2023`.

Relaciona atributos orbitais a um modelo geoestatístico derivado de análises de ouro em rejeitos. É uma ponte direta entre referências laboratoriais, localização e espectros para estimar teor. **Limite:** rejeitos de uma instalação não representam solos naturais mundiais nem proporções minerais. Interpolações não são novas análises independentes. Landsat-8 auxilia o alinhamento histórico e Sentinel-2 fornece os atributos preditivos; isso não estabelece superioridade geral sobre Landsat, especialmente Landsat-5.

### 5. Chen et al. (2026) — TabPFN com Sentinel-2

[Integrating transformer-based learning and Sentinel-2 bare soil composites for soil organic carbon mapping in the black soil region of Northeast China](https://www.nature.com/articles/s41598-025-33682-4). *Scientific Reports*, 16, 3784; publicado em 5 de janeiro de 2026. DOI: 10.1038/s41598-025-33682-4. BibTeX: `chen2026`.

Integra composições multitemporais de solo exposto e variáveis ambientais com 174 amostras. TabPFN com composição P50 apresenta R² de 0,78 e RMSE de 1,90 g/kg para carbono orgânico, superando CNN e XGBoost no estudo. Orienta extração orbital e controle da superfície. **Limite:** carbono orgânico do solo não equivale aos teores de elementos ou óxidos previstos neste TCC. A reamostragem local não substitui teste em regiões externas nem garante resultado para litologia ou terras raras.

### 6. Barkov et al. (2026) — bibliotecas harmonizadas

[From field-scale to large-scale spectral libraries: Tabular foundation models in soil spectroscopy](https://arxiv.org/html/2608.00608v1). Preprint arXiv:2608.00608v1, submetido em 1 de agosto de 2026. DOI: 10.48550/arXiv.2608.00608. BibTeX: `barkov2026`.

Compara modelos e representações espectrais em 85 tarefas de regressão com LimeSoDa e OSSL, incluindo TabPFN. Fundamenta diferentes escalas de dados e preparação dos atributos. **Limite:** usa espectros vis-NIR/MIR de amostras, não imagens orbitais; os alvos são propriedades do solo. Variabilidade entre instrumentos não demonstra benefício causal de misturar sensores. Partições aleatórias não respondem, por si, à hipótese de transferência entre regiões. Trata-se de preprint.

### 7. Huang et al. (2026) — teste externo

[Zero-shot inference with Tabular Prior-data Fitted Network (TabPFN) for soil MIR spectral analysis](https://www.sciencedirect.com/science/article/pii/S0016706126002089). *Geoderma*, 471, 117880; julho de 2026, publicado online em 29 de maio de 2026. DOI: 10.1016/j.geoderma.2026.117880. BibTeX: `huang2026`.

Compara TabPFN, PLSR, Cubist e CNN para carbono total, pH e fósforo extraível por Olsen. Utiliza treinamento KSSL e testes no Texas (620 amostras) e leste da Austrália (387), variando tamanho e semelhança espectral do treinamento. É especialmente relevante para D06–D07 pelo teste externo. **Limite:** MIR de amostras e propriedades do solo não demonstram transferência orbital ou mineralógica. A declaração de disponibilidade orienta solicitar acesso aos dados ao KSSL.

## Síntese para o projeto

Na classificação litológica, Costa fornece o precedente brasileiro e Yang, o protocolo com TabPFN e atributos Sentinel-2; ambos discutem o papel das coordenadas. Na composição química, Kutzke amplia os alvos geoquímicos a partir de espectros, Zhang leva a predição geoquímica a dados de satélite e Chen une TabPFN e Sentinel-2. Na generalização, Barkov orienta bibliotecas espectrais de diferentes escalas e instrumentos, e Huang testa o TabPFN em uma região externa. As diferenças entre entradas e tarefas impedem comparar seus resultados como um único benchmark.

Nesta busca, não foi confirmado um estudo que reúna TabPFN, Sentinel-2, classificação litológica terrestre e previsão quantitativa de proporções minerais com teste entre regiões. Isso delimita a evidência encontrada, sem provar inexistência ou originalidade absoluta. A contribuição depende dos rótulos efetivamente disponíveis e das avaliações executadas. Essa busca foi feita quando o alvo estava redigido como proporções minerais; o alvo do TCC é a composição química (D01, esclarecido em 4 de novembro de 2026). A busca complementar de 4 de novembro de 2026, descrita abaixo, também não encontrou estudo que aplique TabPFN a teores de elementos ou óxidos a partir de dados de satélite.

Terras raras constituem alternativa condicionada em D09, não foco exclusivo adotado. Estes estudos não validam especificamente sua previsão orbital. Teores elementares, identidade mineral e frações mineralógicas permanecem tarefas distintas.

## Revisão da seleção em 4 de novembro de 2026

Decisão do autor, após reavaliação da contribuição de cada estudo sugerida pela IA. O mínimo exigido pelo orientador é de seis artigos; a seleção passou de oito para sete.

- **Removido Peña-Asensio et al. (2024).** O TabPFN aparece apenas na classificação, sem divisão de teste descrita nem comparação com outros modelos; os rótulos minerais foram atribuídos a partir da própria composição medida, e os 126 registros de SEM-EDS não têm relação com dados orbitais. Sua justificativa era a identificação mineral, que deixou de ser alvo com D01.
- **Removido Luo et al. (2025).** O foco é o aumento de dados; sem dados sintéticos, o TabPFN tem acurácia balanceada inferior à do Random Forest na litologia (0,820 contra 0,843), e as entradas são perfis de poço. A tarefa litológica permanece sustentada por Costa.
- **Incluído Yang, Huang e Lu (2026)**, pelo uso central do TabPFN em classificação com atributos Sentinel-2, comparação com modelos convencionais, teste com poucas amostras e análise do efeito das coordenadas.

As pastas removidas foram preservadas em `fontes/artigos-descartados/`. A numeração das pastas mantidas foi ajustada para `01`–`07`.

Busca complementar (Playwright e buscador web, 4 de novembro de 2026): não foi encontrado estudo com TabPFN aplicado a teores de elementos, metais pesados, terras raras, anomalias geoquímicas, prospectividade ou litologia a partir de satélite. Foram verificados e não selecionados: [Schmidinger et al. (2026)](https://arxiv.org/abs/2509.09408), TabPFN com atributos de krigagem em mapeamento de solo, alternativa para discutir coordenadas; [Barkov et al. (2026)](https://arxiv.org/abs/2508.09888), TabPFN em 31 conjuntos de 30 a 460 amostras, sobreposto ao estudo 2; [Kasenov et al. (2026)](https://www.mdpi.com/1999-4893/19/4/302), previsão de Au, Cu e Li sem TabPFN; e o [mapeamento de solo no norte do Cazaquistão (2026)](https://www.mdpi.com/2077-0472/16/11/1239), que cita o TabPFN sem avaliá-lo. A ausência encontrada delimita a busca, sem provar inexistência.

## Triagem e abrangência da pesquisa incorporada

Foram consideradas as 21 entradas de artigos da lista anterior, os materiais brasileiros complementares e os oito candidatos novos. Permaneceram, em 9 de outubro de 2026, três entradas antigas, quatro candidatos novos e Barkov, já analisado no projeto; dois deles foram removidos na revisão de 4 de novembro de 2026. A seleção priorizou aderência e complementaridade.

Bai e Zhao foram preteridos pela sobreposição com Zhang; Santos e Ma perderam prioridade diante dos precedentes diretos de TabPFN e da cobertura brasileira de Costa. Estudos de prospectividade, GNN, grafos de conhecimento e aprendizado positivo–não rotulado respondem sobretudo à favorabilidade de depósitos. Schmidinger e o outro Barkov são metodológicos; Setiawati e Jouichat abordam propriedades do solo menos próximas dos alvos centrais. A exclusão desta lista curta não invalida os trabalhos nem remove referências já utilizadas em capítulos.

A pesquisa incorporada executou consultas em inglês, mandarim, hindi, espanhol, árabe padrão, francês, bengali, português, indonésio, urdu, russo, alemão, japonês, pidgin nigeriano, árabe egípcio, marata, vietnamita, telugo, suaíli, hauçá, turco, punjabi ocidental, tagalo, tâmil e cantonês/Yue, seguindo a [tabela por total de falantes baseada no Ethnologue 2026](https://en.wikipedia.org/wiki/List_of_languages_by_total_number_of_speakers). Isso não significa encontrar artigos em 25 idiomas; os estudos confirmados foram predominantemente em inglês.

Esta é uma revisão dirigida, não uma revisão sistemática exaustiva. Os sete estudos estão disponíveis em `fontes/artigos/`, conforme o índice `fontes/README.md`. Após a reabertura com intervenção do autor, o [HTML integral de Kutzke](https://www.tandfonline.com/doi/full/10.1080/08120099.2022.2094465) e seus visualizadores de tabelas e figuras foram acessados com Playwright; a leitura corrigiu a descrição do experimento entre crátons. Antes de reproduzir experimentos, conferir protocolos e suplementos.
