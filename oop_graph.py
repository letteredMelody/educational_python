class Node:
    def __init__(self, value='', neigbs=[]):
        self.value = value
        self.neigbs = neigbs


class Graph:
    def __init__(self, nodes: list[Node]):
        self.nodes = nodes
        self.matrix = self._build_adjacency_matrix(nodes)

    def _build_adjacency_matrix(self, nodes: Node):
        matrix = []
        for node in nodes:
            line = []
            for index in range(len(nodes)):
                if index == nodes.index(node):
                    line.append(1)
                elif index in node.neigbs:
                    line.append(1)
                else:
                    line.append(0)
            matrix.append(line)
        return matrix

    @property
    def adjacency_matrix(self):
        return self.matrix

    def print_adjacency_matrix(self):
        matrix = self.adjacency_matrix
        for line in matrix:
            print(f'{line}'.replace(',', '').replace('[', '').replace(']', ''))

    def get_node(self, index):
        return self.nodes[index]

    def is_connected(self, node_1: Node, node_2: Node):
        return self.nodes.index(node_1) in node_2.neigbs

    def is_connected_by_id(self, index_1, index_2):
        return index_1 in self.nodes[index_2].neigbs

nodes = [
    Node(value='123', neigbs=[1, 2]),
    Node(value='13', neigbs=[0]),
    Node(value='321', neigbs=[0]),
]

graph = Graph(nodes)

#print(graph.adjacency_matrix)
#graph.print_adjacency_matrix()

node_1 = graph.get_node(0)
node_2 = graph.get_node(1)
node_3 = graph.get_node(2)

print(graph.is_connected(node_1, node_2))
print(graph.is_connected_by_id(1, 2))
