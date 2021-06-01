# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 11:32:15 2020

@author: eleou

Version : 2.0.1
"""
import tkinter
import pandas as pd
import dataframe_sql as ds
from dataframe_sql import query
from DisplayGraphe import display

def buildQuery(filtreDict, displayDict, tableDict):
    
    if(tableDict["author"]==1 and tableDict["publication"]==0):
       columns = "name_author,nbr_publication"
    elif(tableDict["author"]==1 and tableDict["publication"]==1):
       columns = "name_author,nbr_publication,date_pub,categorie,nbr_authors,article_title"
       if(tableDict["year"]==1):
           columns += ",year"
    elif(tableDict["author"]==0 and tableDict["publication"]==1):
       columns = "date_pub,categorie,nbr_authors,article_title"
       if(tableDict["year"]==1):
           columns += ",year"
    elif(tableDict["author"]==0 and tableDict["publication"]==0):
        columns="*"
    if (tableDict["keyword"]==1):
           columns= "date_pub,article_title,id_publication"
           if(displayDict["affichage"]=="author"):
            columns= "name_author,id_publication"   
    if (displayDict["affichage"]=="author" and (tableDict["author"]==1 or tableDict["publication"]==1) and tableDict["keyword"]==0):
           columns += ",id_publication"
    if (displayDict["affichage"]=="keyword" and (tableDict["author"]==1 or tableDict["publication"]==1) and tableDict["keyword"]==0):
           columns += ",id_publication"                                        
    
    print("Preparation de la requete")
    requete = "SELECT DISTINCT "
    requete += columns
    premierId = 0
    
    #Ajout des table pour la close from de la requete

    requete += " FROM table"
        
    if(displayDict["zeroParam"]==0 or (displayDict["zeroParam"]==1 and tableDict["keyword"]==1)):
       if(displayDict["limite"]!=0 and displayDict["affichage"]!="author" and tableDict["keyword"]==0):
         requete+= " LIMIT {0}".format(displayDict["limite"])
       print("la requete est " + requete)
       return requete
        
    requete += " WHERE "
    
    premierFiltre = 0
        
    for key, value in filtreDict.items():
        if (premierFiltre != 0 and value != "" and value != 0 and key !="keyword"):
            requete+= " AND "
            
        if (key =="nbr_authors" and value !=0):
            filtre = key + " >= " + str(value)
            requete += filtre
            premierFiltre=1
            
        elif (key =="nbr_publication" and value !=0):
            filtre = key + " >= " + str(value)
            requete += filtre
            premierFiltre=1
        
        elif (key =="keyword"):
            pass             
        
        else:
            if(value != "" and value !=0 and key!= "keyword"):
             filtre = key + " = " + str(value)
             requete += filtre
             premierFiltre=1
      
    if(displayDict["limite"]!=0 and displayDict["affichage"]!="author" and tableDict["keyword"]==0):
           requete+= " LIMIT {0}".format(displayDict["limite"])
           
    print("la requete est " + requete)
    return requete       

        
def run(FiltreDict,displayDict,tableDict,querys):
    #Ouverture des fichiers nécéssaires a l'execution
    
    print("Execution de la requete")
    
    if((displayDict["affichage"]=="" or displayDict["affichage"]=="publication") and tableDict["keyword"]==0):
        result = query(querys)
        
        
    elif(displayDict["affichage"]=="author" and tableDict["keyword"]==0):
        requete = query(querys)
        id_requete = requete["id_publication"]
        dfnA = query("SELECT DISTINCT name_author,id_publication FROM table")
        dfnA = dfnA[dfnA.id_publication.isin(id_requete)].reset_index(drop=True)
        dfnA = dfnA.drop(columns=["id_publication"])
        if(displayDict["limite"]!=0):
            result = dfnA[0:displayDict["limite"]]
        else:
            result = dfnA 
    
    elif(tableDict["keyword"]==1 and displayDict["affichage"]!="keyword"):
        requete = query(querys)
        dfkeyword = query("SELECT DISTINCT id_publication FROM keywordt where keyword = "+FiltreDict["keyword"])
        dfkeyword = dfkeyword["id_publication"]
        requete = requete[requete.id_publication.isin(dfkeyword)].reset_index(drop=True)
        requete = requete.drop(columns=["id_publication"])
        if(displayDict["limite"]!=0):
          result = requete[0:displayDict["limite"]]
        else:
            result = requete
            
    elif(displayDict["affichage"]=="keyword" and tableDict["keyword"]==0):
        requete = query(querys)
        id_requete = requete["id_publication"]
        dfky = query("SELECT DISTINCT keyword,id_publication FROM keywordt")
        dfky = dfky[dfky.id_publication.isin(id_requete)].reset_index(drop=True)
        dfky = dfky.drop(columns=["id_publication"])
        if(displayDict["limite"]!=0):
            result = dfky[0:displayDict["limite"]]
        else:
            result = dfky
    elif(displayDict["affichage"]=="keyword" and tableDict["keyword"]==1):
        dfky = query("SELECT DISTINCT keyword,id_publication FROM keywordt")
        id_requete = query("SELECT DISTINCT id_publication FROM keywordt where keyword = "+FiltreDict["keyword"])
        id_requete = id_requete["id_publication"]
        dfky = dfky[dfky.id_publication.isin(id_requete)].reset_index(drop=True)
        dfky = dfky.drop(columns=["id_publication"])
        if(displayDict["limite"]!=0):
            result = dfky[0:displayDict["limite"]]
        else:
            result = dfky
        
    return result
    

  
 
          
   
 
    
             
