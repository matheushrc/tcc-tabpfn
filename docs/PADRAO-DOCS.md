# Padrão dos docs

Regras que a IA segue ao documentar e que o revisor de docs confere. O `docs/SUMARIO.md` é o índice gerado dos docs vivos: consulte-o antes de procurar um assunto com grep ou de criar um arquivo. As regras de trabalho da IA estão em `AGENTS.md`, e as editoriais, em `ABNT.md`.

## Dono de cada assunto

Cada fato mora em um único doc dono; os outros só apontam para ele.

| Assunto | Doc dono |
| --- | --- |
| Escopo, decisões, pendências e estados (pendente, finalizado, compilado) | `docs/decisoes-projeto.md` |
| Dados básicos do trabalho (título, autor, orientadores) | `tcc.conf` |
| Regras de trabalho da IA | `AGENTS.md` |
| Regras editoriais e normas | `ABNT.md`; transcrições das normas em `fontes/normas/` |
| Mapa do repositório | `README.md` |
| Dados do TCC: inventário, contagens, rótulos e lacunas | `docs/dados/dataset-brasil.md` |
| Bases públicas brasileiras (ANM, SGB): o que oferecem e seus limites | `docs/dados/fontes-brasil.md` |
| Bases de outros países e suporte espacial | `docs/dados/catalogo-global.md` |
| Agrupamento das substâncias da `SUBS` em classes | `docs/proposta-sinonimos-subs.md` |
| Estudos do capítulo 3: motivo da seleção e limites | `docs/artigos.md` |
| Estudos do capítulo 3: pasta, estado da análise e autoria | `fontes/README.md` |
| Traduções e termos técnicos | `docs/terminologia.md` |
| Proposta de metodologia | `fontes/metodologia/metodologia.md` |
| Scripts | `scripts/README.md` |
| Fontes, hashes e contagens dos arquivos de dados | `README.md` de cada pasta em `datasets/` (fora do git) |

`docs/arquivo/` guarda documentos congelados (propostas superadas, levantamentos antigos, o plano de reorganização de outubro). Não são lidos nem atualizados, salvo pedido do autor, e não entram no sumário.

## Antes de documentar

1. Ache o doc dono na tabela acima ou no `docs/SUMARIO.md`.
2. Leia só a seção dona, pelo intervalo de linhas do sumário.
3. Edite essa seção. Não crie um `.md` novo se um dono já cobre o assunto. Um arquivo novo só entra quando nenhum dono cobre o assunto; nesse caso, acrescente-o à tabela acima na mesma alteração e dê `git add` antes de regenerar o sumário.
4. Não copie o fato para outros docs: aponte para o dono.

## Drift

Drift é um doc vivo que contradiz o registro de decisões ou outro doc.

- **Estados só no registro.** Palavras de estado (pendente, finalizado, compilado, aguarda, em andamento) ficam em `docs/decisoes-projeto.md`; os outros docs citam o ID da decisão. A exceção é o estado da análise de cada estudo do capítulo 3, cujo dono é `fontes/README.md`. `uv run python scripts/docs_sumario.py --estados` lista essas palavras fora do registro para conferência.
- **Ao registrar um fato novo:** confira-o contra `docs/decisoes-projeto.md` e contra o doc dono; procure com `git grep` o valor antigo (contagem, caminho, nome, alvo) nos docs vivos e corrija no lugar cada trecho que o fato desmente.
- **Ao mover ou renomear um arquivo:** procure o caminho antigo com `git grep` e atualize as referências dos docs vivos.
- **O que não se corrige:**
  - as entradas do histórico de `docs/decisoes-projeto.md`: decisões anteriores são preservadas, e a substituição é registrada (`AGENTS.md`);
  - as transcrições (`fontes/artigos/**`, `fontes/normas/nbr-*.md`, notícias);
  - `docs/arquivo/`.

  Quando uma linha de decisão vigente ficar desatualizada, marque-a entre colchetes no início, como já se faz em D01 e D18, sem apagar o texto.
- **Fonte de cada fato:** distinga o que o autor decidiu do que a IA sugeriu ou mediu, com data absoluta (`AGENTS.md`).

## Estrutura de um arquivo

- Um H1 por arquivo. A primeira frase diz de que assunto o doc é dono.
- Um tema por seção.
- Aspas retas e links com a URL original completa (`AGENTS.md`).
- Nenhuma credencial, token ou URL temporária de sessão.

## Sumário

`docs/SUMARIO.md` é gerado por `scripts/docs_sumario.py`; não edite à mão.

- Gerar: `uv run python scripts/docs_sumario.py`.
- Conferir se está em dia: `uv run python scripts/docs_sumario.py --check`.

Ficam fora do índice:
- as transcrições e os exemplos: `fontes/artigos/**`, `fontes/artigos-descartados/**`, `templates/**`, `Template_UFFSTex/**`;
- o LaTeX.

Aparecem só com o título:
- os capítulos (`tcc/markdown/**`);
- as normas (`fontes/normas/**`);
- `docs/arquivo/**`;
- `AGENTS.md`, `CLAUDE.md` e `.claude/**`.
