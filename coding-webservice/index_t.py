#!/usr/bin/env python
# coding: utf-8


import whoosh.fields
import whoosh.index
import whoosh.qparser
import whoosh.analysis
import whoosh.support.charset
import whoosh.scoring
import os
import csv


my_analyzer = whoosh.analysis.LanguageAnalyzer("es") | whoosh.analysis.CharsetFilter(whoosh.support.charset.accent_map)# | whoosh.analysis.NgramFilter(minsize=2, maxsize=4)



schema = whoosh.fields.Schema(
    code = whoosh.fields.ID(stored=True),
    description = whoosh.fields.TEXT(stored=True,analyzer=my_analyzer),
    description_additional = whoosh.fields.TEXT(stored=False,analyzer=my_analyzer)
)


if not os.path.exists("index_t"):
    os.mkdir("index_t")
ix = whoosh.index.create_in("index_t", schema)

writer = ix.writer()


with open('cie-o-t.csv', newline='', encoding="utf-8-sig") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")
    for row in reader:
        writer.add_document(code=row["code"],description=row["description"],description_additional=row["description_additional"])


writer.commit()