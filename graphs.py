from collections import deque


class Node:
    def __init__(self, data, neighbours=None):
        if not neighbours:
            neighbours = []
        self.neighbours = neighbours
        self.data = data

class Graph:
    def __init__(self, nodes):
        self.nodes = nodes


# based on bfs
def find_path(graph, start, end):
    queue = deque()
    for n in graph.nodes:
        n.visited = False
    queue.append(start)
    while len(queue):
        n = queue.popleft()
        if n == end:
            return "TAK"
        if not n.visited:
            n.visited = True
            for neigh in n.neighbours:
                queue.append(neigh)
    return "NIE"

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)

n1.neighbours = [n2, n5, n4]
n2.neighbours = [n5, n6]
n4.neighbours = [n5, n2]
n5.neighbours = [n3]


g = Graph([n1, n2, n3, n4, n5])

print(find_path(g, n4, n6))