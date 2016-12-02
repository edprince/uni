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

    def dijkstra(self, start):
        '''Function finds the cheapest path from a given node to a target
        
        Accepts a valid start value that resides within the weighted graph'''
        unvisited = {node: None for node in self.adjacencyList.keys()}
        visited = {}
        current = start
        currentDistance = 0
        unvisited[current] = currentDistance

        while True:
            for neighbour, weight in self.adjacencyList[current].items():
                if neighbour not in unvisited:
                    continue
                newDistance = currentDistance + weight
                if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                    unvisited[neighbour] = newDistance
            visited[current] = currentDistance
            del unvisited[current]
            if not unvisited: 
                break
            potential_nodes = [node for node in unvisited.items() if node[1]]
            current, currentDistance = sorted(potential_nodes, key = lambda x: x[1])[0]

        return visited

class Node:
    def __init__(self, value):
        '''On initialisation, gives a value to the node'''
        self.value = value

if __name__ == '__main__':
    g = Graph({
    
        'A': {'B': 4, 'C': 3, 'D': 7},
        'B': {'A': 4, 'D': 1, 'F': 4},
        'C': {'A': 3, 'D': 3, 'E': 5},
        'D': {'A': 7, 'B': 1, 'C': 3, 'E': 2, 'F': 2, 'G': 7},
        'E': {'C': 5, 'D': 2, 'G': 2},
        'F': {'B': 4, 'D': 2, 'G': 4},
        'G': {'D': 7, 'E': 2, 'F': 4}
        })

    g.display_nodes()
    print(g.dijkstra('A'))
