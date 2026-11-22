"""Agrupa por elemento os nomes de substâncias da ANM (SUBS) e do SGB.

Uso:
    python -I scripts/agrupar_substancias.py <BRASIL.dbf> <substancias_ocorrencias.json> <saida.csv>

O agrupamento combina três regras, nesta ordem:
1. tabela de minerais-minério e casos especiais (conhecimento mineralógico, revisável);
2. nome normalizado (sem acentos e sem prefixos como "MINÉRIO DE") igual ao de um elemento;
3. fuzzy matching (difflib) de cada palavra contra os nomes dos elementos, com corte em 0,90.
Nomes com fuzzy entre 0,80 e 0,90 ficam como "revisar" e não são agrupados. Com corte
menor, rochas com grafia parecida se confundiam com elementos ("ARENITO" e arsênio,
"CALCÁRIO MAGNESIANO" e magnésio, "TALCO" e tálio).
"""

import collections
import csv
import difflib
import json
import struct
import sys
import unicodedata

# Classe -> símbolo. Metais, metaloides e o silício (decisão do autor, D24).
ELEMENTOS = {
    "Ouro": "Au", "Prata": "Ag", "Platina": "Pt", "Paládio": "Pd", "Ródio": "Rh",
    "Rutênio": "Ru", "Irídio": "Ir", "Ósmio": "Os", "Ferro": "Fe", "Manganês": "Mn",
    "Cobre": "Cu", "Níquel": "Ni", "Cobalto": "Co", "Cromo": "Cr", "Vanádio": "V",
    "Titânio": "Ti", "Zinco": "Zn", "Chumbo": "Pb", "Estanho": "Sn", "Alumínio": "Al",
    "Nióbio": "Nb", "Tântalo": "Ta", "Tungstênio": "W", "Molibdênio": "Mo",
    "Zircônio": "Zr", "Háfnio": "Hf", "Lítio": "Li", "Berílio": "Be", "Magnésio": "Mg",
    "Césio": "Cs", "Rubídio": "Rb", "Terras raras": "ETR", "Urânio": "U", "Tório": "Th",
    "Bismuto": "Bi", "Antimônio": "Sb", "Arsênio": "As", "Mercúrio": "Hg", "Cádmio": "Cd",
    "Gálio": "Ga", "Germânio": "Ge", "Índio": "In", "Tálio": "Tl", "Silício": "Si",
}
# Elementos de terras raras (Sc, Y e lantanídeos) entram na classe "Terras raras".
TERRAS_RARAS = ["Cério", "Lantânio", "Neodímio", "Ítrio", "Escândio", "Praseodímio",
                "Disprósio", "Térbio", "Európio", "Samário", "Gadolínio"]

# Minerais-minério e casos especiais: nome normalizado -> (classe, observação).
MINERAIS = {
    "CASSITERITA": ("Estanho", ""), "ILMENITA": ("Titânio", ""), "RUTILO": ("Titânio", ""),
    "COLUMBITA": ("Nióbio", ""), "TANTALITA": ("Tântalo", ""),
    "TANTALITA-COLUMBITA": ("Tântalo", "mineral de Nb e Ta; classe a decidir"),
    "SCHEELITA": ("Tungstênio", ""), "WOLFRAMITA": ("Tungstênio", ""),
    "BAUXITA": ("Alumínio", ""), "BAUXITA FOSFOROSA": ("Alumínio", "também fosfato; revisar"),
    "CROMITA": ("Cromo", ""), "GALENA": ("Chumbo", ""), "SULFETOS DE CHUMBO": ("Chumbo", ""),
    "HEMATITA": ("Ferro", ""), "MAGNETITA": ("Ferro", ""),
    "ESPODUMENIO": ("Lítio", ""), "PETALITA": ("Lítio", ""), "LEPIDOLITA": ("Lítio", ""),
    "AMBLIGONITA": ("Lítio", ""), "MONAZITA": ("Terras raras", "também Th"),
    "XENOTIMA": ("Terras raras", ""), "ALLANITA": ("Terras raras", "revisar"),
    "ZIRCAO": ("Zircônio", ""), "ZIRCONITA": ("Zircônio", ""), "MOLIBDENITA": ("Molibdênio", ""),
    "SILICATOS DE NIQUEL": ("Níquel", ""), "OURO NATIVO": ("Ouro", ""),
    "MAGNESITA": ("Magnésio", "também refratário industrial; revisar"),
    "SAIS DE MAGNESIO": ("Magnésio", "sais, não minério metálico; revisar"),
    "PIRITA": ("Ferro", "lavrada em geral para enxofre; revisar"),
    "FERRO MANGANES": ("Manganês", "Fe-Mn; classe a decidir"),
    "OURO PIGMENTO": ("Arsênio", "auripigmento, sulfeto de arsênio, não ouro"),
    "QUARTZO": ("Silício", "também gema e uso industrial; revisar"),
    "QUARTZO INDUSTRIAL": ("Silício", "revisar"),
    "QUARTZITO INDUSTRIAL": ("Silício", "rocha; revisar"),
    "ITABIRITO": ("Ferro", "rocha-minério de ferro"),
    "ALUVIAO ESTANIFERO": ("Estanho", ""), "ALUVIAO AURIFERO": ("Ouro", ""),
    "HIDRARGILITA": ("Alumínio", "gibbsita"), "GIBBSITA": ("Alumínio", ""),
    "LIMONITA": ("Ferro", ""), "CANGA": ("Ferro", "crosta ferruginosa"),
    "PIROCLORO": ("Nióbio", ""), "POLUCITA": ("Césio", ""),
    "BERILO": ("Berílio", "também gema (água-marinha, esmeralda); revisar"),
    "TITANITA": ("Titânio", "raramente minério; revisar"),
    "SILICA": ("Silício", "revisar"), "SILEX": (None, "rocha silicosa; fora salvo decisão do autor"),
    "ARGILA ALUMINOSA": (None, "argila; fora salvo decisão do autor"),
    "QUARTZITO": (None, "rocha, uso principal em revestimento; fora salvo decisão do autor"),
    "AREIA QUARTZOSA": (None, "areia; fora salvo decisão do autor"),
}
PREFIXOS = ["MINERIO DE ", "SAIS DE ", "SULFETOS DE ", "SILICATOS DE "]


def norm(s):
    s = unicodedata.normalize("NFKD", s.upper().strip())
    return "".join(c for c in s if not unicodedata.combining(c))


ALVOS = {norm(k): k for k in ELEMENTOS}
ALVOS.update({norm(k): "Terras raras" for k in TERRAS_RARAS})
MIN = {norm(k): v for k, v in MINERAIS.items()}


def classificar(nome):
    n = norm(nome)
    if n in MIN:
        cls, obs = MIN[n]
        return cls, "tabela de minerais", 1.0, obs
    base = n
    for p in PREFIXOS:
        if base.startswith(p):
            base = base[len(p):]
    if base in ALVOS:
        return ALVOS[base], "exato" if base == n else "prefixo", 1.0, ""
    melhor, nota = None, 0.0
    for tok in [base] + base.replace("-", " ").split():
        for alvo, cls in ALVOS.items():
            r = difflib.SequenceMatcher(None, tok, alvo).ratio()
            if r > nota:
                melhor, nota = cls, r
    if nota >= 0.90:
        return melhor, "fuzzy", nota, ""
    if nota >= 0.80:
        return None, "revisar", nota, f"mais próximo: {melhor}"
    return None, "fora", nota, ""


def ler_dbf(caminho, campo):
    with open(caminho, "rb") as f:
        n, hl, rl = struct.unpack("<IHH", f.read(32)[4:12])
        campos = []
        while True:
            d = f.read(32)
            if d[0] == 0x0D:
                break
            campos.append((d[:11].split(b"\0")[0].decode(), d[16]))
        f.seek(hl)
        cont = collections.Counter()
        for _ in range(n):
            r = f.read(rl)
            o = 1
            for nome, tam in campos:
                if nome == campo:
                    cont[r[o:o + tam].decode("utf-8", "replace").strip()] += 1
                o += tam
    return cont


def main(dbf, sgb_json, saida):
    anm = ler_dbf(dbf, "SUBS")
    sgb = collections.Counter(
        x["attributes"]["SUBSTANCIA_MINERAL"]
        for x in json.load(open(sgb_json, encoding="utf-8"))["features"]
        if x["attributes"]["IMPORTANCIA"] == "Principal"
    )
    with open(saida, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["fonte", "nome", "registros", "classe", "simbolo", "regra", "nota", "obs"])
        for fonte, cont in (("ANM", anm), ("SGB", sgb)):
            for nome, q in cont.most_common():
                cls, regra, nota, obs = classificar(nome)
                w.writerow([fonte, nome, q, cls or "", ELEMENTOS.get(cls, ""), regra,
                            f"{nota:.2f}", obs])


if __name__ == "__main__":
    main(*sys.argv[1:4])
