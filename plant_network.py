import csv
import networkx as nx
from operator import itemgetter
import community
from networkx.readwrite import json_graph
import json
import os
import os.path

def getEdges(filename):
    with open(filename, 'r') as nodecsv:
        nodereader = csv.reader(nodecsv)
        edges = [tuple(e[2:]) for e in nodereader][1:]
        return edges

def getAggregatedEdgesAndRoles(edges):
    dic = {}
    roles = set()
    for x in edges:
        if (x[0], x[1]) in dic.keys():
            dic[(x[0], x[1])] = int(x[2])+ int(dic[(x[0], x[1])])
        else:
            dic[(x[0], x[1])] = int(x[2])
        roles.add(x[0])
        roles.add(x[1])
    aggregatedEdges = []
    for k, v in dic.items():
        aggregatedEdges.append((k[0], k[1], v))
    return aggregatedEdges , roles

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

region_edges = {}
roles_set = set()
for k,v in files.items():
    region_file_name = k + '_edges'
    file_name = os.path.join(dir,v)
    edges = getEdges(file_name)
    aggregatedEdges, roles = getAggregatedEdgesAndRoles(edges)
    region_edges[region_file_name] = aggregatedEdges
    roles_set |= roles


graphs = {}
for k, v in region_edges.items():
    k  = k.replace('_edges','')
    graph = nx.Graph()
    graph.add_nodes_from(roles_set)
    graph.add_weighted_edges_from(v)
    print("for Graph ", k, nx.info(graph))
    print('---------------------------------------------')
    graphs[k] = graph


print(graphs)