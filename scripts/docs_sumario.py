"""Gera o `docs/SUMARIO.md` e confere drift de estados nos docs Markdown.

Uso (na raiz do repositório):

    uv run python scripts/docs_sumario.py            # grava docs/SUMARIO.md
    uv run python scripts/docs_sumario.py --check    # o sumário está em dia?
    uv run python scripts/docs_sumario.py --estados  # palavras de estado fora do registro

Os arquivos vêm de `git ls-files`: pastas ignoradas nunca entram. As regras estão em
`docs/PADRAO-DOCS.md`. Adaptado de `scripts/docs_sumario.py` do projeto api_ai_project
(DevDecisor), em 22 de novembro de 2026.
"""

import argparse
import fnmatch
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

SUMARIO = "docs/SUMARIO.md"
REGISTRO = "docs/decisoes-projeto.md"
HISTORICO = "docs/decisoes-historico.md"
SEM_TITULO = "(sem título)"

# Não entram no sumário: transcrições, exemplos e LaTeX.
IGNORADOS: tuple[str, ...] = (
    "fontes/artigos/**",
    "fontes/artigos-descartados/**",
    "templates/**",
    "Template_UFFSTex/**",
    "tcc/latex/**",
)

# Entram só com o título e não são conferidos por `--estados`.
FORA_DO_ESCOPO: tuple[str, ...] = (
    "tcc/markdown/**",
    "fontes/normas/**",
    "fontes/noticias/**",
    "fontes/README.md",
    "docs/arquivo/**",
    "CLAUDE.md",
    "AGENTS.md",
    ".claude/**",
)

# Palavras de estado que pertencem ao registro de decisões (ver `docs/PADRAO-DOCS.md`).
ESTADOS = re.compile(
    r"\b(pendentes?|finalizad[oa]s?|compilad[oa]s?|aguarda|em andamento|não validad[oa])\b",
    re.IGNORECASE,
)

# Texto fixo do sumário. Quem decide o que é local é o `.gitignore` (o script só lê o
# `git ls-files`); se ele mudar, atualize este texto.
PASTAS_LOCAIS: str = (
    "Existem só no checkout principal, ficam fora do git e não entram neste sumário:\n"
    "`datasets/` (um `README.md` por pasta), as cópias locais de `fontes/revisao-bibliografica/`\n"
    "e os PDFs de `fontes/normas/`."
)

_CERCA = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")
_TITULO = re.compile(r"^ {0,3}(#{1,6})(?:[ \t]+(.*?))?[ \t]*$")
_FECHO_TITULO = re.compile(r"[ \t]+#+[ \t]*$")

_VAZIO = "vazio"
_TEXTO = "texto"
_CODIGO = "codigo"
_TITULO_TIPO = "titulo"
_DIVISOR = "divisor"


@dataclass(frozen=True)
class Secao:
    nivel: int
    titulo: str
    inicio: int
    fim: int


def _linhas(texto: str) -> list[str]:
    """Quebra em linhas sem depender do fim de linha (CRLF, LF ou CR)."""
    linhas = texto.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    if linhas and linhas[-1] == "":
        linhas.pop()
    return linhas


def _classificar(linhas: list[str]) -> list[tuple[str, int, str]]:
    """Dá a cada linha (tipo, nível, título), ignorando o que está em cercas de código."""
    itens: list[tuple[str, int, str]] = []
    cerca: str | None = None
    for linha in linhas:
        if cerca is not None:
            fecho = re.match(rf"^ {{0,3}}{re.escape(cerca[0])}{{{len(cerca)},}}[ \t]*$", linha)
            itens.append((_CODIGO, 0, ""))
            if fecho:
                cerca = None
            continue
        abertura = _CERCA.match(linha)
        if abertura and not (abertura.group(1)[0] == "`" and "`" in abertura.group(2)):
            cerca = abertura.group(1)
            itens.append((_CODIGO, 0, ""))
        elif linha == "---":
            itens.append((_DIVISOR, 0, ""))
        elif not linha.strip():
            itens.append((_VAZIO, 0, ""))
        else:
            titulo = _TITULO.match(linha)
            if titulo and len(titulo.group(1)) <= 4:
                texto = _FECHO_TITULO.sub("", titulo.group(2) or "")
                itens.append((_TITULO_TIPO, len(titulo.group(1)), texto))
            else:
                itens.append((_TEXTO, 0, ""))
    return itens


def ler_secoes(texto: str) -> list[Secao]:
    """Devolve as seções de nível 1 a 4, com as linhas (base 1) de início e de fim."""
    linhas = _linhas(texto)
    itens = _classificar(linhas)
    titulos = [i for i, (tipo, _, _) in enumerate(itens) if tipo == _TITULO_TIPO]
    secoes: list[Secao] = []
    for posicao, i in enumerate(titulos):
        nivel, titulo = itens[i][1], itens[i][2]
        if nivel == 1:
            secoes.append(Secao(nivel, titulo, i + 1, len(linhas)))
            continue
        limite = len(linhas)
        for j in titulos[posicao + 1 :]:
            if itens[j][1] <= nivel:
                limite = j
                break
        fim = i
        divisores = [k for k in range(i + 1, limite) if itens[k][0] == _DIVISOR]
        if divisores:
            fim = divisores[-1]
        else:
            naovazias = [k for k in range(i + 1, limite) if itens[k][0] != _VAZIO]
            fim = naovazias[-1] if naovazias else i
        secoes.append(Secao(nivel, titulo, i + 1, fim + 1))
    return secoes






def _arquivos_versionados(raiz: Path) -> list[str]:
    saida = subprocess.run(
        ["git", "ls-files", "-z"],
        cwd=raiz,
        check=True,
        capture_output=True,
    ).stdout.decode("utf-8")
    caminhos = [c for c in saida.split("\0") if c and (raiz / c).is_file()]
    return sorted(caminhos)


def _fora_do_escopo(caminho: str) -> bool:
    return any(fnmatch.fnmatchcase(caminho, padrao) for padrao in FORA_DO_ESCOPO)


def _ignorado(caminho: str) -> bool:
    return any(fnmatch.fnmatchcase(caminho, padrao) for padrao in IGNORADOS)


def _docs(arquivos: list[str]) -> list[str]:
    return [a for a in arquivos if a.endswith(".md") and a != SUMARIO and not _ignorado(a)]


def _ler(raiz: Path, caminho: str) -> str:
    return (raiz / caminho).read_bytes().decode("utf-8", errors="replace")


def _h1(texto: str) -> str:
    for secao in ler_secoes(texto):
        if secao.nivel == 1:
            return secao.titulo or SEM_TITULO
    return SEM_TITULO




def gerar_sumario(raiz: Path) -> str:
    """Monta o texto do `docs/SUMARIO.md` a partir dos arquivos versionados em `raiz`."""
    arquivos = _arquivos_versionados(raiz)
    docs = _docs(arquivos)
    blocos = [
        "# Sumário da documentação\n\n"
        "<!-- markdownlint-disable-file MD013 -->\n\n"
        "Gerado por `scripts/docs_sumario.py`; não edite à mão. "
        "Leia o trecho com Read (offset/limit).\n"
    ]

    for caminho in (d for d in docs if not _fora_do_escopo(d)):
        texto = _ler(raiz, caminho)
        linhas = [f"## {caminho} — {_h1(texto)}", ""]
        for secao in ler_secoes(texto):
            recuo = "  " * (secao.nivel - 1)
            linhas.append(f"{recuo}- `{secao.inicio}-{secao.fim}` {secao.titulo}")
        blocos.append("\n".join(linhas) + "\n")

    linhas = ["## Fora do escopo", ""]
    for caminho in (d for d in docs if _fora_do_escopo(d)):
        linhas.append(f"- `{caminho}` — {_h1(_ler(raiz, caminho))}")
    blocos.append("\n".join(linhas) + "\n")

    blocos.append(f"## Pastas locais (fora do git)\n\n{PASTAS_LOCAIS}\n")
    return "\n".join(blocos)


def _raiz_do_repositorio() -> Path:
    saida = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        check=True,
        capture_output=True,
    ).stdout.decode("utf-8")
    return Path(saida.strip())


def _gravar(caminho: Path, texto: str) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with open(caminho, "w", encoding="utf-8", newline="\n") as arquivo:
        arquivo.write(texto)


def _verificar(raiz: Path) -> int:
    problemas = 0
    atual = raiz / SUMARIO
    esperado = gerar_sumario(raiz)
    gravado = _ler(raiz, SUMARIO).replace("\r\n", "\n") if atual.is_file() else None
    if gravado != esperado:
        print(f"{SUMARIO}: desatualizado; rode `uv run python scripts/docs_sumario.py`")
        problemas += 1
    return 1 if problemas else 0


def _estados(raiz: Path) -> int:
    """Lista palavras de estado fora do registro; só informa, não falha."""
    arquivos = _arquivos_versionados(raiz)
    for caminho in (d for d in _docs(arquivos) if not _fora_do_escopo(d) and d not in (REGISTRO, HISTORICO)):
        cerca = False
        for numero, linha in enumerate(_linhas(_ler(raiz, caminho)), start=1):
            if _CERCA.match(linha):
                cerca = not cerca
            if not cerca and ESTADOS.search(linha):
                print(f"{caminho}:{numero}: {linha.strip()[:120]}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    grupo = parser.add_mutually_exclusive_group()
    grupo.add_argument(
        "--check",
        action="store_true",
        help="sai com 1 se o sumário estiver desatualizado",
    )
    grupo.add_argument(
        "--estados",
        action="store_true",
        help="lista palavras de estado fora de docs/decisoes-projeto.md (drift)",
    )
    args = parser.parse_args(argv)
    raiz = _raiz_do_repositorio()
    if args.check:
        return _verificar(raiz)
    if args.estados:
        return _estados(raiz)
    _gravar(raiz / SUMARIO, gerar_sumario(raiz))
    return 0


if __name__ == "__main__":
    for fluxo in (sys.stdout, sys.stderr):
        if hasattr(fluxo, "reconfigure"):
            fluxo.reconfigure(errors="replace")
    sys.exit(main())
