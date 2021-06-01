# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 10:12:14 2020

@author: eleou
"""

# Import packages for data cleaning
import numpy as np
import pandas as pd
import re # For finding specific strings in the text

# Import packages for data visualization
import plotly.offline as py
import plotly.graph_objects as go
import networkx as nx
from plotly.offline import plot

'''
    import plotly_express as px
    from plotly.offline import plot
    fig = px.scatter(...)
    plot(fig)
'''

#import script with pandas dataframe request
#from TestDisplayGraph import return_df

def make_edge(x, y, width):
    return  go.Scatter(x         = x,
                       y         = y,
                       line      = dict(width = width,
                                   color = 'cornflowerblue'),
                       hoverinfo = 'text',
                       #text      = ([text]),
                       mode      = 'lines')

def display(name,dfResult):
    df = dfResult
    # Etape 1 : recuperer les noms de colonnes du dataframe
    # ainsi que la valeur du noeud central qui est le parametre de la fonction
    colonnes = list()
    colonnes = df.columns.tolist()
    centralNode = name
    
    nbNoeuds = len(df)#la taille du dataframe definit le nombre de noeuds
    # Etape 2 : Creation des noeud pour chaque ligne du dataframe
    node_names = [a for a in range(nbNoeuds)] #Les noms des noeuds seront des numéros les infos apparaittront avec le curseur sur un noeud en particulier
    node_weight = 3 #Rendre cette variable constante pour tous les noeuds

    node_list = nx.Graph() #Create empty graph
    node_list.add_node(centralNode, size = 10) #Add central node(author name)

    for i in range(len(node_names)):
        node_list.add_node(node_names[i], size = node_weight) # add node for article
        node_list.add_edge(centralNode, node_names[i], weight = node_weight) #add connection to central node
    
    pos_ = nx.spring_layout(node_list) # generate positions of nodes

    edge_trace = [] # create custom edges
    
    
    for edge in node_list.edges():
        x0, y0 = pos_[edge[0]]
        x1, y1 = pos_[edge[1]]
		
        #data = df[df[colonnes[0]].isin([edge[1]])]
		
        '''
        loc_nbr = df['nbr_authors'].iloc[0] - 1 if df['nbr_authors'].iloc[0] != 1 else 1
        text = "Porticipated on this project with {} other people".format(loc_nbr)
        '''
        current_trace = make_edge(
								[x0, x1, None],
								[y0, y1, None],
								#text,
								width = 0.5
								#width = nodnode_list.edges()[edge]['weight']
								)

        edge_trace.append(current_trace)


    node_trace = go.Scatter(x				= [],
                        	y				= [],
                        	text      		= [],
                        	textposition	= "top center",
                        	textfont_size	=   10,
                        	#hoverinfo		= 'text',
                            hovertemplate  = [],
							mode			= 'markers',
							marker			= dict(color	= [],
                                         		size		= [] ,
                                         		line=dict(
                color='black',
                width=1
            )))
	
    annotations = []
	#create custom nodes
    index = len(df)-1
    
    for node in node_list.nodes():
        text = ""
        for i in range(len(df.columns)):
            text += "<br><b>{0}</b>:{1},".format(df.columns[i],df[colonnes[i]].iloc[index])
        #data = df[df[colonnes[1]].isin([node])]
        hover_text = ""
		
        if(node == centralNode):
            hover_text = tuple(["{0}".format(centralNode)])
            color = tuple(['ivory']) 
            size = tuple([5 * node_list.nodes()[node]['size']])
        else:
            hover_text = tuple([text])
            color = tuple(['cornflowerblue'])
            size = tuple([5 * node_list.nodes()[node]['size']])
		
        x, y = pos_[node]
        node_trace['x'] += tuple([x])
        node_trace['y'] += tuple([y])
        node_trace['marker']['color'] += color
        node_trace['marker']['size'] += size
        texth = tuple([hover_text])
        node_trace['hovertemplate'] += texth
        #node_trace['adtext'] += tuple([hover_text])
        
    #     annotations.append(
 		 # dict(x=x,
    #           	 y=y,
    #             	 #text="<b> " + node + "</b>", # node name that will be displayed
    #               text = "<b> {} </b>".format(node),
    #             	 #xanchor='left',
    #            	 #xshift=10,
    #             	 #font=dict(color='black', size=10),
    #             	 showarrow=False)
    #       )

        layout = go.Layout(
     	paper_bgcolor='rgba(0,0,0,0)', # transparent background
     	plot_bgcolor='rgba(0,0,0,0)', # transparent 2nd background
     	xaxis =  {'showgrid': False, 'zeroline': False}, # no gridlines
     	yaxis = {'showgrid': False, 'zeroline': False}, # no gridlines
		#annotations = annotations,
	)
        index = index - 1
	#create empty figure
    fig = go.Figure(layout = layout)
    fig.update_layout(
    hoverlabel=dict(
        font_size=17,
        font_family="Rockwell",
        bgcolor = "ivory"
        
    )
)

	#add all of traces
    
    for trace in edge_trace:
        fig.add_trace(trace)
	
    fig.add_trace(node_trace)

	#layout customization
    fig.update_layout(showlegend = False)

    fig.update_xaxes(showticklabels = False)
    fig.update_yaxes(showticklabels = False)
    plot(fig)
	#show result
	#fig.show()

#guys, start using two things:
#1. GIT, PLEASE
#2. Proper styling(at least main() and __name__...) 
