# Proposta: litologia e composição química do solo na mesma base

Sugestão da IA em 4 de novembro de 2026, ainda **não adotada**. Responde a duas perguntas do autor: se faz sentido especificar “composição química do solo” no título e se é possível fazer classificação litológica e predição da composição química ao mesmo tempo sem aumentar muito o esforço. Adoção, mudança de título ou de escopo dependem do autor e dos orientadores; se adotada, registrar em `docs/decisoes-projeto.md` (D01, D06, D07, D09).

## Título: “composição química do solo”

Sugestão de título: *Avaliação do TabPFN para classificação litológica e predição da composição química do solo a partir de dados espectrais de satélite*.

**A favor:**

- **Precisão:** “composição química” sozinha pode ser de rocha, sedimento ou solo, que são tarefas diferentes.
- **Coerência com o sensor:** em áreas tropicais, o Sentinel-2 observa solo, regolito e vegetação, raramente a rocha fresca.
- **Coerência com os dados pontuais disponíveis:** tabela de solo da Base de Dados Geoquímica do SGB, GEMAS e o subconjunto de solo do SIGÉOM (`docs/datasets-suporte-espacial.md`). Rocha e sedimento de bacia ficariam fora, evitando misturar meios.
- **Apoio na literatura analisada:** Barkov, Chen e Huang avaliam o TabPFN em propriedades do solo.

**Cuidados:**

1. **Profundidade da amostra.** O satélite observa os primeiros milímetros da superfície. O GEMAS Ap é de 0–20 cm; o Atlas Geoquímico de MG descreve solos subsuperficiais, e a tabela de solo do SGB precisa ter a profundidade verificada. Amostras profundas enfraquecem a relação com a reflectância e devem ser tratadas como limitação.
2. **Diferenciação dos trabalhos relacionados.** O diferencial passa a ser: dados espectrais de satélite (não espectroscopia de laboratório), alvos geoquímicos de elementos e óxidos (não carbono ou pH), classificação litológica e generalização entre regiões.
3. **Duas referências diferentes.** Os rótulos litológicos vêm do mapa geológico e o alvo químico vem das análises de solo; a metodologia deve tratá-los como tarefas distintas.

**Alternativa:** “composição química superficial” ou “geoquímica de superfície”, mais abrangente (inclui rocha aflorante e till), porém menos clara.

## Duas tarefas na mesma tabela

Não é possível fazer as duas tarefas sem nenhum esforço adicional, mas é possível compartilhar quase todo o pipeline.

**Etapas compartilhadas:**

- aquisição do Sentinel-2, máscara de nuvens e vegetação e compósitos;
- extração da reflectância nos pontos;
- grupos espaciais e regiões de teste (validação por blocos);
- uso do TabPFN, com `TabPFNClassifier` e `TabPFNRegressor` de mesma interface, sem treinamento demorado nem ajuste de hiperparâmetros.

**Mesmos pontos para os dois alvos.** Cada amostra de solo com coordenada recebe, por junção espacial com `geologia_MG.shp`, também o rótulo litológico do polígono. Resulta uma única tabela com dois alvos:

| ponto | B2 … B12 | unidade litológica (mapa) | Fe | Al | Mn | … |
| --- | --- | --- | --- | --- | --- | --- |

As linhas, os atributos e as partições são os mesmos; mudam apenas a coluna-alvo e a métrica (acurácia ou F1 para litologia; RMSE ou R² para cada elemento ou óxido).

**Esforço que continua adicional:**

- métricas, resultados e discussão para duas tarefas;
- legenda litológica: agrupar as 193 unidades do mapa em poucas classes com significado geológico. O TabPFN tem limite de número de classes (10 de forma nativa na versão 2; conferir na versão adotada);
- generalização entre regiões: para a química, bases de outros países usam elementos comparáveis; para a litologia, cada país tem sua própria legenda cartográfica, e harmonizá-las seria um trabalho à parte.

## Divisão sugerida para manter o trabalho enxuto

| Tarefa | Onde | Validação | Papel no TCC |
| --- | --- | --- | --- |
| Composição química do solo | Minas Gerais e outras regiões com dados pontuais de solo compatíveis | Blocos espaciais e região externa (D06, D07) | Tarefa principal |
| Classificação litológica | Minas Gerais, nos mesmos pontos da química | Blocos ou sub-regiões de MG; concordância com o mapa, não validação de campo | Tarefa complementar |

Nessa divisão, a litologia acrescenta um rótulo, uma métrica e uma seção de resultados; a estimativa de esforço é da IA, não medida. A mudança retira da litologia o teste entre países e, por isso, altera parte do escopo atual.

## Pendências para decidir

- Adotar ou não “do solo” no título.
- Confirmar a profundidade das amostras de solo do SGB em Minas Gerais.
- Definir o agrupamento da legenda litológica e verificar o limite de classes da versão do TabPFN.
- Decidir se a generalização entre regiões ficará restrita à composição química.
