# Suporte espacial dos datasets de outros países

Verificação da IA em 4 de novembro de 2026 sobre os datasets de `datasets/` descritos em `docs/datasets.md`. A pergunta do autor foi se eles funcionam como a mineralometria do SGB (`docs/fonte-sgb-geoquimica.md`), ou seja, por sedimento de rio, ou se podem treinar o TabPFN para prever áreas sem rio. São constatações e sugestões, não decisões do autor. Os tipos de amostra foram conferidos nos arquivos locais e nos READMEs de cada pasta.

## Por que o tipo de amostra importa

- **Amostra pontual** (solo, till, rocha aflorante): o valor medido descreve o local da coleta. Pode ser associado ao pixel Sentinel-2 da coordenada, e o modelo treinado pode prever qualquer pixel, inclusive em áreas sem rio.
- **Amostra de bacia** (sedimento de rio ou de lago, concentrado de bateia): o valor resume o material transportado de toda a bacia a montante. Os atributos devem ser agregados por bacia, e a previsão é uma média da bacia, não um valor por pixel. A coleta depende de haver drenagem.
- **Subsuperfície** (furo de sondagem, frente de lavra): o satélite não observa o material amostrado; não serve para treino com reflectância.

## Classificação dos datasets

| Dataset | Tipo de amostra verificado | Suporte | Alvo disponível | Uso para prever áreas sem rio |
| --- | --- | --- | --- | --- |
| GEMAS Ap (Europa) | Solo agrícola superficial, 2.113 sítios, 34 países | Pontual | 52 elementos (água-régia) | **Sim.** Melhor candidato externo; licença CC BY 4.0 |
| SIGÉOM (Québec) | 561.232 registros mistos: códigos 30 (sedimento de corrente, 216.768) e 20 (fundo de lago, 169.538) predominam; há horizontes de solo e frações de till | Misto | Óxidos e elementos | **Parcialmente.** Só o subconjunto de solo e till; os códigos de solo e till precisam ser confirmados no dicionário oficial antes do filtro |
| GEOROC crátons (África, Índia, China) | Rocha total (`WR`), vulcânica, plutônica e metamórfica | Pontual, com coordenadas às vezes em intervalos | Óxidos e elementos | **Com cautela.** A rocha fresca analisada nem sempre corresponde à superfície vista pelo satélite (solo, alteração, vegetação); filtrar coordenadas precisas |
| SACM (EUA) | 22.635 de 29.781 amostras são de furo de sondagem; cerca de 1.600 de afloramento | Majoritariamente subsuperfície | Elementos | **Só o subconjunto de afloramento**, que é pequeno |
| CGS 1:250k (África do Sul) | Sedimento de corrente de primeira ordem, com solo superficial quando necessário, segundo o serviço | Bacia pequena, misto com solo | 3 óxidos e 21 elementos | **Não diretamente.** A tabela não distingue sedimento de solo por amostra |
| NGSA (Austrália) | Sedimento de saída de bacia (TOS 0–10 cm e BOS 60–80 cm), 1.315 sítios em 1.186 bacias | Bacia grande (~5.500 km² por sítio) | 68 elementos | **Não.** Escala continental de bacia |
| GSJ (Japão) | Sedimento fluvial, 3.025 amostras | Bacia | 53 analitos | **Não** |
| CDoGS 0434 e Yukon OF2859 (Canadá) | Sedimento de lago e de corrente; água | Bacia | Elementos | **Não** |
| G-BASE (Reino Unido) | Amostra de sedimento de corrente e de solo urbano | Bacia e pontual | Elementos | **Limitado.** Apenas amostra pública pequena |
| SGB ocorrências, USGS MRDS, MRDS Califórnia, OZMIN | Ocorrências e depósitos minerais | Pontual | Substância ou commodity, sem teor | **Como rótulo de presença**, não de composição; ausência de registro não é negativo |
| MapBiomas SoilData (Brasil) | Perfis de solo com espectro | Pontual | Atributos de solo | **Auxiliar.** Coordenadas `#N/A` nesta cópia |

## Constatações

1. **Nenhum dataset estrangeiro tem proporções de minerais.** Todos trazem teores de elementos ou óxidos. A mineralometria com vários minerais por amostra só foi encontrada na base do SGB, que é de concentrado de bateia e, portanto, de bacia. Isso não é um impedimento: o alvo do TCC é a composição química (D01, esclarecido pelo autor em 4 de novembro de 2026), que todos esses datasets fornecem.
2. **Para prever áreas sem rio, os candidatos são os de amostra pontual de superfície:** GEMAS, o subconjunto de solo e till do SIGÉOM, GEOROC filtrado e o afloramento do SACM. No Brasil, a tabela de solo do SGB (4.272 amostras no retângulo de MG, química elementar) também é pontual.
3. **Não misturar suportes no mesmo treino.** Dados de bacia e dados pontuais medem coisas diferentes; se ambos forem usados, devem formar experimentos separados, com o tipo de amostra registrado (`sample_medium` no schema canônico de `docs/datasets.md`).
4. **Superfície observada.** Em áreas vegetadas, o pixel mostra principalmente a vegetação, não o solo ou a rocha. Para amostras pontuais, a extração deve usar composições de solo exposto ou máscaras de vegetação, como fizeram Chen et al. (2025) com compósitos de solo exposto.
5. **Generalização entre regiões (D06, D07):** os conjuntos pontuais compatíveis entre si são poucos e de meios diferentes (solo agrícola europeu, solo e till canadense, rocha de crátons). Uma comparação justa entre regiões exige o mesmo tipo de amostra, a mesma digestão e o mesmo painel de elementos.

## Pendências

- Confirmar no dicionário oficial do SIGÉOM (`Attributs_echantillons_sediment.xlsx` ou `Echantillons_de_sediments.pdf`) quais códigos correspondem a solo e a till antes de filtrar.
- Verificar a precisão das coordenadas do GEOROC por amostra.
- Definir o painel de elementos ou óxidos comum entre as bases pontuais escolhidas e verificar a compatibilidade de digestão e método.
