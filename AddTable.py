# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 03:43:36 2020

@author: Mansour Lo
"""

import pandas as pd
import dataframe_sql as ds
import time

start_time = time.time()
publication=pd.read_csv("C:/Users/Mansour Lo/Desktop/M1 INFO/Projet Integré/dataset1/publication.csv",encoding='latin1')
author = pd.read_csv("C:/Users/Mansour Lo/Desktop/M1 INFO/Projet Integré/dataset1/author.csv",encoding='latin1')
pub_aut=pd.read_csv("C:/Users/Mansour Lo/Desktop/M1 INFO/Projet Integré/dataset1/publication_author.csv",encoding='latin1')
pub_yrs = pd.read_csv("C:/Users/Mansour Lo/Desktop/M1 INFO/Projet Integré/dataset1/publication_year.csv",encoding='latin1')
keyword=pd.read_csv("C:/Users/Mansour Lo/Desktop/M1 INFO/Projet Integré/dataset1/Publication_keywords.csv",encoding='latin1')
year=pd.read_csv("C:/Users/Mansour Lo/Desktop/M1 INFO/Projet Integré/dataset1/year.csv",encoding='latin1')


ds.register_temp_table(author, "author")
ds.register_temp_table(publication, "publication")
ds.register_temp_table(pub_aut, "pub_aut")
ds.register_temp_table(pub_yrs, "pub_yrs")
ds.register_temp_table(keyword, "keywordt")
ds.register_temp_table(year, "year")

  
table = ds.query("SELECT * FROM author INNER JOIN pub_aut ON author.id_author = pub_aut.id_author")
table = table.drop(columns=["author.id_author","pub_aut.id_author"])
ds.register_temp_table(table,"fusautid_aut")
ds.remove_temp_table("author")
ds.remove_temp_table("pub_aut")



table = ds.query("SELECT * FROM year INNER JOIN pub_yrs ON year.id_year = pub_yrs.id_year")
table = table.drop(columns=["year.id_year","pub_yrs.id_year"])
ds.register_temp_table(table,"fusyrsid_yrs")
ds.remove_temp_table("year") 
ds.remove_temp_table("pub_yrs")



table = ds.query("SELECT * FROM publication INNER JOIN fusyrsid_yrs ON fusyrsid_yrs.id_publication = publication.id_publication")
table = table.drop(columns=["fusyrsid_yrs.id_publication"])
table = table.rename(columns={"publication.id_publication":"id_publication"})
ds.register_temp_table(table,"fuspub1")
ds.remove_temp_table("publication")
ds.remove_temp_table("fusyrsid_yrs")

table = ds.query("SELECT * FROM fusautid_aut INNER JOIN fuspub1 ON fuspub1.id_publication = fusautid_aut.id_publication")
table = table.drop(columns=["fusautid_aut.id_publication"])
table = table.rename(columns={"fusautid_aut.nbr_publication":"nbr_publication","fuspub1.nbr_publication":"nbr_publication_year","fuspub1.id_publication":"id_publication"})
ds.register_temp_table(table,"table")  
ds.remove_temp_table("fuspub1")
ds.remove_temp_table("fusautid_aut")

del publication
del author
del pub_aut
del year
del pub_yrs
del keyword
del table

print( "Le temps pris pour le chargement est de : " + str(time.time() - start_time))

test = ds.query("SELECT * FROM table")
print(test.info())

del test