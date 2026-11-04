# Base de Dados Geoquímica do SGB

Pesquisa da IA em 4 de novembro de 2026, feita para responder à lacuna 2 de `docs/lacunas-dataset-mg.md`: existe um dataset oficial brasileiro com análises laboratoriais que informem teores de vários minerais por amostra? São constatações e sugestões, não decisões do autor. Atualização no mesmo dia: o autor esclareceu que o alvo do TCC é a composição química (D01); para esse alvo, as tabelas de interesse são as de análises químicas, especialmente a de solo, e a mineralometria passa a ser apenas apoio. A plataforma foi aberta com o MCP do Playwright e os serviços foram consultados diretamente.

## Fonte encontrada

A Base de Dados Geoquímica do Serviço Geológico do Brasil (SGB) é oficial, pública e atualizada continuamente; as camadas consultadas estão identificadas como “Geoquímica Exploratória – Jul/2026” e “Geoquímica Ambiental – Jul/2026”.

- Plataforma: <https://geoportal.sgb.gov.br/geoquimica>
- Serviço ArcGIS consultável (exploratória): <https://geoportal.sgb.gov.br/server/rest/services/geologia/geoq_externa/MapServer>
- Serviço ArcGIS consultável (ambiental): <https://geoportal.sgb.gov.br/server/rest/services/gestaoterritorial/geoq_externa_amb/MapServer>
- Lançamento: [MundoGEO, 29 de agosto de 2025](https://mundogeo.com/2025/08/29/servico-geologico-do-brasil-lanca-nova-plataforma-para-acesso-a-dados-geoquimicos/), com dados de 138 projetos georreferenciados.

O aviso da plataforma informa que a base está em atualização contínua e que os valores podem variar com o método analítico e a época da análise; a documentação de cada projeto está no RIGeo.

## Mineralometria: vários minerais por amostra

A tabela “Resultados analíticos de Mineralometria” informa, para cada amostra de concentrado de bateia (minerais pesados), a proporção de vários minerais ao mesmo tempo. Há 134 minerais distintos na base, como magnetita, hematita, ilmenita, zircão, monazita, ouro, cianita e turmalina.

Exemplo conferido no projeto “Mapeamento Geoquímico do Quadrilátero Ferrífero e seu Entorno”, amostra de campo `4070-MR-B-0005` (lat −20,069; lon −44,537), analisada em 2009 pela SGS Geosol, leitura “Mineralometria Semiquantitativa”: magnetita S40, limonita S40, ilmenita S15, hematita S3, zircão S3 e outros 11 minerais com S1.

Os valores são classes semiquantitativas, não percentuais exatos. Segundo [Lins e Castro (2010), CPRM](https://rigeo.sgb.gov.br/bitstream/doc/15957/1/P60_CassianoCastroetal_ConcentradoBateia.pdf):

| Código | Faixa |
| --- | --- |
| S1 | < 1% |
| S3 | 1–5% |
| S15 | 5–25% |
| S40 | 25–50% |
| S60 | 50–75% |
| S85 | > 75% |

Os códigos X, Y e Z também aparecem na base; seu significado não foi confirmado.

## Volume conferido

Contagens obtidas no serviço em 4 de novembro de 2026. O retângulo usado (lon −51,1 a −39,8; lat −22,95 a −14,2) envolve Minas Gerais e inclui partes de estados vizinhos.

| Tabela | Brasil | Retângulo de MG | O que mede |
| --- | --- | --- | --- |
| Mineralometria (resultados) | 676.847 resultados | 6.677 amostras | Classes de proporção de minerais |
| Solo | 851.216 resultados | 4.272 amostras | Teores de elementos químicos |
| Sedimento de corrente | — | 35.854 amostras | Teores de elementos químicos |
| Rocha | — | 7.048 amostras | Teores de elementos químicos |
| Concentrado de bateia | — | 7.808 amostras | Teores de elementos químicos |

O projeto do Quadrilátero Ferrífero tem 1.136 amostras de mineralometria. Outros projetos com mineralometria na região incluem Vazante-Paracatu, Serra Negra/Salitre (fosfato), Lítio Fase 2 e Jequitinhonha.

## Ressalvas para o TCC

1. **Não é solo da área de mineração.** A mineralometria vem de sedimento de rio concentrado e representa a bacia a montante do ponto, não o pixel onde foi coletado. A associação natural com o Sentinel-2 seria por bacia de drenagem, e não ponto a pixel; a camada `Drenagem` do dataset do coorientador pode apoiar essa delimitação.
2. **O solo tem química elementar.** Permite prever teores de elementos (Fe, Al, Mn…), que correspondem ao alvo de composição química do TCC (D01). É a tabela mais diretamente útil desta base, por ser de amostra pontual.
3. **Relação com as áreas de mineração.** As áreas de processos minerários da ANM (SIGMINE, já presente no dataset do coorientador) são requeridas pelas empresas. Não foi encontrada base pública com as análises apresentadas nesses processos. A base do SGB é o levantamento público oficial de apoio à prospecção, mas não foi verificado se é usada formalmente para delimitar áreas da ANM.
4. **Datas.** A base é atualizada continuamente, mas cada amostra tem a data da sua análise (por exemplo, 2009 no Quadrilátero Ferrífero).

## Outras fontes encontradas

- [Atlas Geoquímico de Minas Gerais](https://agenciagov.ebc.com.br/noticias/202608/atlas-geoquimico-de-minas-gerais-reune-dados-sobre-a-distribuicao-de-elementos-quimicos-no-solo-agua-e-sedimentos-sgb) (SGB, 2026): cerca de 10 mil amostras de sedimento, solo e água, campo de 2009 a 2013; química elementar.
- [BDSolos e PronaSolos, da Embrapa](https://www.alice.cnptia.embrapa.br/alice/bitstream/doc/1026056/1/2015043.pdf): perfis de solo do país; não foi confirmado se há dados mineralógicos exportáveis.
- [CODEMGE](https://www.agenciaminas.mg.gov.br/noticia/governo-de-minas-passa-a-disponibilizar-levantamentos-aerogeofisicos-do-estado-gratuitamente/): aerogeofísica e mapas geológicos de MG, sem geoquímica de solo.
- [GeoSGB](https://geosgb.sgb.gov.br/geosgb/about_geosgb_en.html): não respondeu durante a pesquisa (conexão recusada).
