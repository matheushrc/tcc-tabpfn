# Plano de implementação da organização do TCC

O Markdown será a fonte principal do conteúdo do TCC. Quando solicitado, a IA escreverá ou atualizará os arquivos LaTeX com base nesses textos, seguindo o template da faculdade disponível em `Template_UFFSTex/`.

A conversão será feita pela IA, sem Pandoc ou outro conversor automático.

## Estrutura proposta

```text
tcc/
├── markdown/
│   ├── 01-introducao.md
│   ├── 02-fundamentacao.md
│   ├── 03-metodologia.md
│   ├── 04-resultados.md
│   └── 05-conclusao.md
└── latex/
    ├── principal.tex
    ├── UFFStex.cls
    ├── bibliografia.bib
    ├── capitulos/
    │   ├── 01-introducao.tex
    │   ├── 02-fundamentacao.tex
    │   ├── 03-metodologia.tex
    │   ├── 04-resultados.tex
    │   └── 05-conclusao.tex
    └── figuras/

Template_UFFSTex/       # template original para consulta
docs/                  # notas e planejamento da pesquisa
datasets/              # dados dos experimentos
```

Os capítulos podem ser ajustados conforme a estrutura exigida para o TCC I ou TCC II. Essa organização é uma proposta; este documento não move os arquivos existentes.

## Nomes dos arquivos de capítulos

Manter a pasta `tcc/latex/capitulos/` e nomear os arquivos com a ordem seguida do nome do capítulo: `01-introducao.tex`, `02-fundamentacao.tex` e assim por diante. Não usar nomes genéricos como `capitulo_1.tex`.

Usar dois dígitos na ordem, letras minúsculas, nomes sem acentos e hífens para separar palavras. O Markdown correspondente terá o mesmo nome-base, como `tcc/markdown/01-introducao.md`.

O prefixo numérico organiza os arquivos. A numeração exibida no texto continua sendo gerada pelo LaTeX, conforme a ordem de inclusão no documento principal:

```latex
\include{capitulos/01-introducao}
\include{capitulos/02-fundamentacao}
\include{capitulos/03-metodologia}
\include{capitulos/04-resultados}
\include{capitulos/05-conclusao}
```

## Localização e uso do template da faculdade

O template original fica na raiz do repositório, na pasta `Template_UFFSTex/`, onde já está atualmente. Essa pasta será preservada como modelo de referência para consultar a classe, os comandos, a formatação e os exemplos fornecidos pela faculdade.

A pasta `tcc/latex/` conterá uma cópia do template adaptada para o TCC. Nela ficarão a classe `UFFStex.cls`, o documento principal `principal.tex`, a bibliografia e os capítulos escritos pela IA a partir dos arquivos Markdown.

```text
raiz/
├── Template_UFFSTex/   # modelo original da faculdade para consulta
└── tcc/
    ├── markdown/      # textos principais do TCC
    └── latex/         # projeto LaTeX do TCC baseado no modelo
```

Ao preparar o projeto LaTeX, a IA deverá copiar os arquivos necessários do template para `tcc/latex/` e adaptar essa cópia com os dados e o conteúdo do trabalho. As atualizações dos capítulos serão feitas em `tcc/latex/capitulos/`. O arquivo `tcc/latex/principal.tex` será o documento de entrada para compilar o TCC e gerar o PDF.

## Fluxo de trabalho

1. Escrever e revisar o conteúdo nos arquivos Markdown.
2. Solicitar à IA a criação ou atualização do capítulo correspondente em LaTeX.
3. A IA consulta o Markdown, o template da faculdade e os arquivos LaTeX existentes para realizar a atualização.
4. Compilar o projeto LaTeX e conferir o PDF, incluindo citações, figuras, tabelas e formatação.
5. Fazer alterações de conteúdo primeiro no Markdown e depois solicitar uma nova atualização do LaTeX.

Exemplo de solicitação:

> Atualize `tcc/latex/capitulos/01-introducao.tex` com base em `tcc/markdown/01-introducao.md`, seguindo o template UFFS. Preserve o conteúdo e as fontes, sem acrescentar informações. Atualize somente os arquivos necessários para esse capítulo.

## Regras propostas para o AGENTS.md

- O Markdown é a fonte principal do conteúdo do TCC.
- Criar ou atualizar a versão LaTeX somente quando solicitado.
- Escrever o LaTeX diretamente a partir do Markdown, sem usar Pandoc ou outro conversor automático.
- Seguir a classe, os comandos e a estrutura do template UFFS disponível em `Template_UFFSTex/`.
- Preservar o template original para consulta e manter o projeto do TCC em `tcc/latex/`.
- Manter os capítulos LaTeX em `tcc/latex/capitulos/`, com nomes no padrão `01-introducao.tex`: ordem antes do nome do capítulo, sem a palavra `capitulo` no nome do arquivo. Usar o mesmo nome-base no Markdown correspondente.
- Preservar o conteúdo, o sentido e as fontes do Markdown, sem inventar informações ou referências.
- Manter as URLs originais completas das fontes no Markdown e cadastrar os dados bibliográficos correspondentes em `bibliografia.bib`.
- Usar o sistema de citações do template, que utiliza `abntex2cite`, e conferir a correspondência entre citações e entradas bibliográficas.
- Deixar a numeração de capítulos e seções para o LaTeX. No Markdown, preferir títulos sem numeração manual e respeitar a hierarquia de capítulos, seções e subseções.
- Ao atualizar um capítulo, preservar os demais e limitar alterações compartilhadas ao que for necessário, como referências bibliográficas ou inclusão do capítulo no documento principal.
- Quando uma revisão do LaTeX exigir alteração de conteúdo, atualizar também o Markdown para manter as versões coerentes.

O `AGENTS.md` atual já contém as regras essenciais de escrita do TCC e as instruções sobre fontes. Na implementação, conferir sua coerência com este plano e evitar duplicar nele explicações extensas.

## Responsabilidade dos documentos da raiz

| Documento | Responsabilidade |
| --- | --- |
| `README.md` | Apresentar o projeto, sua finalidade e orientar o início do trabalho. |
| `tcc.conf` | Centralizar as informações básicas do TCC: título, autor, orientação, curso, instituição, campus, cidade e etapa do trabalho. |
| `ARCHITECTURE.md` | Explicar a organização, as responsabilidades das áreas e as relações entre pesquisa, Markdown, template e LaTeX. |
| `AGENTS.md` | Registrar regras operacionais que a IA precisa seguir, incluindo fontes, preservação do template e atualização do LaTeX sob solicitação. |
| `ORGANIZACAO_TCC.md` | Manter este plano, suas etapas de execução, verificações e exemplos do fluxo de escrita. |

O `ARCHITECTURE.md` deverá ser breve e explicar decisões estáveis, limites e pontos de entrada. O mapa deve permitir localizar onde escrever um capítulo, onde adaptar sua apresentação e onde consultar o modelo original. Essa abordagem se baseia na proposta de [matklad para ARCHITECTURE.md](https://matklad.github.io/2021/02/06/ARCHITECTURE.md.html).

O `tcc.conf` mantém as informações em texto no formato `chave=valor`, sem comandos LaTeX. Os nomes próprios usam capitalização normal, preservando grafia e acentos. Campos vazios indicam informações pendentes; título em inglês, palavras-chave, resumo e abstract serão preenchidos ao final do TCC I. Ao escrever o LaTeX, a IA deverá adaptar esses dados aos comandos e ambientes do template. A classe usa o ano da compilação, que deverá ser conferido com o ano de entrega informado em `tcc.conf`.

Aplicar ao `AGENTS.md` o filtro de descoberta da skill `agents-md-optimizer`: manter decisões operacionais e convenções que não podem ser inferidas com segurança dos arquivos; deixar árvores de diretórios e descrições detalhadas nos documentos de organização. A orientação está discutida por [Addy Osmani](https://addyosmani.com/blog/agents-md/).

## Estado inicial e escopo

Atualmente, o template está em `Template_UFFSTex/`, a introdução em `introducao.md` e as notas de pesquisa em `docs/`. A estrutura `tcc/` apresentada neste plano ainda precisa ser criada; o `ARCHITECTURE.md` também precisa ser escrito.

`introducao.md` contém a introdução atual do autor deste projeto e será a origem de `tcc/markdown/01-introducao.md`.

`introducao.example.md` contém o exemplo de introdução do TCC de Natanael Henrik Zago, outro aluno orientado pelo mesmo professor. O documento de origem está em `docs/Final_UFFS___TCC_1__Natanael_Henrik_Zago_.pdf`. O exemplo e o PDF servem como referência de estrutura e escrita; não são conteúdo autoral deste TCC e não devem ser incorporados como capítulos do trabalho. Essa identificação foi fornecida pelo autor deste projeto.

A implementação consiste em organizar os textos, preparar a cópia do template e documentar o fluxo. Não inclui desenvolver os experimentos, preencher resultados ou escrever capítulos sem conteúdo de referência. A criação dos capítulos LaTeX depende de solicitação explícita, conforme o `AGENTS.md`.

## Etapas de implementação

### 1. Conferir os arquivos e definir a migração

- Ler `introducao.md`, `introducao.example.md`, `tcc.conf`, os documentos relevantes de `docs/` e os arquivos do template.
- Tratar `introducao.md` como o texto principal atual e `introducao.example.md` como exemplo do TCC de Natanael Henrik Zago, cujo PDF está em `docs/Final_UFFS___TCC_1__Natanael_Henrik_Zago_.pdf`. Não tratar o exemplo ou as notas de pesquisa como capítulos aprovados deste TCC.
- Conferir referências locais à introdução antes de movê-la, para atualizar os caminhos afetados.
- Registrar quais capítulos possuem conteúdo e quais ainda precisam ser escritos.

Critério de conclusão: origem e destino dos textos definidos, sem perda de conteúdo e sem promoção de exemplos ou notas a texto final.

### 2. Organizar o conteúdo Markdown

- Criar `tcc/markdown/` e mover a introdução principal para `tcc/markdown/01-introducao.md`, preservando o conteúdo e as URLs.
- Remover a numeração manual dos títulos e ajustar a hierarquia: `#` para capítulo, `##` para seção e `###` para subseção.
- Manter notas em `docs/` e preservar `introducao.example.md` e o PDF de Natanael Henrik Zago como referências, distinguindo-os do texto principal. Não mover o exemplo para `01-introducao.md` nem substituir a introdução atual pelo conteúdo do outro aluno.
- Criar os demais arquivos somente quando houver conteúdo a organizar ou uma solicitação para iniciar sua escrita; os nomes da árvore representam os destinos planejados.
- Atualizar referências ao caminho antigo da introdução nos documentos pertinentes.

Critério de conclusão: introdução disponível no destino previsto, títulos coerentes e fontes preservadas. Nenhuma cópia antiga deve competir com o Markdown principal.

### 3. Preparar o projeto LaTeX quando solicitado

- Criar `tcc/latex/`, `tcc/latex/capitulos/` e `tcc/latex/figuras/`.
- Copiar do template os arquivos necessários, incluindo `UFFStex.cls` e `principal.tex`, preservando `Template_UFFSTex/`.
- Conferir os arquivos auxiliares exigidos pelo template e garantir que o projeto adaptado tenha todas as dependências locais necessárias.
- Adaptar capa e dados institucionais com as informações confirmadas em `tcc.conf`, definido como fonte principal dos dados básicos do TCC. Autor, orientador, coorientador, curso, instituição, campus, cidade e etapa já foram informados. O título em inglês, as palavras-chave, o resumo e o abstract serão preenchidos ao final do TCC I; o ano de entrega ainda precisa ser informado. Campos vazios representam informações pendentes e não devem ser preenchidos por inferência.
- Retirar da cópia os exemplos de capítulos, referências, figuras, apêndices e anexos que não façam parte do trabalho.
- Manter os elementos obrigatórios do template. Resumo e abstract devem ser baseados em textos fornecidos ou escritos a partir de conteúdo confirmado.
- Incluir no documento principal apenas capítulos efetivamente existentes, seguindo a ordem dos prefixos numéricos.

Critério de conclusão: projeto adaptado separado do original, com arquivos locais completos e sem conteúdo fictício apresentado como parte do TCC.

### 4. Escrever a introdução em LaTeX quando solicitado

- Ler o Markdown principal e escrever `tcc/latex/capitulos/01-introducao.tex` diretamente, seguindo os comandos do template.
- Preservar significado, parágrafos, listas e fontes; aplicar apenas as adaptações necessárias à sintaxe e à apresentação.
- Conferir cada fonte citada e cadastrar suas informações confirmadas em `tcc/latex/bibliografia.bib`, preservando a URL original.
- Usar o sistema de citações já adotado pelo template, sem substituir sua configuração por outro sistema.
- Não converter URLs em referências bibliográficas com autores, datas ou títulos inventados. Registrar qualquer informação pendente antes de considerar as referências concluídas.
- Conferir o vínculo entre a introdução e `principal.tex`.

Critério de conclusão: conteúdo correspondente ao Markdown, citações com entradas corretas e capítulo incluído no documento principal.

### 5. Documentar a arquitetura e as regras operacionais

- Criar `ARCHITECTURE.md` com propósito do repo, mapa das áreas, relações entre elas e limites de responsabilidade.
- Explicar nele que Markdown é a origem do conteúdo, que LaTeX é atualizado pela IA sob solicitação e que o template original serve de referência.
- Distinguir estrutura existente de estrutura planejada enquanto a migração estiver incompleta; atualizar essa distinção após cada etapa concluída.
- Revisar `AGENTS.md` com o filtro do optimizer. Preservar todas as regras de citações existentes e as decisões confirmadas pelo usuário.
- Evitar incluir no `AGENTS.md` árvores de arquivos, histórico da conversa, dependências copiadas das configurações ou comandos não verificados.
- Atualizar o `README.md` para orientar a localização dos textos e dos documentos de organização.

Critério de conclusão: cada documento cumpre sua responsabilidade, sem instruções conflitantes e sem descrever funcionalidades planejadas como existentes.

### 6. Verificar a migração e o projeto LaTeX

- Comparar os textos antes e depois da migração, permitindo apenas ajustes intencionais de títulos e caminhos.
- Conferir URLs originais, hierarquia dos títulos e correspondência dos nomes-base entre Markdown e LaTeX.
- Conferir se `Template_UFFSTex/` permaneceu intacto e se os caminhos de inclusão, figuras e bibliografia apontam para arquivos existentes.
- Identificar as ferramentas LaTeX disponíveis e compilar a partir de `tcc/latex/`, usando o processo exigido pelo template, incluindo processamento bibliográfico e passagens adicionais quando necessário.
- Se a compilação local não for possível, informar a limitação e preparar o projeto com seus arquivos locais para revisão no Overleaf; não afirmar que a compilação passou.
- Conferir o PDF: capa, sumário, numeração, acentos, referências, listas, figuras e tabelas. Resolver citações e referências indefinidas.
- Registrar em documentação apenas o comando de compilação efetivamente verificado. Tratar arquivos auxiliares de compilação na configuração do Git sem ocultar os arquivos-fonte do trabalho.

Critério de conclusão: migração conferida e, quando a etapa LaTeX for executada, compilação e revisão visual realizadas ou limitações explicitamente registradas.

## Manutenção após a implementação

Para cada capítulo novo, escrever e revisar primeiro o Markdown. Ao solicitar a versão LaTeX, a IA deverá atualizar o arquivo correspondente, suas referências e os vínculos necessários no documento principal. Revisões de conteúdo originadas na leitura do PDF devem ser aplicadas primeiro ao Markdown.

Quando a ordem dos capítulos mudar, renomear os arquivos Markdown e LaTeX correspondentes e atualizar as inclusões em `principal.tex`. O prefixo dos arquivos organiza o projeto; o LaTeX continua responsável pela numeração exibida no documento.

Atualizar `ARCHITECTURE.md` quando mudarem as responsabilidades ou relações entre áreas. Atualizar `AGENTS.md` quando houver uma nova decisão operacional ou um problema recorrente que exija uma instrução específica.

## Checklist de entrega

- [ ] Introdução migrada e caminhos atualizados.
- [ ] Numeração e hierarquia dos arquivos e títulos conferidas.
- [ ] Template original preservado.
- [ ] Cópia LaTeX preparada, quando solicitada.
- [ ] Introdução LaTeX escrita, quando solicitada.
- [ ] Fontes, citações e bibliografia conferidas.
- [ ] `ARCHITECTURE.md` criado e coerente com a estrutura existente.
- [ ] `AGENTS.md` revisado com regras operacionais concisas.
- [ ] `README.md` atualizado com orientação de navegação.
- [ ] Compilação e revisão do PDF verificadas, quando aplicável, com limitações registradas.

Este checklist registra trabalho futuro. A atualização deste plano não executa a migração, a criação do projeto LaTeX ou a escrita dos capítulos.
