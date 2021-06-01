
import sys
import time

from tkinter.messagebox import *

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import interface_support as IS
from interface_support import *

from Requete import buildQuery, run

#Librairie de notre fonction d'affichage du graphe
from DisplayGraphe import display

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    IS.set_Tk_var()
    top = Interface (root)
    IS.init(root, top)
    root.mainloop()

w = None
def create_Interface(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Interface(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    interface_support.set_Tk_var()
    top = Interface (w)
    interface_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Interface():
    global w
    w.destroy()
    w = None

class Interface:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("715x608")
        top.title("Interface Dataviz")
        top.configure(background="#d9d9d9")
        top.configure(cursor="xterm")

        self.Titre = tk.Label(top)
        self.Titre.place(relx=0.233, rely=0.089, height=40, width=390)
        self.Titre.configure(background="#d9d9d9")
        self.Titre.configure(disabledforeground="#a3a3a3")
        self.Titre.configure(font="-family {8514oem} -size 18")
        self.Titre.configure(foreground="#000000")
        self.Titre.configure(text='''Interface Dataviz''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)
        
        #Fram FILTRE AUTEUR
        self.Filtre_auteur = tk.LabelFrame(top)
        self.Filtre_auteur.place(relx=0.223, rely=0.197, relheight=0.17
                , relwidth=0.507)
        self.Filtre_auteur.configure(relief='groove')
        self.Filtre_auteur.configure(foreground="black")
        self.Filtre_auteur.configure(text='''Filtre Auteur''')
        self.Filtre_auteur.configure(background="#d9d9d9")
        

        #Label Nom Auteur
        self.Nom_auteur = tk.Label(self.Filtre_auteur)
        self.Nom_auteur.place(relx=0.018, rely=0.299, height=17.3, width=75.48
                , bordermode='ignore')
        self.Nom_auteur.configure(background="#d9d9d9")
        self.Nom_auteur.configure(disabledforeground="#a3a3a3")
        self.Nom_auteur.configure(foreground="#000000")
        self.Nom_auteur.configure(text='''Nom Auteur''')
        
        #champ de saisie pour l'auteur
        self.EntryNA = tk.Entry(self.Filtre_auteur, textvariable=IS.nomAut)
        self.EntryNA.place(relx=0.331, rely=0.272, height=24, relwidth=0.504
                , bordermode='ignore')
        self.EntryNA.configure(background="white")
        self.EntryNA.configure(disabledforeground="#a3a3a3")
        self.EntryNA.configure(font="TkFixedFont")
        self.EntryNA.configure(foreground="#000000")
        self.EntryNA.configure(insertbackground="black")
        
        #Label Sur le Nbr min de Publication
        self.Nbr_min_pub = tk.Label(self.Filtre_auteur)
        self.Nbr_min_pub.place(relx=0.018, rely=0.68, height=12, width=114.19
                , bordermode='ignore')
        self.Nbr_min_pub.configure(background="#d9d9d9")
        self.Nbr_min_pub.configure(disabledforeground="#a3a3a3")
        self.Nbr_min_pub.configure(foreground="#000000")
        self.Nbr_min_pub.configure(text='''Nbr min Publication''')
        
        #chanp de sasie sur le nbr Minimal de publication
        self.EntryNMP = tk.Entry(self.Filtre_auteur, textvariable=IS.nbrMinpub)
        self.EntryNMP.place(relx=0.384, rely=0.68, height=17.33, relwidth=0.136
                , bordermode='ignore')
        self.EntryNMP.configure(background="white")
        self.EntryNMP.configure(disabledforeground="#a3a3a3")
        self.EntryNMP.configure(font="TkFixedFont")
        self.EntryNMP.configure(foreground="#000000")
        self.EntryNMP.configure(insertbackground="black")
        
        
        #Fram Filtre Publication
        self.Filtre_Publication = tk.LabelFrame(top)
        self.Filtre_Publication.place(relx=0.112, rely=0.40, relheight=0.3
                , relwidth=0.764)
        self.Filtre_Publication.configure(relief='groove')
        self.Filtre_Publication.configure(foreground="black")
        self.Filtre_Publication.configure(text='''Filtre Publication''')
        self.Filtre_Publication.configure(background="#d9d9d9")
    
        
        #Label Keywords
        self.Keyword = tk.Label(self.Filtre_Publication)
        self.Keyword.place(relx=0.012, rely=0.14, height=32.66, width=74.19
                , bordermode='ignore')
        self.Keyword.configure(background="#d9d9d9")
        self.Keyword.configure(disabledforeground="#a3a3a3")
        self.Keyword.configure(foreground="#000000")
        self.Keyword.configure(text='''Mots Cles''')
        
        
        #Champ de saisie pour Keyword
        self.EntryKey = tk.Entry(self.Filtre_Publication, textvariable=IS.keywords)
        self.EntryKey.place(relx=0.171, rely=0.16, height=24, relwidth=0.346
                , bordermode='ignore')
        self.EntryKey.configure(background="white")
        self.EntryKey.configure(disabledforeground="#a3a3a3")
        self.EntryKey.configure(font="TkFixedFont")
        self.EntryKey.configure(foreground="#000000")
        self.EntryKey.configure(insertbackground="black")

        #Label Categorie
        self.Categorie = tk.Label(self.Filtre_Publication)
        self.Categorie.place(relx=0.012, rely=0.43, height=32.66, width=74.19
                , bordermode='ignore')
        self.Categorie.configure(background="#d9d9d9")
        self.Categorie.configure(disabledforeground="#a3a3a3")
        self.Categorie.configure(foreground="#000000")
        self.Categorie.configure(text='''Categorie''')
        
        #champ de saisie cathegorie
        self.EntryCat = tk.Entry(self.Filtre_Publication, textvariable=IS.categorie)
        self.EntryCat.place(relx=0.171, rely=0.44, height=24, relwidth=0.346
                , bordermode='ignore')
        self.EntryCat.configure(background="white")
        self.EntryCat.configure(disabledforeground="#a3a3a3")
        self.EntryCat.configure(font="TkFixedFont")
        self.EntryCat.configure(foreground="#000000")
        self.EntryCat.configure(insertbackground="black")


        #label Type venue
        self.is_complete = tk.Label(self.Filtre_Publication)
        self.is_complete.place(relx=0.55, rely=0.16, height=20.26, width=120
                , bordermode='ignore')
        self.is_complete.configure(background="#d9d9d9")
        self.is_complete.configure(disabledforeground="#a3a3a3")
        self.is_complete.configure(foreground="#000000")
        self.is_complete.configure(text='''Publication Achevee''')
        
        self.CheckComp = tk.Checkbutton(self.Filtre_Publication, variable =IS.TcheckComp, \
                 onvalue = 1, offvalue = 0)
        self.CheckComp.place(relx=0.81, rely=0.16, bordermode='ignore')
        self.CheckComp.configure(background="#d9d9d9")
        

        #Label Année de publication
        self.Annee = tk.Label(self.Filtre_Publication)
        self.Annee.place(relx=0.56, rely=0.44, height=20.6, width=35.48
                , bordermode='ignore')
        self.Annee.configure(background="#d9d9d9")
        self.Annee.configure(disabledforeground="#a3a3a3")
        self.Annee.configure(foreground="#000000")
        self.Annee.configure(text='''Annee''')
        
        #champ saisie Annee
        self.entryAnnee = ttk.Combobox(self.Filtre_Publication)
        self.entryAnnee.place(relx=0.682, rely=0.44, relheight=0.115
                , relwidth=0.284, bordermode='ignore')
        self.entryAnnee.configure(textvariable=IS.annee)
        self.entryAnnee.configure(takefocus="")
        self.entryAnnee.configure(values=getyears())
        
        
        #Label Affichage
        self.Affichage = tk.Label(self.Filtre_Publication)
        self.Affichage.place(relx=0.56, rely=0.74, height=20.6, width=55.48
                , bordermode='ignore')
        self.Affichage.configure(background="#d9d9d9")
        self.Affichage.configure(disabledforeground="#a3a3a3")
        self.Affichage.configure(foreground="#000000")
        self.Affichage.configure(text='''Affichage''')
        
        #champ selectionné sur affichage
        # On fait le filtre selon la table authors ou Publication
        self.TComboboxAff = ttk.Combobox(self.Filtre_Publication)
        self.TComboboxAff.place(relx=0.682, rely=0.74, relheight=0.115
                , relwidth=0.284, bordermode='ignore')
        self.TComboboxAff.configure(textvariable=IS.comboAff)
        self.TComboboxAff.configure(takefocus="")
        self.TComboboxAff.configure(cursor="fleur")
        self.TComboboxAff.configure(values=["author","publication","keyword"])

        

        #◘Label Co-auteur
        self.Co_auteur = tk.Label(self.Filtre_Publication)
        self.Co_auteur.place(relx=0.024, rely=0.74, height=14, width=80
                , bordermode='ignore')
        self.Co_auteur.configure(background="#d9d9d9")
        self.Co_auteur.configure(disabledforeground="#a3a3a3")
        self.Co_auteur.configure(foreground="#000000")
        self.Co_auteur.configure(text='''Nbr Co-auteur''')
        
        #Label LIMITE
        # self.limite = tk.Label()
        # self.limite.place(relx=0.57, rely=0.80, height=14, width=105
        #         , bordermode='ignore')
        # self.limite.configure(background="#d9d9d9")
        # self.limite.configure(disabledforeground="#a3a3a3")
        # self.limite.configure(foreground="#000000")
        # self.limite.configure(text='''LIMITE DE NOEUD''')
        
         #Champ de saisie Limite
        # self.Entrylim = tk.Entry( textvariable=IS.limite)
        # self.Entrylim.place(relx=0.73, rely=0.80, height=17.33, relwidth=0.08
        #         , bordermode='ignore')
        # self.Entrylim.configure(background="white")
        # self.Entrylim.configure(disabledforeground="#a3a3a3")
        # self.Entrylim.configure(font="TkFixedFont")
        # self.Entrylim.configure(foreground="#000000")
        # self.Entrylim.configure(insertbackground="black")
        
        

        #Champ de saisie Nbr Co-auteur
        self.EntryCoa = tk.Entry(self.Filtre_Publication, textvariable=IS.nbAuthor)
        self.EntryCoa.place(relx=0.18, rely=0.74, height=17.33, relwidth=0.102
                , bordermode='ignore')
        self.EntryCoa.configure(background="white")
        self.EntryCoa.configure(disabledforeground="#a3a3a3")
        self.EntryCoa.configure(font="TkFixedFont")
        self.EntryCoa.configure(foreground="#000000")
        self.EntryCoa.configure(insertbackground="black")
        
        self.Table = tk.LabelFrame(top)
        self.Table.place(relx=0.20, rely=0.72, relheight=0.16
                , relwidth=0.15)
        self.Table.configure(relief='groove')
        self.Table.configure(foreground="black")
        self.Table.configure(text='''Table''')
        self.Table.configure(background="#d9d9d9")
        
        self.CheckAut = tk.Checkbutton(self.Table, variable =IS.TcheckAut, \
                 onvalue = 1, offvalue = 0)
        self.CheckAut.place(relx=0.10, rely=0.16, bordermode='ignore')
        self.CheckAut.configure(background="#d9d9d9")
        
        self.LCheckAut = tk.Label(self.Table)
        self.LCheckAut.place(relx=0.35, rely=0.2, height=14, width=40
                , bordermode='ignore')
        self.LCheckAut.configure(background="#d9d9d9")
        self.LCheckAut.configure(disabledforeground="#a3a3a3")
        self.LCheckAut.configure(foreground="#000000")
        self.LCheckAut.configure(text='''Auteur''')
        
        self.CheckPub = tk.Checkbutton(self.Table, variable =IS.TcheckPub, \
                 onvalue = 1, offvalue = 0)
        self.CheckPub.place(relx=0.10, rely=0.34, bordermode='ignore')
        self.CheckPub.configure(background="#d9d9d9")
        
        self.LCheckPub = tk.Label(self.Table)
        self.LCheckPub.place(relx=0.35, rely=0.40, height=14, width=60
                , bordermode='ignore')
        self.LCheckPub.configure(background="#d9d9d9")
        self.LCheckPub.configure(disabledforeground="#a3a3a3")
        self.LCheckPub.configure(foreground="#000000")
        self.LCheckPub.configure(text='''Publication''')
        
        self.CheckKey = tk.Checkbutton(self.Table, variable =IS.TcheckKey, \
                 onvalue = 1, offvalue = 0)
        self.CheckKey.place(relx=0.10, rely=0.53, bordermode='ignore')
        self.CheckKey.configure(background="#d9d9d9")
        
        self.LCheckKey = tk.Label(self.Table)
        self.LCheckKey.place(relx=0.33, rely=0.58, height=14, width=60
                , bordermode='ignore')
        self.LCheckKey.configure(background="#d9d9d9")
        self.LCheckKey.configure(disabledforeground="#a3a3a3")
        self.LCheckKey.configure(foreground="#000000")
        self.LCheckKey.configure(text='''Mots Cles''')
        
        self.CheckAnn = tk.Checkbutton(self.Table, variable =IS.TcheckAnn, \
                 onvalue = 1, offvalue = 0)
        self.CheckAnn.place(relx=0.10, rely=0.72, bordermode='ignore')
        self.CheckAnn.configure(background="#d9d9d9")
        
        self.LCheckAnn = tk.Label(self.Table)
        self.LCheckAnn.place(relx=0.33, rely=0.75, height=14, width=40
                , bordermode='ignore')
        self.LCheckAnn.configure(background="#d9d9d9")
        self.LCheckAnn.configure(disabledforeground="#a3a3a3")
        self.LCheckAnn.configure(foreground="#000000")
        self.LCheckAnn.configure(text='''Annee''')
        
        self.scale = tk.Scale(root, orient='horizontal', from_=0, to=500,
        resolution=1, tickinterval=50, length=350,label="                                 LIMITE DE NOEUD"
        ,variable =IS.limite)      
        self.scale.place(relx=0.45, rely=0.73, height=100, width=320, bordermode='ignore')
        self.scale.configure(background="#d9d9d9")
        

        #bouton recherche qui point vers la fonction getElement()
        self.ButtonRecherche = tk.Button(top, command=getElement)
        self.ButtonRecherche.place(relx=0.466, rely=0.926, height=28, width=76.13)
        self.ButtonRecherche.configure(activebackground="#ececec")
        self.ButtonRecherche.configure(activeforeground="#000000")
        self.ButtonRecherche.configure(background="#d9d9d9")
        self.ButtonRecherche.configure(disabledforeground="#a3a3a3")
        self.ButtonRecherche.configure(foreground="#000000")
        self.ButtonRecherche.configure(highlightbackground="#d9d9d9")
        self.ButtonRecherche.configure(highlightcolor="black")
        self.ButtonRecherche.configure(pady="0")
        self.ButtonRecherche.configure(text='''Recherche''')
    
#fonction des recuperation des éléments

def getElement(*args):
   #showinfo("Alerte", IS.comboAff.get()) # message de teste 
   var1=IS.nomAut.get() # get the name of author
   var2=IS.nbrMinpub.get() # get number min of article
   var3=IS.keywords.get() # get the keys
   var4=IS.categorie.get() # name of categorie
   var5=IS.annee.get()
   var6=IS.nbAuthor.get()
   var7=IS.comboAff.get()
   var8 = IS.TcheckComp.get()
   
   var9 = IS.TcheckAut.get()
   var10 = IS.TcheckPub.get()
   var11 = IS.TcheckKey.get()
   var12 = IS.TcheckAnn.get()
   var13 = IS.limite.get()
   #print(str(IS.DisplayNomAuth.get()), str(IS.DisplayIdAuth.get()))
   #stockage des variables dans dictionnaire, plus simple
   monDict = {}
   if var1 != "" : monDict["name_author"] = "'"+var1+"'"
   if var2 != 0 : monDict["nbr_publication"] = var2
   if var3 != "" : monDict["keyword"] = "'"+var3+"'"
   if var4 != "" : monDict["categorie"] = "'"+var4+"'"
   if var5 != "" : monDict["year"] = var5
   if var6 != 0 : monDict["nbr_authors"] = var6
   monDict["is_complete"] = var8
   param = 0
   for key,value in monDict.items():
       
       if(isinstance(value,int) and value !=0):
           param +=1
       elif(isinstance(value,str) and value !=""):
           param +=1
       
   displayDict = {
       "zeroParam" : param,
       "affichage" : var7,
       "limite" : var13
       }
   #print(monDict.get("nomAuth"))
   tableDict = {
       "author" : var9,
       "publication" : var10,
       "keyword" : var11, 
       "year" : var12, 
       }   
   start_time = time.time()
   #Preparation de la requete 
   requete = buildQuery(monDict, displayDict, tableDict)
   if("name_author" in monDict and displayDict["zeroParam"]==1 ):
       nomnoeudcentral = monDict["name_author"]
   elif("keyword" in monDict and displayDict["zeroParam"]==1):
       nomnoeudcentral = monDict["keyword"]
   elif("year" in monDict and displayDict["zeroParam"]==1):
       nomnoeudcentral = monDict["year"]
   else:
       nomnoeudcentral = requete 
   #execution de la requete
   result = run(monDict,displayDict,tableDict,requete)
   print( "Le temps pris pour la requete est de : " + str(time.time() - start_time))
   
   print(result)                  
   start_time = time.time()
   display(nomnoeudcentral,result);
   print( "Le temps pris pour l'affichage du graphe' est de : " + str(time.time() - start_time))
   
def getyears():
     i = 1900
     tab = []
     while i < 2021:
         tab.append(i)
         i += 1
         
     return tab
if __name__ == '__main__':
    vp_start_gui()





