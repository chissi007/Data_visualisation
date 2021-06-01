Readme du projet de data visualisation du groupe TD2.

Fonctions du projet : 

	- Saisie de filtres pour executer des requêtes sur un jeu de données DBLP
	- Construction d'une requête type SQL à partir des filtres
	- Execution de la requête et récupération du résultat sous forme d'un dataframe
	- Visualisation du résultat sous forme d'un graphe.

Mise en place pour le fonctionnement du programme : 
	
	1 : Telecharger les fichiers du programmes, à savoir :  AddTable.py, DisplayGraphe.py, Interface.py et interface_support.py

	2 : Importer les modules nécéssaires au fonctionnement du programme(le detail des différentes librairie est donnée plus bas)

	3 : Ouvrir le fichier AddTable.py et modifier le chemin d'accès vers les fichiers du dataset pour les lignes 12 à 18 inclues(Veillez à respecter l'écriture des noms de fichiers, c'est sensible à la casse)

	4 : Ouvrir le fichier Interface.py et cliquer sur le bouton d'éxecution ou bien sur le raccourci clavier(ctrl+entrée pour spyder)

Fonctionnement du programme : 

	Le programme récupère les données entrées dans l'interface et construit une requete type SQL(SELECT<les données qui vont être retourné> FROM <les fichiers consultés pour recuperer les données> WHERE <Les conditions>) grace à la méthode "buildQuery()". 

	Ensuite, la méthode "run()" execute la requete et retourne le résultat sous forme d'un dataframe.

	Enfin, la méthode "display()" récupère le dataframe et construit le graphe et l'affiche dans un navigateur.

Utilisation de l'interface : 

	- Toutes les cellules de saisie permettent d'appliquer des filtres sur la requête(clause "WHERE") par exemple, si vous entrez un nom d'auteur dans la cellule prévue à cet effet, le programme retournera les informations liées à cet auteur. Il est possibles d'appliquer plusieurs filtres sur une même requête, si il y a un lien entre les données le resultat s'affichera, sinon, c'est que le programme n'a trouvé aucun lien. 

	- Les cases à cocher permettent de saisir les tables desquelles vous désirez avoir des informations(clause "FROM") c'est à dire les fichiers qui seront consultés(Les fichiers de jointures sont automatiquement ajoutés)

	- Les cellules dans le carré du haut sont destinées aux informations relatives aux auteurs, celles du bas sont destinées aux publications, leurs titres, mots clés, années de publication, etc...

	- Le bouton "Recherche" permet de valider les filtres et de lancer la requête. 

	Exemple d'utilisation : 

	user : "Je veux les publications rédigées l'auteur A Min Tjoa et qui ont pour mot clé VISION"

	requête sql : "SELECT * FROM publication, pub_aut, authors WHERE name_author = 'A Min Tjoa' AND keyword = 'VISION"

	il faut entrer le nom de l'auteur dans la cellule "nom_auteur", saisir le mot clé dans la case du même nom, cocher la case publication et cliquer sur le bouton rechercher, le programme fait le nécéssaire pour l'affichage du graphe.

	Une fois le graphe affiché, pour avoir des informations, il suffit de placer le curseur de la souris, ensuite une cellule contenant les informations relative au noeud(une des ligne du resultat de la requete) apparait.

	ATTENTION : Les valeurs des filtres sont sensibles à la casse, les noms d'auteurs ont une majuscule. 

Description des méthodes et librairies utilisées : 

	les librairies : 

		- IHM(Interface homme machine) : TKinter, TKinter.ttk, tkinter.messagebox. Ces librairies ont étées choisies pour leur
		rapidité de prise en main afin de réaliser notre interface simplement.

		- Importation des fichiers : pandas, cette librairie permet la manipulation de fichiers au format csv, excel ou encore des dataframes. Nous l'avons utilisés pour ouvrir les fichiers csv, et importer des échantillons de données grâce à la méthode "read_csv" qui prend en paramètre un chemin d'accès vers un fichier.
		Il faut au préalable prendre connaissance du type de séparateur utilisé dans les fichiers car il est nécéssaire de le transmettre dans l'appel de la méthode. De plus, bien prendre en note les noms des "headers" si vous voulez manipuler les données car ils sont sensibles à la casse. 

		- Manipulation des fichiers/données : dataframe_sql, elle permet d'effectuer des requêtes de type sql sur les fichiers et de retourner les resultats sous forme d'un dataframe.
		Nous avons utilisés les méthodes suivantes :
			- query("SELECT ... FROM ... WHERE") execute la requete
			- remove_temp_table(), register_temp_table(), drop() permettent la manipulation de tables afin d'optimiser les données pour des soucis de performance. 

	Les fonctions importantes du programme : 

		- getElement()(dans le fichier interface.py) : 
		C'est la méthode qui s'execute lors de la pression sur le bouton recherche de l'interface. Elle récupère les données saisies dans l'interface, les enregistres dans des dictionnaires pour plus de facilité à les transmettre aux autres fonctions. 

		- buildQuery(monDict, displayDict, tableDict)(Dans le fichier Requete.py) : Cette fonction prend en paramètre 3 dictionnaires, le premier contient les filtres à appliquer sur la requête, le second prend les noms de fichiers qui seront requis et le dernier contient les limites de resultats ou si il y a ou non des filtres à appliquer. La fonction retourne la requête au format sql sous forme d'une chaine de caractères.

		- run(monDict, displayDict, tableDict, requete)(Requete.py) : prend les 3 mêmes dictionnaires que la fonction précédente pour les informations nécéssaire à la librairie dataframe_sql. Elle prend aussi la requête construite en amon et l'execute. Elle retourne un dataframe contenant le resultat.

		- Display(monNoeudCentral, result)(DisplayGraphe.py) : Cette dernière fonction prend en paramètre les informations concernant le noeud central(base de la requete) ainsi que le dataframe resultat de la requête. La fonction construit les noeuds, les connexions avec le noeud central et affiche le graphe dans un navigateur. 