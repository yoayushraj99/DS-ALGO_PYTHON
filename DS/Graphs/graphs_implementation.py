class Graph:
    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def add_vertex(self, node):
        if node not in self.adjacent_list.keys():
            self.adjacent_list[node] = []
            self.number_of_nodes += 1
        else:
            return "Node Already exists"

    def add_edge(self, node1, node2):
        # undirectedGraph
        # First check that node1 and node2 is in self.adjacent_list
        dict_node = self.adjacent_list
        if node1 in self.adjacent_list.keys() and node2 in self.adjacent_list.keys():
            if node2 not in dict_node[node1]:
                dict_node[node1].append(node2)
            if node1 not in dict_node[node2]:
                dict_node[node2].append(node1)
        else:
            return "These nodes does not exists."

    def show_connections(self):
        all_nodes = self.adjacent_list.keys()
        for node in all_nodes:
            node_connections = self.adjacent_list[node]
            connections = ""
            for vertex in node_connections:
                connections += vertex + " "
            print(node + "-->" + connections)


graph = Graph()
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_vertex('4')
graph.add_vertex('5')
graph.add_vertex('6')
graph.add_edge('3', '1')
graph.add_edge('3', '4')
graph.add_edge('4', '2')
graph.add_edge('4', '5')
graph.add_edge('1', '2')
graph.add_edge('1', '0')
graph.add_edge('0', '2')
graph.add_edge('6', '5')

graph.show_connections()
# 0-->1 2
# 1-->3 2 0
# 2-->4 1 0
# 3-->1 4
# 4-->3 2 5
# 5-->4 6
# 6-->5
