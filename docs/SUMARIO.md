# Sumário da documentação

<!-- markdownlint-disable-file MD013 -->

Gerado por `scripts/docs_sumario.py`; não edite à mão. Leia o trecho com Read (offset/limit).

## ABNT.md — Regras de escrita e revisão do TCC

- `1-53` Regras de escrita e revisão do TCC
  - `5-13` Norma ABNT verificada
  - `15-30` Preferências editoriais do autor
  - `32-45` Convenções do projeto
  - `47-53` Como usar na revisão

## README.md — tcc-tabpfn

- `1-19` tcc-tabpfn
  - `5-19` Mapa do repositório

## docs/PADRAO-DOCS.md — Padrão dos docs

- `1-85` Padrão dos docs
  - `5-29` Dono de cada assunto
  - `31-36` Antes de documentar
  - `38-46` Decisões
  - `48-61` Drift
  - `63-68` Estrutura de um arquivo
  - `70-85` Sumário

## docs/artigos.md — Estudos do capítulo 3

- `1-60` Estudos do capítulo 3
  - `7-49` Estudos selecionados
    - `9-13` 1. Franca-Rocha et al. (2025) — prospectividade de ferro com Sentinel-2
    - `15-19` 2. Yang, Huang e Lu (2026) — classificação com TabPFN e Sentinel-2
    - `21-25` 3. Kutzke, Eichstaedt e Kahnt (2022) — diversos alvos geoquímicos
    - `27-31` 4. Zhang et al. (2023) — integração orbital e geoquímica
    - `33-37` 5. Chen et al. (2026) — TabPFN com Sentinel-2
    - `39-43` 6. Barkov et al. (2026) — bibliotecas harmonizadas
    - `45-49` 7. Huang et al. (2026) — teste externo
  - `52-60` Busca

## docs/dados/catalogo-global.md — Datasets para o datalake geoquímico e mineral

- `1-169` Datasets para o datalake geoquímico e mineral
  - `9-31` Inventário e prioridade
  - `33-46` Onde estão os dados
  - `48-60` Três classes que não podem ser misturadas
    - `50-52` A. Alvos quantitativos de geoquímica
    - `54-56` B. Ocorrências e depósitos
    - `58-60` C. Dados auxiliares ou amostras limitadas
  - `62-83` Schema canônico recomendado
  - `85-103` Protocolo para regiões nunca vistas
  - `105-121` Candidatos não baixados
  - `123-129` Aquisição, licenças e limitações
  - `131-169` Suporte espacial dos datasets de outros países
    - `135-139` Por que o tipo de amostra importa
    - `141-155` Classificação dos datasets
    - `157-163` Constatações
    - `165-169` Pendências

## docs/dados/dataset-brasil.md — Dataset do Brasil

- `1-75` Dataset do Brasil
  - `5-24` Conteúdo
  - `26-31` O que os rótulos informam
  - `33-41` Dados espectrais de satélite em tabela
  - `43-57` Bibliotecas espectrais
  - `59-65` Lacunas
  - `67-75` Qualidade

## docs/dados/fontes-brasil.md — Datasets brasileiros de áreas de exploração mineral

- `1-159` Datasets brasileiros de áreas de exploração mineral
  - `7-11` Resultado
  - `13-24` Comparação das bases da ANM
  - `26-60` SIGMINE
    - `40-52` Referência espacial
    - `54-60` Downloads
  - `62-72` Limitação conceitual: processo minerário não é necessariamente uma mina em operação
  - `74-78` Obtenção de uma latitude e longitude por área
  - `80-84` SIGBM como base georreferenciada complementar
  - `86-97` Fontes oficiais
  - `99-159` Base de Dados Geoquímica do SGB
    - `103-112` Fonte encontrada
    - `114-131` Mineralometria: vários minerais por amostra
    - `133-145` Volume conferido
    - `147-152` Ressalvas para o TCC
    - `154-159` Outras fontes encontradas

## docs/decisoes-historico.md — Histórico das decisões do TCC

- `1-89` Histórico das decisões do TCC

## docs/decisoes-projeto.md — Registro de decisões, ideias e pendências do TCC

- `1-96` Registro de decisões, ideias e pendências do TCC
  - `5-11` Finalidade e uso
  - `13-39` Escopo registrado
  - `41-51` Distinções que devem ser preservadas no texto
  - `53-57` Fundamentação e limites dos artigos discutidos
  - `59-66` Pendências antes de fechar a metodologia
  - `68-74` Abrangência mineral e alternativa de terras raras
  - `76-84` Organização dos trabalhos e extensão multimodal opcional
  - `86-92` Organização editorial e obtenção das fontes
  - `94-96` Conferência final

## docs/fluxo-dados.md — Fluxo dos dados

- `1-136` Fluxo dos dados
  - `5-60` Diagrama
  - `62-73` O que cada base faz
  - `75-123` Exemplo: classificação com mais de um minério
    - `77-88` Dados de treino
    - `90-102` Saída do modelo para locais novos
    - `104-113` Avaliação
    - `115-123` Classes com poucos exemplos
  - `125-136` Exemplo: predição química

## docs/proposta-sinonimos-subs.md — Proposta de agrupamento das substâncias (D24)

- `1-100` Proposta de agrupamento das substâncias (D24)
  - `5-10` Resumo
  - `12-22` Limite de classes do TabPFN-3.5
  - `24-32` Método
  - `34-76` Classes propostas
  - `78-90` Para o autor decidir
  - `92-100` Reprodução

## docs/terminologia.md — Terminologia e observações de fonte

- `1-72` Terminologia e observações de fonte
  - `5-11` Yang, Huang e Lu (2026) — seção 3.2
  - `13-21` Kutzke, Eichstaedt e Kahnt (2022) — seção 3.3
  - `23-72` Capítulo 2 — Revisão Bibliográfica
    - `27-56` Observações sobre a proposta
    - `58-68` Conferência das fontes antes pendentes
    - `70-72` Redução das referências

## scripts/README.md — Scripts

- `1-45` Scripts
  - `7-12` Arquivos
  - `14-34` Execução
  - `36-45` Como funciona

## Fora do escopo

- `.claude/agents/claude-docs-auditor.md` — Auditor de docs
- `.claude/agents/claude-docs-reviewer.md` — Revisor de docs
- `.claude/agents/claude-docs-writer.md` — Documentador
- `.claude/agents/conversor-artigos.md` — Campos abaixo são usados pelo Claude Code; outras ferramentas podem ignorá-los.
- `AGENTS.md` — Instruções para agentes
- `CLAUDE.md` — (sem título)
- `docs/arquivo/ORGANIZACAO_TCC.md` — Plano de implementação da organização do TCC
- `docs/arquivo/avaliacao-introducao.md` — Pontos de revisão da introdução
- `docs/arquivo/cronograma-tcc1.md` — Cronograma de escrita do projeto
- `docs/arquivo/proposta-revisao-bibliografica.md` — 2 REVISÃO BIBLIOGRÁFICA
- `docs/arquivo/proposta-tarefas-integradas.md` — Proposta: litologia e composição química do solo na mesma base
- `docs/arquivo/topicos.md` — Ordem de escrita do trabalho
- `fontes/README.md` — Fontes para consulta
- `fontes/normas/README.md` — Normas ABNT para consulta
- `fontes/normas/nbr-10520-2023.md` — ABNT NBR 10520:2023
- `fontes/normas/nbr-14724-2024.md` — ABNT NBR 14724:2024
- `fontes/normas/nbr-6023-2025.md` — ABNT NBR 6023:2025
- `fontes/noticias/g1-terras-raras-2026-07-11.md` — Brasil tem 2ª maior reserva de terras raras do mundo, mas só 1% da produção global
- `fontes/noticias/jornal-hora-extra-minerais-criticos.md` — Brasil cria política para ampliar produção de minerais críticos
- `tcc/markdown/01-introducao.md` — 1 INTRODUÇÃO
- `tcc/markdown/02-revisao-bibliografica.md` — 2 REVISÃO BIBLIOGRÁFICA
- `tcc/markdown/03-trabalhos-relacionados.md` — 3 TRABALHOS RELACIONADOS
- `tcc/markdown/04-metodologia.md` — 4 METODOLOGIA
- `tcc/markdown/05-cronograma.md` — 5 CRONOGRAMA
- `tcc/markdown/06-consideracoes-finais.md` — 6 CONSIDERAÇÕES FINAIS

## Pastas locais (fora do git)

Existem só no checkout principal, ficam fora do git e não entram neste sumário:
`datasets/` (um `README.md` por pasta), as cópias locais de `fontes/revisao-bibliografica/`
e os PDFs de `fontes/normas/`.
