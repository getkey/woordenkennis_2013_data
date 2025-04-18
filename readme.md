1. [Download data](https://biblio.ugent.be/publication/4268774)
2. `pdftotext Woordenkennis_van_Nederlanders_en_Vlamingen_anno_2013.pdf`
3. The first, 290th and 750th page are all mixed up and needs to be fixed manually
4. `./convert.py | awk 'NF > 1' > result.tsv`
