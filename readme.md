This is a tool that generates an Anki card deck based on the most known words of the dutch language.

## Setup

1. [Download data](https://biblio.ugent.be/publication/4268774)
2. `pdftotext Woordenkennis_van_Nederlanders_en_Vlamingen_anno_2013.pdf`
3. The first, 290th and 750th page are all mixed up and need to be fixed manually
4. `./convert.py | awk 'NF > 1' > result.tsv`
5. `./anki.py results.tsv anki.txt`
