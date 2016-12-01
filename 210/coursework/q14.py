#Solution must be OOP
class Graph:
    '''Graph class contains methods to manipulate and store graph

    Allows addition of nodes/edges to the graph. Stores in a
    dictionary using the adjacency list approach'''

    def __init__(self, adjacencyList = {}):
        self.adjacencyList = adjacencyList

    def add_edge(self, start, to):
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

    def bfs(self, start, target):
        '''Searches the graph breadth first looking for the shortest path to a node

        Accepts any value as an argument to attempt to search for'''
        queue = self.adjacencyList[start]
        path = [start]
        visited = set([start])

        while (len(queue) > 0):
            node = queue.pop(0)
            edges = self.adjacencyList[node]

            if node in visited:
                continue
            visited.add(node)

            if (node == target):
                return path
            else:
                path.append(node)
                queue.extend(edges)

    def dfs(self, start, target):
        '''Searches the graph depth first looking for the shortest path to a node

        Accepts any value as an argument to attempt to search for'''
        queue = self.adjacencyList[start]
        path = [start]
        visited = set([start])

        while (len(queue) > 0):
            node = queue.pop() 
            edges = self.adjacencyList[node] 
            if node in visited:
                continue
            visited.add(node)

            if (node == target):
                return path
            else:
                path.append(node)
                queue.extend(edges)

class Node:
    def __init__(self, value):
        '''On initialisation, gives a value to the node'''
        self.value = value

if __name__ == '__main__':
    g = Graph(
            {
                0: [1,3],
                1: [0,2],
                2: [1,3],
                3: [0,2]
                }
    )
    g.display_nodes()

    print(g.dfs(0, 3))
    print(g.bfs(0,3))
