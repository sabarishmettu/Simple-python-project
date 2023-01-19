#importing the required libraries
import networkx as nx 
import matplotlib.pyplot as plt 

#creating a graph with five nodes
G = nx.Graph() 
G.add_nodes_from([1,2,3,4,5]) 

#adding edges with weights
G.add_edge(1,2,weight=2) 
G.add_edge(1,3,weight=3) 
G.add_edge(2,3,weight=1) 
G.add_edge(2,4,weight=2) 
G.add_edge(3,4,weight=1) 
G.add_edge(3,5,weight=2) 
G.add_edge(4,5,weight=3) 

#calculating shortest path using dijkstra algorithm
dijkstra_shortest_path = nx.dijkstra_path(G, 1, 5) 
  
#printing the shortest path
print("The shortest path between the five countries is: ", dijkstra_shortest_path)
