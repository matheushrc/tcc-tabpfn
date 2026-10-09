# tcc-tabpfn

## Escrita do TCC

O texto principal da introdução está em `tcc/markdown/01-introducao.md`. Faça as revisões de conteúdo no Markdown e solicite à IA a atualização de `tcc/latex/capitulos/01-introducao.tex` quando necessário, seguindo o template da faculdade.

Os dados básicos do trabalho ficam em `tcc.conf`, no formato `chave=valor`. O projeto LaTeX está em `tcc/latex/`, com `principal.tex` como documento principal e `bibliografia.bib` para referências. `Template_UFFSTex/` preserva o modelo original.

Para revisar no Overleaf, envie os arquivos de `tcc/latex/`, preservando as subpastas, e selecione `principal.tex` como documento principal. A tentativa de compilação local ficou bloqueada no carregamento do Babel/MiKTeX; o PDF ainda não foi validado. Título em inglês, palavras-chave, resumo e abstract permanecem pendentes para o fim do TCC I; a versão atual contém introdução e trabalhos relacionados; a revisão conceitual está pendente.

Consulte `ARCHITECTURE.md` para a organização das áreas, `AGENTS.md` para as regras de trabalho e `ORGANIZACAO_TCC.md` para o plano e as verificações da reorganização. `templates/natanael/` contém o documento integral de referência e um projeto LaTeX de reprodução por inclusão do PDF; `templates/guia-trabalhos-relacionados.md` contém o guia de escrita.

As seções abaixo registram o histórico de pesquisa e planejamento; decisões atuais de conteúdo devem seguir o Markdown principal.

Purpose & context

Matheus Henrique is developing a TCC (undergraduate thesis) combining artificial intelligence and geospatial analysis, under a professor's guidance. The core research question is: "Is it possible to estimate the mineral composition of a region from satellite spectral signatures using tabular/geospatial learning models trained on historical geochemical data?"

The project aims to train ML models on geochemical deposit data paired with satellite imagery to identify potential new mining locations. An ambitious case study is planned: retroactively applying the trained model to historical Landsat imagery of the Serra Pelada gold deposit in Brazil (pre-discovery, pre-1979) as a qualitative exploratory validation.

Key domain areas: mineral prospectivity mapping, remote sensing, geospatial ML, and multi-target regression.

Current state

The task framing has been significantly refined through prior exploration:

Problem formulation: Shifted from binary presence/absence classification (which requires artificial negative sampling with known bias issues) to multi-target regression — predicting mineral composition vectors (elemental percentages) from satellite spectral signatures. This formulation is more scientifically sound given the dataset structure.
Primary dataset: National Geochemical Database on Ore Deposits (NGDOD), Legacy Data (USGS ScienceBase), containing geochemical composition data (~30K samples across US deposit types, with elemental percentages per location). Next step is examining the actual CSV column structure to confirm which elements have sufficient sample coverage.
Model landscape: TabPFN v2 (professor-suggested, supports regression), Random Forest/XGBoost regressors as baselines, and GNNs for spatially-structured regression — enabling the model comparison the professor expects.
Serra Pelada framing: Recast as a qualitative case study with explicit acknowledgment of limitations: cross-sensor generalization (Landsat MSS vs. Sentinel-2), cross-region generalization (US-trained model applied to Brazil), and the geological constraint that Serra Pelada is an alluvial deposit with limited surface spectral signature prior to mining.
GEE pipeline: Still in planning — feature extraction per coordinate using Sentinel-2 or Landsat bands and spectral indices is the next major technical step.

On the horizon

Examine NGDOD CSV column structure to identify elements with sufficient coverage for regression targets
Design and implement the Google Earth Engine (GEE) spectral feature extraction pipeline (band values + indices per geochemical sample coordinate)
Finalize model architecture decisions for GNN (spatial graph construction approach)
Plan cross-sensor preprocessing strategy for the Serra Pelada historical Landsat MSS case study

Key learnings & principles

Percentage composition encodes relative absence: A key insight — elemental percentage data implicitly reflects the relative absence of other minerals, making regression more informative than binary classification and avoiding the need for artificial negative sampling.
Task-dataset alignment matters: The TIME paper (arxiv.org/html/2506.00813v1) — a multimodal tabular-image fusion framework from the medical domain — does not directly map onto this geospatial prospectivity problem, though TabPFN's role as a tabular encoder within it is relevant context.
Geological realism as a constraint: Serra Pelada's alluvial nature means surface spectral signatures before excavation are geologically limited — important for setting honest expectations about the case study's predictive power.
Negative sampling bias: Binary classification approaches for prospectivity mapping suffer from the problem of selecting representative "absence" samples, which the regression reformulation sidesteps entirely.

Approach & patterns

Research direction is professor-guided, with Matheus independently proposing model candidates (e.g., GNNs) and finding supporting literature.
Iterative problem reformulation: willing to revisit fundamental framing when new insights (like the composition-as-relative-absence insight) warrant it.
Validation strategy balances quantitative model comparison (on US data) with qualitative historical case study (Serra Pelada).

Tools & resources

Data: NGDOD Legacy Data (USGS ScienceBase item 60abefced34ea221ce51f37f)
Remote sensing: Google Earth Engine (GEE), Sentinel-2, Landsat MSS; spectral indices including iron oxide index, clay index, SWIR band ratios, hydrothermal alteration signatures
ML frameworks: TabPFN v2, Random Forest, XGBoost, GNNs
Reference paper: TIME framework (arxiv.org/html/2506.00813v1) — multimodal tabular-image fusion
Other references: SIGMINE (ANM) for Brazilian mining data context

DAVIES, Rhys S.; TROTT, McLean; GEORGI, Jaakko; et al. Artificial intelligence and machine learning to enhance critical mineral deposit discovery. Geosystems and Geoenvironment, vol. 4, no. 2, p. 100361, 2025. Disponível em: <https://www.sciencedirect.com/science/article/pii/S2772883825000111>. Acesso em: 21 Aug. 2026.

LUO, Jiaqi; YUAN, Yuan and XU, Shixin. TIME: TabPFN-Integrated Multimodal Engine for Robust Tabular-Image Learning. arXiv.org. Disponível em: <https://arxiv.org/abs/2506.00813v1>. Acesso em: 21 Aug. 2026.
