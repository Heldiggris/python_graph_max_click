import pylab
from networkx import nx
import matplotlib.pyplot as plt
import networkx.algorithms.clique as cl

'''
Программа принимает матрицу смежности, строит на её основе граф,
находит максимальную клику, рисует граф, раскрашивая вершины, входящие в максимальную клику,
в зелёный цвет, а остальные в красный
'''

def Graf_create(matrix):
    '''
    Принимет матрицу связности и на её основе строит матрицу,
    возвращает построенный граф
    '''
    graph = nx.Graph()
    graph.add_nodes_from(range(len(matrix)))
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            if(matrix[i][j] == 1):
                graph.add_edge(i, j)
    return graph

def Graf_max_clique(graph):
    '''
    Принимает граф и возвращает максимальную клику
    '''
    clique_max = []
    clique = [i for i in cl.find_cliques(graph)]
    max_len_clique = len(clique[0])
    for i in clique:
        print(i)
        if(max_len_clique <= len(i)):
            print(len(i))
            max_len_clique = len(i)
            clique_max = i
    return clique_max

if __name__ == '__main__':
    graph_matrix = []
    a = list(map(int, input().split()))
    graph_matrix.append(a)
    for i in range(len(a) - 1):
        a = list(map(int, input().split()))
        graph_matrix.append(a)
    graph = Graf_create(graph_matrix)
    clique_max = Graf_max_clique(graph)
    color=[]
    for i in range(len(a) * len(a) - 1):
        if i in clique_max:
            color.append('g')
        else:
            color.append('r')
    nx.draw_shell(graph, node_color=color,width=2, with_labels=True)
    pylab.show()
