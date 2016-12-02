#Solution must be OOP
class Graph:
    '''Graph class contains methods to manipulate and store graph

    Allows addition of nodes/edges to the graph. Stores in a
    dictionary using the adjacency list approach'''

    def __init__(self, adjacencyList = {}):
        self.adjacencyList = adjacencyList

    def add_edge(self, start, to, weight):
        self.adjacencyList[start][to] = weight
         
    def add_vertex(self, value):
        '''Adds a new vertex to the graph.

        Accepts any value as an argument, and makes a node with that
        label'''
        new_node = Node(value)
        self.adjacencyList[value] = {}

    def display_nodes(self):
        '''Displays adjacency list of the graph.'''
        print(self.adjacencyList)

    def dijkstra():
        '''Function finds the cheapest path from a given node to a target'''

class Node:
    def __init__(self, value):
        '''On initialisation, gives a value to the node'''
        self.value = value

if __name__ == '__main__':
    g = Graph({
        'A': {'B': 4, 'C': 2},
        'B': {'A': 2, 'C': 8},
        'C': {'A': 6, 'D': 1},
        'D': {'B': 3, 'C': 1}
        })

    g.display_nodes()
    print(g.dfs(0, 3))
    print(g.bfs(0,3))
