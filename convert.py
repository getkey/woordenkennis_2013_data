#!/usr/bin/env python3

from itertools import zip_longest

def convert(filename):
    with open(filename, encoding='utf-8') as f:
        # first, we split into pages, each page is separated by \f
        pages = f.read().split('\f')

    # then we split each page in columns, each column is separated by \n\n
    pages = [page.split('\n\n') for page in pages]

    # then we split each column in lines, each line is separated by \n
    pages = [[col.split('\n') for col in page] for page in pages]

    for page in pages:
        # we print the first line of each column, then the second line, etc

        lol = zip_longest(*page)
        kek = [list(col) for col in lol]

        # we print
        for i, col in enumerate(kek):
            for ligne in col:
                if ligne != "" and ligne != None:
                    print(ligne, end='\t')
            print()

convert("./Woordenkennis_van_Nederlanders_en_Vlamingen_anno_2013.txt")
