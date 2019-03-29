import csv
import networkx as nx
from operator import itemgetter
import community
from networkx.readwrite import json_graph
import json
import os
import os.path

def getNodes(filename):
    with open(filename, 'r') as nodecsv:
        nodereader = csv.reader(nodecsv)
        edges = [tuple(e[2:]) for e in nodereader][1:]
        return edges

dir = 'I:\Data Science Lab\LERs Data for Network Construction'
files = {
    'region_1_old':'region_1_old.csv',
'region_2_old':'region_2_old.csv',
'region_3_old':'region_3_old.csv',
'region_4_old':'region_4_old.csv',
'region_1_new':'region_1_new.csv',
'region_2_new':'region_2_new.csv',
'region_3_new':'region_3_new.csv',
'region_4_new':'region_4_new.csv'

}

roles = set()
temp = []
edges = []
for k,v in files.items():
    file_name = os.path.join(dir,v)
    edges = getNodes(file_name)
    #temp.append(x[0],x[1] for x in edges)
    for x in edges:
        roles.add(x[0])
        roles.add(x[1])
roles = list(roles)



graph = nx.Graph()
graph.add_nodes_from(roles)
print(nx.info(graph))
