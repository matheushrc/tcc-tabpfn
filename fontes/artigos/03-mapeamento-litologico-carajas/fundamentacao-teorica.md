# Leitura orientada — Costa, Tavares e Oliveira

**Situação:** leitura e redação pelo autor pendentes.

## Roteiro de leitura — sugestões da IA

**Organização deste arquivo:** mantenha o roteiro, as observações sobre a revisão e as propostas da IA, quando solicitadas, antes de “Anotações do autor”. Essa última seção fica no fim do arquivo para permitir a continuidade da escrita sem interrupções. A proposta da IA é cumulativa: preserve os trechos aprovados e atualize-a até a conclusão indicada pelo autor; ao final, deixe apenas o subtópico numerado, seu título e o texto consolidado, sem o rótulo de versão da IA, crases, anotações do autor ou seções de apoio, após conferir a incorporação do conteúdo aprovado e de suas fontes.

**Foco:** Mapeamento litológico no Brasil.

**Artigo para consulta:** [Predictive lithological mapping through machine learning methods: a case study in the Cinzento Lineament, Carajás Province, Brazil](https://jgsb.sgb.gov.br/index.php/journal/article/view/63).

**Consulta alternativa:** [PDF no repositório oficial RIGeo](https://rigeo.sgb.gov.br/bitstreams/5886b568-feeb-4456-955e-bdb7852ea011/download). A cópia local está em `artigo.pdf`, e sua conversão está em `artigo.md`.

Este roteiro orienta a leitura e as anotações. A redação da fundamentação teórica e da análise acadêmica será feita pelo autor; os itens abaixo não constituem texto pronto para o TCC.

### Conceitos para você estudar antes de escrever o capítulo 2

- [ ] Mapeamento litológico e fontes dos rótulos geológicos.
- [ ] Magnetometria, radiometria, MVI e SRTM.
- [ ] Random Forest, validação cruzada e uso de coordenadas.

### Seções para ler e perguntas para suas anotações

| Seção ou elemento do artigo | O que procurar e registrar |
| --- | --- |
| 1. Introduction; 2. Geological Framework | Qual dificuldade de mapeamento caracteriza a área e quais unidades são consideradas? |
| 3. Data; figuras 2 e 3 | Quais variáveis entram nos modelos, quais dados são excluídos e de onde vêm os rótulos? |
| 4.1. Evaluation of Machine Learning Algorithms; tabela 2 | Como os modelos são comparados e como a validação é realizada? |
| 4.2. Random Forest Algorithm; tabelas 3 e 4 | Como o número de árvores e a importância dos atributos são avaliados? |
| 5 Results; figura 6; tabelas 5 e 6 | Como são calculadas a recuperação global e as porcentagens por unidade? |
| 6. Discussions; 7 Conclusions | Quais efeitos das coordenadas, do ruído e da referência cartográfica exigem cautela? |

### Perguntas para você preparar a análise do estudo no capítulo 3

- [ ] Concordância com um mapa existente equivale a validação independente de campo?
- [ ] Que diferenças existem entre dados geofísicos e espectros orbitais no seu problema?
- [ ] Como discutir reconhecimento espacial local sem tratá-lo como transferência para outra região?

### Antes de redigir

- [ ] Anotar as páginas, seções, tabelas ou figuras que sustentam cada informação que você pretende usar.
- [ ] Separar o que os autores propõem, executam e demonstram; registrar também os limites da avaliação.
- [ ] Identificar conceitos que exigem consultar as referências originais, preservando suas URLs completas.
- [ ] Redigir com suas palavras, citando as fontes; discutir como o estudo se aproxima e se diferencia das tarefas do seu TCC.

### Observações sobre a revisão

- *Greenfield*: mantido em inglês, como ocorre na literatura geológica em português, para indicar áreas com pouco conhecimento geológico prévio. Um exemplo é o estudo [Análise prospectiva para ouro nas regiões Ouro Roxo-Cantagalo e Chico Torres, Província Mineral do Tapajós](https://www.scielo.br/j/rbg/a/kDdRZQf7pCB5m9rtrdknRSg/?lang=pt), que emprega o termo nesse sentido.
- “Coberturas supergênicas” são materiais formados ou alterados por processos próximos à superfície, como o intemperismo. O termo não se refere às copas das árvores.
- *Contracted* significa “contratados”. O artigo não afirma que o próprio SGB executou todos os levantamentos.

**Complementos para suas anotações:**

- Os mesmos três projetos forneceram dados aerorradiométricos de potássio (K), urânio equivalente (eU) e tório equivalente (eTh). Os autores também usaram uma fatia horizontal do modelo de inversão do vetor de magnetização (MVI), a 100 m de profundidade, e um modelo digital de elevação derivado da missão SRTM. O artigo não informa o portal de obtenção nem a versão do SRTM.
- Para reunir os dados, interpolaram as medições aerogeofísicas em grades de 125 m e ajustaram os dados radiométricos nas áreas em que os projetos se sobrepunham. Depois, colocaram todas as grades no mesmo sistema de coordenadas e em células de 250 m, reunindo os valores de cada localização em uma linha da base.
- Os rótulos das 1.400 amostras de treinamento vieram do mapa geológico existente: 100 amostras aleatórias por unidade litológica. Não eram novas observações de campo.

**Fonte:** [Costa, Tavares e Oliveira — introdução e seção 3, dados](https://rigeo.sgb.gov.br/bitstreams/5886b568-feeb-4456-955e-bdb7852ea011/download).

### Versão proposta pela IA para comparação

```markdown
Os autores propõem o uso de algoritmos de aprendizado de máquina (MLAs) para a criação de novos mapas geológicos em áreas *greenfield* e/ou a melhoria de mapas já criados, utilizando-se de dados de sensoriamento remoto e aerogeofísica, já que a criação desses mapas em áreas tropicais com florestas densas e espessas coberturas supergênicas é desafiadora, pois a exposição das rochas é limitada e o acesso aos afloramentos rochosos pode ser difícil.

Os dados aerogeofísicos que utilizaram para o treinamento do modelo vieram de três projetos contratados pelo Serviço Geológico do Brasil (SGB), sendo eles: Oeste de Carajás, Rio Maria e Tucuruí, nos quais coletaram dados aeromagnéticos, que registram variações no campo magnético da Terra e são muito utilizados em mapeamentos geológicos pelas diferenças de suscetibilidade magnética entre as rochas. Esses mesmos projetos também forneceram dados aerorradiométricos de potássio (K), urânio equivalente (eU) e tório equivalente (eTh). Para os dados magnéticos, os autores utilizaram uma fatia horizontal do modelo de inversão do vetor de magnetização (MVI), a 100 m de profundidade. Também utilizaram um modelo digital de elevação derivado da missão SRTM, mas o artigo não informa de onde ele foi obtido.

Para juntar os dados, os autores interpolaram as medições aerogeofísicas em grades de 125 m, estimando valores entre os locais medidos, e ajustaram os dados radiométricos nas áreas de sobreposição dos projetos para reduzir diferenças entre os levantamentos. Depois, colocaram todas as grades no mesmo sistema de coordenadas, SIRGAS 2000 / UTM zona 22 Sul, e em células de 250 m. Assim, cada localização passou a reunir os valores dos diferentes dados em uma mesma linha da base.
```

### Anotações do autor

Os autores propõem o uso de algoritmos de aprendizado de máquina (MLAs) para a criação de novos mapas geológicos em áreas *greenfield* e/ou a melhoria de mapas já criados, utilizando-se de dados de sensoriamento remoto e aerogeofísica, já que a criação desses mapas em áreas tropicais com florestas densas e espessas coberturas supergênicas é desafiadora, pois a exposição das rochas é limitada e o acesso aos afloramentos rochosos pode ser difícil.

Os dados aerogeofísicos que utilizaram para o treinamento do modelo vieram de três projetos contratados pelo Serviço Geológico do Brasil (SGB), sendo eles: Oeste de Carajás, Rio Maria e Tucuruí, nos quais coletaram dados aeromagnéticos, que registram variações no campo magnético da Terra e são muito utilizados em mapeamentos geológicos pelas diferenças de suscetibilidade magnética entre as rochas. Esses mesmos projetos também forneceram dados aerorradiométricos de potássio (K), urânio equivalente (eU) e tório equivalente (eTh). Para os dados magnéticos, os autores utilizaram uma fatia horizontal do modelo de inversão do vetor de magnetização (MVI), a 100 m de profundidade. Também utilizaram um modelo digital de elevação derivado da missão SRTM, mas o artigo não informa de onde ele foi obtido.

Para juntar os dados, os autores interpolaram as medições aerogeofísicas em grades de 125 m, estimando valores entre os locais medidos, e ajustaram os dados radiométricos nas áreas de sobreposição dos projetos para reduzir diferenças entre os levantamentos. Depois, colocaram todas as grades no mesmo sistema de coordenadas, SIRGAS 2000 / UTM zona 22 Sul, e em células de 250 m. Assim, cada localização passou a reunir os valores dos diferentes dados em uma mesma linha da base.
