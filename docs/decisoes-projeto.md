# Registro de decisões, ideias e pendências do TCC

Registro iniciado em 9 de outubro de 2026, a partir das intenções expressas pelo autor na discussão do projeto. Os dados básicos e o título vigente permanecem definidos em `tcc.conf`.

## Finalidade e uso

Este arquivo acompanha o que foi proposto, o que depende de confirmação e o que foi efetivamente realizado. Uma intenção registrada não comprova execução nem resultado. Antes de finalizar o TCC, conferir cada item com os arquivos, procedimentos e resultados produzidos e ajustar o texto acadêmico ao escopo efetivamente executado.

Estados utilizados: **decisão de escopo** (direção adotada, ainda sujeita à viabilidade), **intenção** (entrega pretendida), **hipótese** (afirmação a testar), **pendência** (informação ainda não confirmada), **realizado** (exige evidência) e **descartado** (exige motivo). Nenhuma atividade experimental ou publicação está marcada como realizada neste registro inicial.

## Escopo registrado

| ID | Decisão ou ideia expressa | Estado inicial | Condição ou evidência necessária |
| --- | --- | --- | --- |
| D01 | Avaliar o TabPFN para classificação litológica e predição da composição mineral a partir de dados espectrais de satélite. | Decisão de escopo | Confirmar rótulos litológicos e medidas mineralógicas adequados; registrar versão do modelo, tarefas executadas e métricas. |
| D02 | Reunir e harmonizar datasets de diferentes regiões do mundo já reunidos pelo autor em sua máquina pessoal. | Decisão de escopo | Inventariar as cópias utilizadas, procedência, coordenadas, materiais, métodos, unidades, licenças e alvos compatíveis. A documentação existente não substitui a inspeção dos arquivos. |
| D03 | Utilizar datasets de áreas brasileiras mapeadas e em exploração, que o coorientador informou que forneceria. | Intenção e pendência | Receber os arquivos e conferir cobertura, datas, origem dos rótulos e análises disponíveis. O uso de Landsat-5 foi relatado pelo autor como aparente e permanece não confirmado. |
| D04 | Aproveitar coordenadas e referências geológicas/laboratoriais dos datasets brasileiros e obter dados espectrais Sentinel-2 para as mesmas áreas. | Decisão de escopo condicionada | Confirmar correspondência espacial e temporal, precisão das coordenadas, profundidade das amostras e condições da superfície. Extrair reflectância das imagens; metadados de aquisição são documentação complementar. |
| D05 | Associar dados espectrais de satélite a classes litológicas e medidas laboratoriais por integração espacial. | Decisão de escopo | Documentar como pontos ou polígonos foram associados a pixels ou áreas, incluindo resolução, agregação, datas e filtros de qualidade. |
| D06 | Investigar se reunir dados harmonizados de diferentes regiões amplia a representatividade e melhora a generalização do TabPFN. | Hipótese | Comparar treinamento com uma e com múltiplas regiões, mantendo a mesma região externa de teste e controles comparáveis. Registrar ganhos, ausência de ganho ou perdas. |
| D07 | Avaliar o modelo em regiões que não participaram do ajuste. | Decisão de escopo condicionada | Definir grupos e regiões retidas antes da avaliação; impedir que amostras relacionadas ou procedimentos de ajuste utilizem os dados de teste. Confirmar que há dados compatíveis suficientes. |
| D08 | Disponibilizar no Kaggle os datasets derivados da integração e harmonização. | Intenção | Confirmar direito de redistribuição de cada fonte; documentar transformações, versões e limitações. Registrar URL e versão somente após a publicação. Se alguma fonte não puder ser redistribuída, documentar a exclusão ou disponibilizar procedimentos de obtenção e preparação. |
| D09 | Manter a maior abrangência viável de minerais e alvos de composição disponíveis; considerar terras raras como recorte se a abrangência maior for inviável. | Decisão de escopo condicionada | Sugestão do coorientador relatada pelo autor, que prefere manter os demais alvos quando possível. Confirmar referências, cobertura por alvo/região, métodos, qualidade, quantidade de amostras e custo computacional. Justificar eventual redução com inspeção e avaliação preliminar. Não constitui foco exclusivo já adotado. |

| D10 | Desenvolver o tema de análise mineral em três trabalhos: este com foco em TabPFN, outro em CNN e outro em modelos mais básicos. | Organização informada pelo autor | Registrar responsabilidades e contribuições efetivas. Nomes, algoritmos específicos do terceiro trabalho e protocolo compartilhado não foram informados. Não atribuir ao autor resultados ou implementações dos colegas. |
| D11 | Explorar uma camada de análise de imagens de satélite e uma fusão adicional de suas saídas ou representações com as do ramo tabular, inspirada no TIME. | Possibilidade opcional, condicionada a tempo | O professor considerou a extensão excessiva para o prazo disponível, segundo o autor. Priorizar o estudo principal de TabPFN; considerar a extensão somente após concluídas suas entregas essenciais e se houver tempo, dados e recursos suficientes. Arquitetura, tipo de saída e cooperação com o trabalho de CNN ainda não definidos. |

| D12 | Seguir a organização do TCC de Natanael: Revisão Bibliográfica no capítulo 2 e Trabalhos Relacionados no capítulo 3; reunir referências de escrita em `templates/`. | Decisão de organização | Sumário do PDF local conferido. Textos dos artigos preservados no capítulo 3; fundamentação conceitual pendente. Só o PDF de Natanael está disponível, sem fontes LaTeX originais. |

## Distinções que devem ser preservadas no texto

- **Geoquímica e mineralogia:** concentrações de elementos ou óxidos não equivalem automaticamente a proporções de minerais. Se as bases permitirem apenas alvos geoquímicos, registrar a limitação e revisar o escopo, os objetivos e, com o autor e os orientadores, o título; não apresentar regressão geoquímica como composição mineralógica medida.
- **Referência independente e mapa derivado:** verificar se as classes litológicas vêm de campo, laboratório ou de classificação prévia de imagens. Reproduzir rótulos de um mapa Landsat não equivale a validar a litologia contra observações independentes.
- **Superfície e subsuperfície:** registrar a relação entre o material amostrado e a superfície observada. Amostras profundas, material transportado e áreas alteradas pela mineração exigem interpretação específica.
- **Diversidade e melhoria:** a integração de bases é uma proposta de preparação dos dados; a melhoria da generalização é uma hipótese. Não afirmar que misturar sensores ou regiões necessariamente melhora o desempenho.
- **Volume e independência:** mais pixels, linhas interpoladas ou previsões não constituem novas análises laboratoriais independentes. Identificar separadamente observações, interpolações e previsões, se estas forem produzidas.
- **Disponibilidade e conclusão:** reunir bases não demonstra que os alvos necessários existem, nem que o conjunto final já foi criado ou publicado. Não qualificar o produto como big data sem critérios e evidências.
- **Triagem e descoberta:** avaliar o potencial de apoio à investigação não comprova descoberta de jazida, reserva ou confirmação de campo. Não foi assumido compromisso de executar uma campanha de validação física.

## Fundamentação e limites dos artigos discutidos

[Barkov et al. (2026)](https://arxiv.org/html/2608.00608v1) avaliam regressão de propriedades do solo com espectroscopia vis-NIR e MIR, usando LimeSoDa e OSSL. A OSSL reúne dados harmonizados de diferentes coleções. O artigo reconhece variabilidade entre métodos e instrumentos, mas não demonstra ganho causado pela mistura de sensores. A avaliação usa partições aleatórias; a transferência para regiões e instrumentos distintos permanece uma questão para investigação.

[Zhang et al. (2023)](https://www.sciencedirect.com/science/article/pii/S2666544123000059) integram um modelo geoestatístico derivado de análises de ouro a dados orbitais. Landsat-8 auxilia o alinhamento histórico, e Sentinel-2 fornece os atributos da modelagem preditiva. Esse procedimento não estabelece uma superioridade geral do Sentinel-2 sobre Landsat, nem constitui comparação com Landsat-5.

## Pendências antes de fechar a metodologia

1. Receber e inspecionar os datasets brasileiros e confirmar o que foi obtido com Landsat-5.
2. Identificar as referências disponíveis para litologia, composição mineralógica e composição geoquímica, separadamente.
3. Selecionar bases e regiões compatíveis, sensores, datas, bandas e critérios de qualidade da superfície.
4. Definir versão do TabPFN, modelos de comparação, métricas e protocolo de validação espacial e entre regiões.
5. Confirmar quais fontes e derivados podem ser publicados no Kaggle.

## Abrangência mineral e alternativa de terras raras

D09 está alinhada a D01–D02. “Manter tudo” significa tentar preservar alvos disponíveis com supervisão adequada, sem prometer previsão de todo mineral ou elemento. O interesse econômico foi relatado pelo autor como motivação da sugestão do coorientador; não é registrado como conclusão sobre preços ou mercado.

Antes de reduzir o escopo, distinguir limitações de memória/tempo, falta de referências compatíveis e desempenho insuficiente por alvo. Vários alvos podem ser avaliados separadamente, sem exigir um único modelo multissaída. A inviabilidade de um alvo não implica excluir todos os demais.

Se terras raras forem o recorte necessário, registrar elementos ou minerais estudados, referências laboratoriais, regiões e motivo da redução, discutindo o recorte final com autor e orientadores. Teores de elementos de terras raras não equivalem a proporções dos minerais portadores. Uma mudança de tarefa ou título requer revisão explícita; D09 não altera automaticamente `tcc.conf`.

## Organização dos trabalhos e extensão multimodal opcional

Segundo o autor, três pessoas desenvolvem trabalhos sobre análise mineral, com focos distintos: TabPFN neste TCC, CNN em outro e modelos mais básicos no terceiro. Essa divisão (D10) esclarece o foco de D01; não significa que os três resultados já existam nem estabelece um experimento conjunto. Eventual compartilhamento de dados, código ou resultados deverá identificar autoria, procedência e responsabilidades. Para comparar trabalhos, será necessário acordar alvos, partições e métricas comparáveis.

A ideia D11 acrescenta à integração espacial de referências laboratoriais e atributos orbitais de D05 um ramo que analise as imagens, seguido de fusão com o ramo tabular. Amplia a arquitetura e o esforço experimental, mas permanece possibilidade para o tempo restante, sem integrar os objetivos obrigatórios atuais. A orientação do professor de que seria muita coisa para o prazo, relatada pelo autor, justifica essa prioridade. Se não for executada, poderá ser apresentada como trabalho futuro, sem resultados atribuídos.

A inspiração é [TIME: TabPFN-Integrated Multimodal Engine for Robust Tabular-Image Learning, de Jiaqi Luo, Yuan Yuan e Shixin Xu (2025)](https://arxiv.org/abs/2506.00813), preprint submetido em 1 de junho de 2025 (BibTeX: `luo2025time`). O resumo descreve TabPFN como codificador tabular congelado, produzindo representações combinadas com atributos de modelos visuais pré-treinados. Portanto, a inspiração principal é fusão de representações; combinar previsões finais seria uma variante a definir, não uma reprodução automaticamente equivalente. O estudo aborda dados naturais e médicos e não comprova desempenho em análise mineral orbital.

Se D11 for retomada, definir primeiro se serão combinados atributos, representações ou previsões; confirmar correspondência espacial entre imagens e registros e comparar com TabPFN isolado usando o mesmo teste externo de D07. Se previsões supervisionadas forem entradas da fusão, gerá-las sem acesso aos rótulos de teste e sem treinar a segunda etapa sobre previsões obtidas com os próprios rótulos dessas amostras. Registrar a decisão de execução antes de acrescentar a extensão aos objetivos ou apresentar resultados. O ramo visual pode exigir articulação com o colega de CNN, mas essa colaboração não foi assumida.

## Conferência final e histórico

Para cada ID, registrar o estado final e a evidência correspondente. Se uma proposta não for executada, manter seu histórico e explicar a mudança; atualizar a introdução, a metodologia e as conclusões para evitar promessas sem correspondência no trabalho realizado. Resultados negativos ou ausência de melhoria também são resultados válidos.

| Data | IDs afetados | Mudança | Motivo e evidência |
| --- | --- | --- | --- |
| 2026-10-09 | D01–D08 | Registro inicial das decisões, intenções e hipóteses. | Discussão com o autor; recebimento das bases brasileiras, experimentos e publicação ainda não comprovados. |
| 2026-10-09 | D09; D01–D02 | Preferência por abrangência mineral/geoquímica ampla, com terras raras como alternativa condicionada. | Instrução do autor e sugestão do coorientador relatada por ele; seleção e viabilidade pendentes. Revisão consolidada em `docs/artigos.md`, sem novos compromissos experimentais. |

| 2026-10-09 | D10–D11; D01, D05, D07 | Registrada a divisão entre três trabalhos e a possibilidade de extensão multimodal, condicionada ao tempo. | Relato do autor, incluindo orientação do professor sobre o prazo; TIME consultado na fonte original. Foco principal permanece TabPFN; extensão não executada e arquitetura pendente. |

| 2026-10-09 | D12 | Corrigidos nomes e numeração dos capítulos conforme o exemplo de Natanael; guia e PDF movidos para `templates/` e exemplo isolado excluído. | Solicitação do autor e sumário do documento local; reprodução LaTeX por inclusão integral do PDF, sem alegar recuperação dos fontes originais. |

| 2026-10-09 | D12 | Reconstrução editável do TCC de Natanael a partir do PDF, usando cópia da classe UFFS. | Solicitação explícita do autor; seis capítulos, elementos pré-textuais, três figuras, cronograma e bibliografia própria em `templates/natanael/`. Conferências de referências documentadas; não se trata dos fontes originais. |
