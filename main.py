import graphviz


def read(name_file):
    return [list(map(int, line.strip().split())) for line in open(name_file, 'r')]


def visual(m):
    graph = graphviz.Graph()
    [graph.node(str(node))
     for node in set(range(1, len(m) + 1)) - set([j + 1 for i in range(len(m))
                                                  for j in range(i + 1, len(m)) if m[i][j] != 0])]
    [graph.edge(str(i + 1), str(j + 1), label=str(m[i][j]))
     for i in range(len(m)) for j in range(i + 1, len(m)) if m[i][j] != 0]
    graph.view()


# Checking for connectivity using theorem

def graph_con(m):
    return len(m) > 1 and len([m[i][j] for i in range(len(m))
                               for j in range(i + 1, len(m)) if m[i][j] != 0]) > (len(m) - 1) * (len(m) - 2) // 2


adj_matrix = read('file.txt')
visual(adj_matrix)
print("Graph is connected!") if graph_con(adj_matrix) else print("Graph is not connected!")
