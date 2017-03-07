import pylab
from networkx import nx
import matplotlib.pyplot as plt

def Graf_create(matrix):
    '''
    Принимет матрицу связности и на её основе строит матрицу,
    возвращает построенные граф
    '''
    graph = nx.Graph()
    graph.add_nodes_from(range(len(matrix)))
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if(matrix[i][j] == 1):
                graph.add_edge(i, j)
    return graph

if __name__ == '__main__':
    graph_1 = nx.Graph()
    graph_matrix = []
    a = list(map(int, input().split()))
    graph_matrix.append(a)
    for i in range(len(a) - 1):
        a = list(map(int, input().split()))
        graph_matrix.append(a)
    nx.draw_shell(Graf_create(graph_matrix))
    pylab.show()
