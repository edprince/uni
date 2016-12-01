#Solution must be OOP
class Graph:
    '''Graph class contains methods to manipulate and store graph

    Allows addition of nodes/edges to the graph. Stores in a
    dictionary using the adjacency list approach'''

    def __init__(self):
        self.adjacencyList = {}

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
        visited = []
        found = False
        if target not in self.adjacencyList:
            print('Target does not exist')
        else:
            visited.append(self.adjacencyList[start])
            while visited:
                path = visited.pop(0)
                node = path[-1]

    def dfs(self, start, target):
        '''Searches the graph depth first looking for the shortest path to a node

        Accepts any value as an argument to attempt to search for'''
        visited = set()
        stack = [target]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                stack.extend(set(self.adjacencyList[node]) - visited)
        return visited

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
    g.add_vertex(4)
    g.add_vertex(8)
    g.add_edge(0,1)
    g.add_edge(1,2)
    g.add_edge(2,3)
    g.add_edge(3,4)
    g.add_edge(4,8)
    g.display_nodes()

    print(g.dfs(0, 8))
