import csv
import networkx as nx
from operator import itemgetter
import community


with open('quakers_nodelist.csv', 'r') as nodecsv:
    #Read the CSV file
    nodereader = csv.reader(nodecsv)
    #Retrieve the data
    #print(nodereader)
    nodes = [n for n in nodereader][1:]
    print(nodes)
    node_names = [n[0] for n in nodes]
    print(len(node_names))


with open('quakers_edgelist.csv','r') as edgecsv:
    #Read the CSV file
    edgereader = csv.reader(edgecsv)
    edges = [tuple(e) for e in edgereader][1:]
    print('\n')
    print(len(edges))
    #print(edges)


G = nx.Graph()
G.add_nodes_from(node_names)
G.add_edges_from(edges)
print(nx.info(G))

historical_sig_dic = {}
gender_dic = {}
birth_dic = {}
death_dic = {}
id_dic = {}


for node in nodes:
    historical_sig_dic[node[0]] = node[1]
    gender_dic[node[0]] = node[2]
    birth_dic[node[0]] = node[3]
    death_dic[node[0]] = node[4]
    id_dic[node[0]] = node[5]


nx.set_node_attributes(G,historical_sig_dic, 'Historical Significance')
nx.set_node_attributes(G, gender_dic, 'Gender')
nx.set_node_attributes(G, birth_dic, 'Birth_Year')
nx.set_node_attributes(G, death_dic, 'Death_Year')
nx.set_node_attributes(G, id_dic, 'ID')

#print(nx.info(G))

for node in G.nodes():
    print(node, G.node[node]['Birth_Year'])