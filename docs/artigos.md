# Revisão bibliográfica — oito estudos prioritários

Atualizada em 9 de outubro de 2026. Consolida a lista anterior e a pesquisa multilíngue de TabPFN. A seleção prioriza aderência e complementaridade com D01–D07: litologia, identificação mineral, integração orbital, harmonização e generalização regional. Não implica implementar todos os métodos citados.

## Estudos selecionados

### 1. Costa, Tavares e Oliveira (2019) — litologia no Brasil

[Predictive lithological mapping through machine learning methods: a case study in the Cinzento Lineament, Carajás Province, Brazil](https://jgsb.sgb.gov.br/index.php/journal/article/view/63). *Journal of the Geological Survey of Brazil*, 2(1), 26–36. DOI: 10.29396/jgsb.2019.v2.n1.3. BibTeX: `costa2019`.

Aplica Random Forest a dados remotos e geofísicos, comparando mapas litológicos com e sem coordenadas, com 1.400 amostras de treinamento. É o precedente brasileiro mais diretamente ligado à classificação proposta. Orienta a comparação com um modelo convencional e a análise da localização. **Limite:** não usa TabPFN nem prevê composição mineral. Coordenadas exigem avaliação que diferencie reconhecimento local de transferência para outra região.

### 2. Luo et al. (2025) — TabPFN para classificação litológica

[Enhancing reservoir parameter prediction workflows via advanced core data augmentation](https://www.sciencedirect.com/science/article/pii/S0264817225003228). *Marine and Petroleum Geology*, 182, 107605. DOI: 10.1016/j.marpetgeo.2025.107605. BibTeX: `luo2025`.

Estuda aumento de dados de testemunhos para classificação litológica e predição petrofísica em reservatórios areníticos, destacando TabDDPM–TabPFN. Sustenta a pertinência do TabPFN à tarefa litológica com poucos registros. **Limite:** utiliza perfis de poços e experimentos em testemunhos, não reflectância orbital. O resultado da combinação não isola o ganho do TabPFN; dados sintéticos não são observações independentes. Conferir o protocolo completo antes de adotar aumento de dados.

### 3. Peña-Asensio et al. (2024) — identificação mineral

[Machine learning applications on lunar meteorite minerals: From classification to mechanical properties prediction](https://www.sciencedirect.com/science/article/pii/S2095268624001010). *International Journal of Mining Science and Technology*, 34(9), 1283–1292. DOI: 10.1016/j.ijmst.2024.08.001. BibTeX: `pena2024`.

Classifica meteoritos, grupos minerais e minerais com TabPFN a partir de porcentagens atômicas obtidas por microscopia em três meteoritos lunares. A regressão das propriedades mecânicas utiliza outros modelos. É um precedente de identificação mineral, distinto de propriedades agronômicas. **Limite:** composição microscópica não equivale a bandas Sentinel-2; identificar minerais não equivale a prever suas proporções no solo. A classificação elevada nesse conjunto não demonstra transferência para materiais terrestres.

### 4. Zhang et al. (2023) — integração orbital e geoquímica

[Deriving big geochemical data from high-resolution remote sensing data via machine learning: Application to a tailing storage facility in the Witwatersrand goldfields](https://www.sciencedirect.com/science/article/pii/S2666544123000059). *Artificial Intelligence in Geosciences*, 4, 9–21. DOI: 10.1016/j.aiig.2023.01.005. BibTeX: `zhang2023`.

Relaciona atributos orbitais a um modelo geoestatístico derivado de análises de ouro em rejeitos. É uma ponte direta entre referências laboratoriais, localização e espectros para estimar teor. **Limite:** rejeitos de uma instalação não representam solos naturais mundiais nem proporções minerais. Interpolações não são novas análises independentes. Landsat-8 auxilia o alinhamento histórico e Sentinel-2 fornece os atributos preditivos; isso não estabelece superioridade geral sobre Landsat, especialmente Landsat-5.

### 5. Chen et al. (2026) — TabPFN com Sentinel-2

[Integrating transformer-based learning and Sentinel-2 bare soil composites for soil organic carbon mapping in the black soil region of Northeast China](https://www.nature.com/articles/s41598-025-33682-4). *Scientific Reports*, 16, 3784; publicado em 5 de janeiro de 2026. DOI: 10.1038/s41598-025-33682-4. BibTeX: `chen2026`.

Integra composições multitemporais de solo exposto e variáveis ambientais com 174 amostras. TabPFN com composição P50 apresenta R² de 0,78 e RMSE de 1,90 g/kg para carbono orgânico, superando CNN e XGBoost no estudo. Orienta extração orbital e controle da superfície. **Limite:** carbono orgânico não é composição mineralógica. A reamostragem local não substitui teste em regiões externas nem garante resultado para litologia ou terras raras.

### 6. Barkov et al. (2026) — bibliotecas harmonizadas

[From field-scale to large-scale spectral libraries: Tabular foundation models in soil spectroscopy](https://arxiv.org/html/2608.00608v1). Preprint arXiv:2608.00608v1, submetido em 1 de agosto de 2026. DOI: 10.48550/arXiv.2608.00608. BibTeX: `barkov2026`.

Compara modelos e representações espectrais em 85 tarefas de regressão com LimeSoDa e OSSL, incluindo TabPFN. Fundamenta diferentes escalas de dados e preparação dos atributos. **Limite:** usa espectros vis-NIR/MIR de amostras, não imagens orbitais; os alvos são propriedades do solo. Variabilidade entre instrumentos não demonstra benefício causal de misturar sensores. Partições aleatórias não respondem, por si, à hipótese de transferência entre regiões. Trata-se de preprint.

### 7. Huang et al. (2026) — teste externo

[Zero-shot inference with Tabular Prior-data Fitted Network (TabPFN) for soil MIR spectral analysis](https://www.sciencedirect.com/science/article/pii/S0016706126002089). *Geoderma*, 471, 117880. DOI: 10.1016/j.geoderma.2026.117880. BibTeX: `huang2026`.

Compara TabPFN, PLSR, Cubist e CNN para carbono total, pH e fósforo extraível por Olsen. Utiliza treinamento KSSL e testes no Texas (620 amostras) e leste da Austrália (387), variando tamanho e semelhança espectral do treinamento. É especialmente relevante para D06–D07 pelo teste externo. **Limite:** MIR de amostras e propriedades do solo não demonstram transferência orbital ou mineralógica. A declaração de disponibilidade orienta solicitar acesso aos dados ao KSSL.

### 8. Kutzke, Eichstaedt e Kahnt (2022) — diversos alvos geoquímicos

[Potential of hyperspectral-based geochemical predictions with neural networks for strategic and regional exploration improvement](https://doi.org/10.1080/08120099.2022.2094465). *Australian Journal of Earth Sciences*, 69(8), 1197–1206. DOI: 10.1080/08120099.2022.2094465. BibTeX: `kutzke2022`.

Relaciona espectros hiperespectrais de testemunhos a referências geoquímicas, avaliando classes de teor definidas por limiares. É pertinente à intenção de investigar diversos alvos. **Limite:** classes de teor não são regressão contínua de proporções minerais; não utiliza TabPFN ou satélite. A divisão aleatória 60/20/20 não comprova transferência regional. Sustenta investigar múltiplos alvos, mas não que todos sejam previsíveis ou igualmente viáveis.

## Síntese para o projeto

Costa e Luo sustentam a tarefa litológica; Peña-Asensio fornece identificação mineral. Zhang e Chen sustentam integração orbital com referências; Barkov e Huang orientam bibliotecas e generalização; Kutzke amplia os alvos geoquímicos. As diferenças entre entradas e tarefas impedem comparar seus resultados como um único benchmark.

Nesta busca, não foi confirmado um estudo que reúna TabPFN, Sentinel-2, classificação litológica terrestre e previsão quantitativa de proporções minerais com teste entre regiões. Isso delimita a evidência encontrada, sem provar inexistência ou originalidade absoluta. A contribuição depende dos rótulos efetivamente disponíveis e das avaliações executadas.

Terras raras constituem alternativa condicionada em D09, não foco exclusivo adotado. Estes estudos não validam especificamente sua previsão orbital. Teores elementares, identidade mineral e frações mineralógicas permanecem tarefas distintas.

## Triagem e abrangência da pesquisa incorporada

Foram consideradas as 21 entradas de artigos da lista anterior, os materiais brasileiros complementares e os oito candidatos novos. Permaneceram três entradas antigas, quatro candidatos novos e Barkov, já analisado no projeto. A seleção priorizou aderência e complementaridade.

Bai e Zhao foram preteridos pela sobreposição com Zhang; Santos e Ma perderam prioridade diante dos precedentes diretos de TabPFN e da cobertura brasileira de Costa. Estudos de prospectividade, GNN, grafos de conhecimento e aprendizado positivo–não rotulado respondem sobretudo à favorabilidade de depósitos. Schmidinger e o outro Barkov são metodológicos; Setiawati e Jouichat abordam propriedades do solo menos próximas dos alvos centrais. A exclusão desta lista curta não invalida os trabalhos nem remove referências já utilizadas em capítulos.

A pesquisa incorporada executou consultas em inglês, mandarim, hindi, espanhol, árabe padrão, francês, bengali, português, indonésio, urdu, russo, alemão, japonês, pidgin nigeriano, árabe egípcio, marata, vietnamita, telugo, suaíli, hauçá, turco, punjabi ocidental, tagalo, tâmil e cantonês/Yue, seguindo a [tabela por total de falantes baseada no Ethnologue 2026](https://en.wikipedia.org/wiki/List_of_languages_by_total_number_of_speakers). Isso não significa encontrar artigos em 25 idiomas; os estudos confirmados foram predominantemente em inglês.

Esta é uma revisão dirigida dos textos e trechos acessíveis, não uma revisão sistemática exaustiva. Foram consultadas fontes editoriais, repositórios e o texto local de Zhang. ScienceDirect e Scientific Reports foram abertos com Playwright. Taylor & Francis bloqueou o acesso direto; Kutzke foi conferido no conteúdo editorial indexado. Antes de reproduzir experimentos, conferir integralmente protocolos e suplementos.
