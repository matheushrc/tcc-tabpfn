# Proposta de agrupamento das substâncias (D24)

> Proposta da IA, de 22 de novembro de 2026, para revisão do autor. Nada aqui é decisão até ser confirmado e registrado em D24 de `docs/decisoes-projeto.md`.

## Resumo

- O TabPFN-3.5 aceita até 160 classes (limites do modelo em D20 de `docs/decisoes-projeto.md`). O número foi lido na configuração gravada nos pesos, porque a documentação não o informa.
- O agrupamento por elemento resulta em 35 classes, que reúnem 100.447 dos 270.994 processos ativos da ANM. As maiores são ouro (42.757), ferro (13.955), cobre (9.857), manganês (5.555), estanho (5.263), lítio (4.423), silício (3.583), terras raras (3.138), alumínio (2.679) e titânio (2.367).
- O fuzzy matching por caracteres ajudou pouco. Com corte de 0,85, juntava rochas a elementos: "ARENITO" a arsênio, "CALCÁRIO MAGNESIANO" a magnésio. Com corte de 0,90, agrupou só "MINÉRIO DE ARSÊNICO". Os sinônimos se resolvem pelo prefixo e pela tabela de minerais; o fuzzy serve para listar casos a conferir.
- Questões abertas desta proposta (estado em D24): quais nomes formam o silício; os nomes ambíguos; os metais alcalinos e alcalinoterrosos de uso industrial; o tratamento das classes raras.

## Limite de classes do TabPFN-3.5

O relatório técnico do TabPFN-3.5 ([Prior Labs, 2026](https://arxiv.org/abs/2609.17895)), o [README do pacote](https://github.com/PriorLabs/TabPFN) e o [cartão do modelo](https://huggingface.co/Prior-Labs/tabpfn_3_5) não informam um número máximo de classes. O README cita apenas a extensão `many_class` para problemas que "exceed TabPFN's built-in class limit", sem dar o número.

O número está na configuração gravada no próprio arquivo de pesos. Foi lido no cabeçalho dos arquivos `tabpfn-v3.5-20260909.safetensors` e `tabpfn-v3.5-20260909_multiclass.safetensors`, baixados só até o fim do cabeçalho, sem os pesos, do [repositório do modelo](https://huggingface.co/Prior-Labs/tabpfn_3_5). Os dois arquivos trazem `MAX_NUMBER_OF_CLASSES = 160` e `max_num_classes = 160`; os demais limites gravados estão em D20.

No [código do pacote](https://github.com/PriorLabs/TabPFN), versão 10.2.0, a partir do commit `e1a3550` de 20/11/2026, o classificador recusa conjuntos com mais classes que esse valor (`validate_num_classes` em `src/tabpfn/validation.py`). O valor padrão de 10 em `inference_config.py` vale apenas para os modelos v2 e v2.5; a partir da v3, a configuração vem do checkpoint.

O valor não foi conferido na versão 9.2.0 fixada em D20. Como a configuração vem do checkpoint, e não do pacote, os pesos `tabpfn-v3.5-20260909` devem dar o mesmo limite; confirmar ao instalar o pacote no servidor.

Consequência: as cerca de 35 classes propostas abaixo cabem no modelo sem agrupar as raras nem decompor o problema. O limite de 160 é técnico; o relatório não mostra o desempenho com tantas classes. As classes com poucos processos continuam sendo um problema estatístico, não de capacidade do modelo.

## Método

O script `scripts/agrupar_substancias.py` lê a coluna `SUBS` de `datasets/brasil/Areas_Mineracao/BRASIL.dbf` e a coluna `SUBSTANCIA_MINERAL` (somente as substâncias principais) de `datasets/brasil/Ocorrencias_Minerais_SGB/substancias_ocorrencias.json`, e grava um CSV com a classe de cada nome. Para cada nome, as regras são aplicadas nesta ordem:

1. **Tabela de minerais-minério.** Mapeamento escrito à mão a partir de conhecimento mineralógico, como cassiterita → estanho e ilmenita → titânio. Nenhum fuzzy chega a "CASSITERITA" a partir de "ESTANHO".
2. **Nome normalizado.** O nome sem acentos e sem prefixos como "MINÉRIO DE" e "SAIS DE" é comparado com os nomes dos elementos. Os elementos de terras raras (cério, lantânio, ítrio etc.) vão para a classe "Terras raras".
3. **Fuzzy matching.** Cada palavra é comparada com os nomes dos elementos pelo `difflib` (corte em 0,90). Notas entre 0,80 e 0,90 ficam marcadas para revisão e não são agrupadas.

Com corte de 0,85, o fuzzy agrupava errado nomes de rochas parecidos com nomes de elementos: "ARENITO" virava arsênio e "CALCÁRIO MAGNESIANO", magnésio; "TALCO" ficava perto de tálio e "GRANITO", de germânio. Com 0,90, o fuzzy agrupou só "MINÉRIO DE ARSÊNICO". Nesta base, quase todos os sinônimos se resolvem pelo prefixo e pela tabela de minerais. O fuzzy serviu sobretudo para listar os casos a conferir.

## Classes propostas

ANM: processos ativos de cada classe (270.994 no total; 100.447 nas 35 classes abaixo). SGB: ocorrências com a substância como principal. `*` = nome marcado para revisão.

| Classe | Símbolo | ANM | SGB | Nomes da ANM agrupados (processos) |
| --- | --- | ---: | ---: | --- |
| Ouro | Au | 42.757 | 4.222 | MINÉRIO DE OURO (32.029); OURO (10.722); ALUVIÃO AURÍFERO (3); OURO NATIVO (3) |
| Ferro | Fe | 13.955 | 1.712 | MINÉRIO DE FERRO (13.489); FERRO (418); HEMATITA (19); MAGNETITA (13); PIRITA* (10); CANGA (2); LIMONITA (2); ITABIRITO (2) |
| Cobre | Cu | 9.857 | 872 | MINÉRIO DE COBRE (9.630); COBRE (227) |
| Manganês | Mn | 5.555 | 1.218 | MINÉRIO DE MANGANÊS (4.813); MANGANÊS (740); FERRO MANGANÊS* (2) |
| Estanho | Sn | 5.263 | 758 | CASSITERITA (4.530); MINÉRIO DE ESTANHO (592); ESTANHO (140); ALUVIÃO ESTANÍFERO (1) |
| Lítio | Li | 4.423 | 38 | MINÉRIO DE LÍTIO (4.364); ESPODUMÊNIO (40); LÍTIO (9); PETALITA (6); LEPIDOLITA (3); AMBLIGONITA (1) |
| Silício | Si | 3.583 | 789 | QUARTZO* (3.455); QUARTZO INDUSTRIAL* (70); QUARTZITO INDUSTRIAL* (37); MINÉRIO DE SILÍCIO (17); SÍLICA* (4) |
| Terras raras | ETR | 3.138 | 20 | TERRAS RARAS (3.087); MONAZITA* (50); MINÉRIO DE CÉRIO (1) |
| Alumínio | Al | 2.679 | 232 | BAUXITA (1.876); MINÉRIO DE ALUMÍNIO (674); ALUMÍNIO (105); HIDRARGILITA (19); GIBBSITA (3); BAUXITA FOSFOROSA* (2) |
| Titânio | Ti | 2.367 | 270 | ILMENITA (1.237); MINÉRIO DE TITÂNIO (712); RUTILO (296); TITÂNIO (115); TITANITA* (7) |
| Níquel | Ni | 1.406 | 141 | MINÉRIO DE NÍQUEL (1.271); NÍQUEL (132); SILICATOS DE NÍQUEL (3) |
| Berílio | Be | 1.018 | 588 | MINÉRIO DE BERÍLIO (624); BERILO* (373); BERÍLIO (21) |
| Zinco | Zn | 989 | 151 | MINÉRIO DE ZINCO (958); ZINCO (31) |
| Chumbo | Pb | 719 | 231 | MINÉRIO DE CHUMBO (601); CHUMBO (83); GALENA (33); SULFETOS DE CHUMBO (2) |
| Nióbio | Nb | 713 | 157 | MINÉRIO DE NIÓBIO (580); COLUMBITA (113); NIÓBIO (18); PIROCLORO (2) |
| Tântalo | Ta | 661 | 904 | MINÉRIO DE TÂNTALO (460); TANTALITA (158); TÂNTALO (42); TANTALITA-COLUMBITA* (1) |
| Tungstênio | W | 432 | 1.091 | MINÉRIO DE TUNGSTÊNIO (239); SCHEELITA (148); TUNGSTÊNIO (25); WOLFRAMITA (20) |
| Cromo | Cr | 173 | 232 | MINÉRIO DE CROMO (74); CROMITA (69); CROMO (30) |
| Magnésio | Mg | 167 | 54 | MINÉRIO DE MAGNÉSIO (97); MAGNESITA* (64); SAIS DE MAGNÉSIO* (4); MAGNÉSIO (2) |
| Platina | Pt | 155 | 16 | MINÉRIO DE PLATINA (125); PLATINA (30) |
| Zircônio | Zr | 140 | 13 | ZIRCÃO (52); ZIRCÔNIO (47); MINÉRIO DE ZIRCÔNIO (26); ZIRCONITA (15) |
| Vanádio | V | 63 | 9 | MINÉRIO DE VANÁDIO (59); VANÁDIO (4) |
| Prata | Ag | 46 | 12 | PRATA (34); MINÉRIO DE PRATA (12) |
| Molibdênio | Mo | 41 | 43 | MINÉRIO DE MOLIBDÊNIO (20); MOLIBDÊNIO (15); MOLIBDENITA (6) |
| Cobalto | Co | 38 | 3 | MINÉRIO DE COBALTO (38) |
| Paládio | Pd | 32 | 0 | MINÉRIO DE PALÁDIO (18); PALÁDIO (14) |
| Antimônio | Sb | 21 | 7 | MINÉRIO DE ANTIMÔNIO (21) |
| Cádmio | Cd | 15 | 1 | CÁDMIO (11); MINÉRIO DE CÁDMIO (4) |
| Bismuto | Bi | 14 | 8 | MINÉRIO DE BISMUTO (11); BISMUTO (3) |
| Urânio | U | 7 | 84 | MINÉRIO DE URÂNIO (7) |
| Arsênio | As | 6 | 13 | MINÉRIO DE ARSÊNICO (3); ARSÊNIO (2); OURO PIGMENTO (1, auripigmento, sulfeto de arsênio) |
| Césio | Cs | 6 | 0 | MINÉRIO DE CÉSIO (5); POLUCITA (1) |
| Rubídio | Rb | 5 | 0 | MINÉRIO DE RUBÍDIO (5) |
| Háfnio | Hf | 2 | 0 | HÁFNIO (2) |
| Mercúrio | Hg | 1 | 1 | MINÉRIO DE MERCÚRIO (1) |

Tório aparece só no SGB (15 ocorrências) e não tem processo ativo com esse nome; a monazita, mineral de terras raras e tório, foi posta em "Terras raras".

## Para o autor decidir

1. **Silício.** "MINÉRIO DE SILÍCIO" tem 17 processos; quase toda a classe vem de "QUARTZO" (3.455), que inclui quartzo para gema e para uso industrial. Ficaram fora "QUARTZITO" (7.150), "AREIA QUARTZOSA" (113), "SÍLEX" e as variedades gemológicas do SGB (cristal de rocha, quartzo rosa, citrino etc.). Definir quais nomes representam o silício.
2. **Nomes ambíguos marcados com `*`.**
   - "PIRITA": em geral é lavrada para enxofre.
   - "BERILO": também é gema; água-marinha e esmeralda ficaram fora.
   - "MAGNESITA" e "SAIS DE MAGNÉSIO": usos refratário e industrial.
   - "MONAZITA": terras raras e tório.
   - "FERRO MANGANÊS" e "TANTALITA-COLUMBITA": cada um tem dois metais.
   - "BAUXITA FOSFOROSA" e "TITANITA".
3. **Metais alcalinos e alcalinoterrosos de uso industrial.** Bário (barita), estrôncio (celestita), potássio (silvinita, sais), sódio (salgema) e cálcio são metais na química, mas na mineração são substâncias não metálicas. Ficaram fora; incluir só se o autor quiser.
4. **Classes raras.** 14 classes têm menos de 100 processos e 6 têm menos de 10. Cabem no limite do TabPFN-3.5, mas uma classe com poucos polígonos pode faltar em alguns blocos da validação cruzada, e suas métricas serão instáveis. Opções: manter todas; definir um mínimo de processos (por exemplo, 100); ou juntar as raras em "outros metálicos". Os elementos do grupo da platina (platina e paládio) também podem formar uma só classe.
5. **"DADO NÃO CADASTRADO"** (10.522 processos): sem substância, fica fora do rótulo.

## Reprodução

```sh
# na raiz do repositório principal, onde fica datasets/
python -I scripts/agrupar_substancias.py \
  datasets/brasil/Areas_Mineracao/BRASIL.dbf \
  datasets/brasil/Ocorrencias_Minerais_SGB/substancias_ocorrencias.json \
  .cache/sinonimos_subs.csv
```
