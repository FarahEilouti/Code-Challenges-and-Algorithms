class Node:
    def __init__(self, value=None):
        self.value = value
    
    def __str__(self):
        return self.value

class Edge:
    def __init__(self,vertex,weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self,value):
        new_vertex = Node(value)
        self.adj_list[new_vertex] = []
        return new_vertex

    def add_edge(self,node1,node2,weight=0):
        
        if not node1 in self.adj_list.keys():
            return("this node does not exist")

        if not node2 in self.adj_list.keys():
            return("this node does not exist")
        
        edge1 = Edge(node2,weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1,weight)
        self.adj_list[node2].append(edge2)

    def __str__(self):
        output = ''
        for vertex in self.adj_list.keys():
            output+= f'{vertex} ->'
            for edge in self.adj_list[vertex]:
                output+= f'{edge.vertex} ---> '
            output+= '\n'
        return output
    


def bfsOfGraph(graph, value):
    
    node = None
    for n in graph.adj_list.keys():

        if n.value == value:
            node = n

            break

    if node is None:
        return []
    
    #queue to store the nodes 
    queue = []
    visited = set()

    queue.append(node)
    visited.add(node.value)
    values = []

    while queue:
        current_node = queue.pop(0)
        values.append(current_node.value)

        for edge in graph.adj_list[current_node]:
            if edge.vertex.value not in visited:
                queue.append(edge.vertex)
                visited.add(edge.vertex.value)

    return values


if __name__ == "__main__":

    graph1 = Graph()

    a = graph1.add_node("A")
    b = graph1.add_node("B")
    c = graph1.add_node("C")
    d = graph1.add_node("D")

    graph1.add_edge(a,b)
    graph1.add_edge(a,c)
    graph1.add_edge(c,b)
    graph1.add_edge(d,b)
    graph1.add_edge(d,c)

# print(bfsOfGraph(graph1, "A"))  # ["A", "B", "C", "D"]
# print(bfsOfGraph(graph1, "B"))  # ["B", "A", "C", "D"]
# print(bfsOfGraph(graph1, "C"))  # ["C", "A", "B", "D"]