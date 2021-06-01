# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 03:46:21 2020

@author: Mansour Lo
"""
import pandas as pd

def Nettoyagepub_keyword():
    publication= pd.read_csv("C:/Users/Mansour Lo/Desktop/DATASET/publication.csv",encoding='latin1')
    keyword=pd.read_csv("C:/Users/Mansour Lo/Desktop/DATASET/Publication_keywords.csv",encoding='latin1')
    pub_aut=pd.read_csv("C:/Users/Mansour Lo/Desktop/DATASET/publication_author.csv",encoding='latin1')
    pub_yrs = pd.read_csv("C:/Users/Mansour Lo/Desktop/DATASET/publication_year.csv",encoding='latin1')
    
    
    test =  pd.Series(list(set(publication["id_publication"].iloc[0:2000000]).intersection(set(pub_aut["id_publication"].iloc[0:6000000]))))
    test2 = pd.Series(list(set(test).intersection(set(keyword["id_publication"].iloc[0:8000000]))))
    test3 = pd.Series(list(set(test2).intersection(set(pub_yrs["id_publication"].iloc[0:2000000]))))
    publication.set_index('id_publication',inplace=True)
    keyword.set_index('id_publication',inplace=True)
    pub_aut.set_index('id_publication',inplace=True)
    pub_yrs.set_index('id_publication',inplace=True)
    
    aut = pub_aut.loc[test3]
    key = keyword.loc[test3]
    pub = publication.loc[test3]
    yrs = pub_yrs.loc[test3]
    
    
    aut.to_csv('publication_author.csv', sep=',', mode='a')
    key.to_csv('Publication_keywords.csv', sep=',', mode='a')
    pub.to_csv('publication.csv', sep=',', mode='a')
    yrs.to_csv('publication_year.csv', sep=',', mode='a')
    return test3
    
test = Nettoyagepub_keyword()
print(test) 
