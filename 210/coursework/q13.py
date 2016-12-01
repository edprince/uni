#Solution must be OOP
class Graph:
    '''Graph class contains methods to manipulate and store graph

    Allows addition of nodes/edges to the graph. Stores in a
    dictionary using the adjacency list approach'''

    def __init__(self):
        self.adjacencyList = {}

    def add_edge(self, start, to):
    '''Adds edge from a start node to a to node

    accepts any values, if not in graph, will create the nodes
    before creating the edge between them'''
        if start not in self.adjacencyList:
            add_vertex(start)
        if to not in self.adjacencyList:
            add_vertex(to)
        self.adjacencyList[start].append(to)
         
    def add_vertex(self, value):
    '''Adds a new vertex to the graph.

    Accepts any value as an argument, and makes a node with that
    label'''
        new_node = Node(value)
        self.adjacencyList[value] = []

    def display_nodes(self):
    '''Displays adjacency list of the graph.'''
        print(self.adjacencyList)

class Node:
    def __init__(self, value):
    '''On initialisation, gives a value to the node'''
        self.value = value


if __name__ == '__main__':
    g = Graph()
    g.add_vertex(0) 
    g.add_vertex(1)
    g.add_vertex(2)
    g.add_vertex(3)
    g.add_vertex(8)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1,2)
    g.add_edge(1,8)
    g.add_vertex(4)
    g.add_edge(4,8)
    g.display_nodes()
