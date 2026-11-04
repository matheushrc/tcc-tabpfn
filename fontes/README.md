# Fontes para consulta

Esta pasta reúne os oito estudos selecionados em `docs/artigos.md`. Os oito possuem `artigo.md`: sete foram extraídos do HTML original com o MCP do Playwright em 6 ou 9 de outubro de 2026; Costa et al. foram convertidos do PDF local com o MCP do PDFCraft em 2 de novembro de 2026. A data de extração não é a data de publicação. O PDF de Costa et al. foi preservado; os demais PDFs redundantes foram removidos conforme a preferência do autor pelo HTML.

| Pasta em `artigos/` | Fonte original | Formato |
| --- | --- | --- |
| `01-geoquimica-rejeitos-witwatersrand/` | [Deriving big geochemical data from high-resolution remote sensing data via machine learning: Application to a tailing storage facility in the Witwatersrand goldfields](https://www.sciencedirect.com/science/article/pii/S2666544123000059) | Markdown; fórmulas em LaTeX |
| `02-tabpfn-espectroscopia-solo/` | [From field-scale to large-scale spectral libraries: Tabular foundation models in soil spectroscopy](https://arxiv.org/html/2608.00608v1) | Markdown, versão v1; fórmulas em LaTeX |
| `03-mapeamento-litologico-carajas/` | [Predictive lithological mapping through machine learning methods: a case study in the Cinzento Lineament, Carajás Province, Brazil](https://jgsb.sgb.gov.br/index.php/journal/article/view/63) | Markdown extraído do PDF via MCP PDFCraft; seis figuras, seis tabelas e 33 referências; PDF editorial de 11 páginas preservado |
| `04-tabpfn-minerais-meteoritos/` | [Machine learning applications on lunar meteorite minerals: From classification to mechanical properties prediction](https://www.sciencedirect.com/science/article/pii/S2095268624001010) | Markdown; cinco figuras, cinco tabelas e fórmulas em LaTeX |
| `05-hiperespectral-predicao-geoquimica/` | [Potential of hyperspectral-based geochemical predictions with neural networks for strategic and regional exploration improvement](https://doi.org/10.1080/08120099.2022.2094465) | Markdown; cinco tabelas completas e três figuras; CSVs em `assets/` |
| `06-tabpfn-sentinel2-carbono-solo/` | [Integrating transformer-based learning and Sentinel-2 bare soil composites for soil organic carbon mapping in the black soil region of Northeast China](https://www.nature.com/articles/s41598-025-33682-4) | Markdown; tabela incorporada da página editorial de tamanho completo |
| `07-tabpfn-mir-validacao-externa/` | [Zero-shot inference with Tabular Prior-data Fitted Network (TabPFN) for soil MIR spectral analysis](https://www.sciencedirect.com/science/article/pii/S0016706126002089) | Markdown; seis figuras, três tabelas e fórmulas em LaTeX |
| `08-tabpfn-litologia-reservatorios/` | [Enhancing reservoir parameter prediction workflows via advanced core data augmentation](https://www.sciencedirect.com/science/article/pii/S0264817225003228) | Markdown; 13 figuras, cinco tabelas e fórmulas em LaTeX |

Os títulos ficam no front matter; o corpo preserva autores, texto, citações, figuras, tabelas e referências. Os links usam URLs completas. As figuras de cada artigo ficam na pasta `assets/` do próprio artigo, nomeadas `figura-<número>.<extensão>` (por exemplo, `figura-1.jpg` e `figura-a1.svg` para figuras de apêndice); no Markdown, cada imagem usa o caminho relativo `assets/` e aponta para a URL original da imagem, na maior resolução disponível. As chamadas de figura no texto, como `[Fig. 1](assets/figura-1.jpg)`, também apontam para esses arquivos locais. As seis imagens de Costa et al. foram extraídas do PDF e apontam para as páginas correspondentes no RIGeo. As tabelas usam Markdown, com repetição das células mescladas nas linhas ou colunas correspondentes e combinação dos níveis de cabeçalho. Os arquivos Markdown dos artigos não usam tags HTML; índices e expoentes usam matemática LaTeX, e as citações mantêm links em Markdown. As fórmulas usam LaTeX, sem MathML dentro dos delimitadores matemáticos. Autores, siglas, listas e referências têm formatação contínua, e controles de navegação foram removidos. Confira os elementos na fonte original antes de transcrever dados para o TCC.

Em Kutzke, os botões de tabelas e figuras foram abertos pelo Playwright. Os cinco CSVs são exportações das tabelas publicadas, e não uma cópia dos registros brutos de espectroscopia e geoquímica. A procedência dos arquivos está documentada em `05-hiperespectral-predicao-geoquimica/assets/README.md`. Os textos de análise já redigidos foram preservados. Cada pasta possui um arquivo `fundamentacao-teorica.md` com roteiro de leitura identificado como sugestão da IA, para apoiar a escrita pelo autor.

Os artigos usam prefixos numéricos e nomes curtos relacionados ao assunto. As notícias estão em `fontes/noticias/`; documentos institucionais e legislação podem ser guardados em `fontes/documentos-institucionais/` e `fontes/legislacao/` quando forem adicionados.

## Ordem de preparação das análises

As pastas `01` e `02` seguem as subseções 3.1 e 3.2 já redigidas em `tcc/markdown/03-trabalhos-relacionados.md`. Seus arquivos `fundamentacao-teorica.md` preservam essas análises de estudos; apesar do nome, pertencem a Trabalhos Relacionados. A fundamentação conceitual de `tcc/markdown/02-revisao-bibliografica.md` continua pendente.

A ordem `03` a `08` é uma sugestão editorial da IA, adotada apenas para organizar a preparação solicitada pelo autor. Não representa subseções já escritas nem compromisso de implementar os métodos dos artigos.

| Ordem | Estudo | Situação da análise | Motivo da posição e limites a preservar |
| --- | --- | --- | --- |
| 01 | Zhang et al. | Texto da seção 3.1 preservado; roteiro acrescentado | Integração orbital e geoquímica; o modelo geoestatístico não fornece novas observações laboratoriais independentes. |
| 02 | Barkov et al. | Texto da seção 3.2 preservado; roteiro acrescentado | TabPFN em bibliotecas espectrais, harmonização e limites das partições aleatórias. |
| 03 | Costa et al. | Roteiro criado; análise pelo autor pendente | Precedente brasileiro de mapeamento litológico com Random Forest; permite discutir coordenadas e concordância com mapas de referência. |
| 04 | Peña-Asensio et al. | Roteiro criado; análise pelo autor pendente | Identificação mineral com TabPFN a partir de composição microscópica; distinguir identidade mineral de proporções mineralógicas e bandas orbitais. |
| 05 | Kutzke et al. | Roteiro criado; análise pelo autor pendente | Múltiplos alvos geoquímicos e transferência entre crátons; espectros de testemunhos e comparação entre previsões não equivalem a validação orbital independente. |
| 06 | Chen et al. | Roteiro criado; análise pelo autor pendente | Aproximação ao sensor proposto: TabPFN com Sentinel-2 e controle de solo exposto; o alvo é carbono orgânico. |
| 07 | Huang et al. | Roteiro criado; análise pelo autor pendente | Avaliação externa com espectros MIR, útil para discutir generalização; não demonstra transferência orbital entre regiões para os alvos deste TCC. |
| 08 | Luo et al. | Roteiro criado; análise pelo autor pendente | Complemento sobre classificação litológica e aumento de dados em poços; amostras sintéticas não são novas referências independentes e a técnica não foi adotada no protocolo do TCC. |

Os títulos e as URLs originais dos oito estudos estão na tabela acima. Essa sequência organiza a leitura e a redação pelo autor, mantendo a separação entre conceitos no capítulo 2 e comparação de estudos no capítulo 3. Os roteiros não acrescentam parágrafos acadêmicos aos capítulos. As referências usadas apenas neles não entram em `tcc/latex/bibliografia.bib` enquanto não forem efetivamente citadas no TCC.
