import csv
import networkx as nx
from operator import itemgetter
import community
from networkx.readwrite import json_graph
import json


with open('quakers_nodelist.csv', 'r') as nodecsv:
    #Read the CSV file
    nodereader = csv.reader(nodecsv)
#    #Retrieve the data
#   #print(nodereader)
    nodes = [n for n in nodereader][1:]
    print(nodes)
    node_names = [n[0] for n in nodes]
    print(len(node_names))


with open('quakers_edgelist.csv', 'r') as edgecsv:
    #Read the CSV file
    edgereader = csv.reader(edgecsv)
    edges = [tuple(e) for e in edgereader][1:]
    print('\n')
    print(len(edges))
#    #print(edges)


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

density = nx.density(G)
print("Network Density is : ", density)

Ann_William_Path = nx.shortest_path(G, source="Anne Camm", target="William Mead")
print("Shortest path between Ann and William", Ann_William_Path)


fell_whitehead_path = nx.shortest_path(G, source="Margaret Fell", target="George Whitehead")
print("Shortest path between Fell and Whitehead", fell_whitehead_path)

#print(nx.diameter(G))

print("Is Graph connected: ", nx.is_connected(G))

components= nx.connected_components(G)
largest_component = max(components, key=len)

subgraph = G.subgraph(largest_component)

print("Diameter for largest component: ", nx.diameter(subgraph))

triadic_closure = nx.transitivity(G)
print("Triadic Closure is ", triadic_closure)

degree_dictionary = dict(G.degree(G.nodes()))
for d in degree_dictionary:
    print(d, degree_dictionary[d])

nx.set_node_attributes(G, degree_dictionary, 'degree')

print(G.node['William Penn'])

sorted_degree_dic = sorted(degree_dictionary.items(), key=itemgetter(1), reverse=True)

print("Getting nodes with top 20 degree")

for node in sorted_degree_dic[:20]:
    print(node)


betweenness_dic = nx.betweenness_centrality(G)
#print(betweenness_dic)
eignevector_dic = nx.eigenvector_centrality(G)

nx.set_node_attributes(G, betweenness_dic, 'betweenness')
nx.set_node_attributes(G, eignevector_dic, 'eigenvector')


sorted_betweenness = sorted(betweenness_dic.items(), key=itemgetter(1), reverse=True)
print("Top 20 nodes with betweenness")

for node in sorted_betweenness[:20]:
    print(node)

top_betweenness = sorted_betweenness[:20]

for b_node in top_betweenness:
    degree = degree_dictionary[b_node[0]]
    print("Name : ", b_node[0], " | Betweenness Centrality : ", b_node[1], " Degree : ", degree)


communities = community.best_partition(G)

for community_ in communities:
    print(community_, communities[community_])

sorted_community = sorted(communities.items(), key=itemgetter(1), reverse=True)

print(sorted_community)

for community_, community_class in sorted_community:
    print(community_, community_class)
#print(communities)
nx.set_node_attributes(G, communities, 'modularity')

#Now let's get the community of class value 2 nodes

community_class_2 = [n for n in G.nodes() if G.node[n]['modularity'] == 2]

#Create a dictionary of eigenvector centrality for those nodes
class_2_eignevector = {n:G.node[n]['eigenvector'] for n in community_class_2}

class_2_sorted_eignevector = sorted(class_2_eignevector.items(), key=itemgetter(1), reverse=True)

print("Modularity class 2 sorted by Eigenvector centrality")
for node in class_2_sorted_eignevector[:5]:
    print("Name : ", node[0], " | Eigenvector_centrality :", node[1])


modularity = {}

for k,v in communities.items():
    if v not in modularity:
        modularity[v] = [k]
    else:
        modularity[v].append(k)

for k,v in modularity.items():
    if len(v)>2:
        print("Class " , str(k), ":", v)


nx.write_gexf(G, "quaker_network.gexf")

data = json_graph.node_link_data(G)
#print(data)

s = json.dumps(data)
#print(s)