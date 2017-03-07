import pylab
from networkx import nx
import matplotlib.pyplot as plt
import networkx.algorithms.clique as cl

'''
Программа принимает матрицу смежности, строит на её основе граф,
находит максимальную клику, рисует граф, раскрашивая вершины и пути , входящие в максимальную клику,
в зелёный цвет, а остальные в красный
'''

class MatrixFormatError(Exception):
    '''Ошибка отвечающая за правильное указание матрицы'''
    def __str__(self, ex):
        return 'Не верная матрица: {}'.format(ex)

def check_matrix(matrix, lenght):
    for i in range(lenght):
        if(matrix[i][i] != 0):
            raise MatrixFormatError('элементы не должны иметь пути от самих себя')
    for i in range(lenght):
        for j in range(lenght):
            if(matrix[i][j] != matrix[j][i]):
                raise MatrixFormatError('введен ориентированный граф')

def Graf_create(matrix):
    '''
    Принимет матрицу связности и на её основе строит граф,
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
        if(max_len_clique <= len(i)):
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

    check_matrix(graph_matrix, len(a))

    graph = Graf_create(graph_matrix)
    clique_max = Graf_max_clique(graph)

    #задание цвета вершинам
    color_node=[]
    for i in range(len(a) * len(a) - 1):
        if i in clique_max:
            color_node.append('g')
        else:
            color_node.append('r')

    #задание цвета путям
    edge_in_clique = []
    color_edge = []
    for i in clique_max:
        for j in clique_max:
            edge_in_clique.append((i, j))
    for i,j in graph.edges_iter():
        if(i,j) in edge_in_clique:
            color_edge.append('g')
        else:
            color_edge.append('r')

    nx.draw_shell(
                  graph,
                  node_color = color_node,
                  width = 2,
                  with_labels = True,
                  edge_color = color_edge
                 )
    pylab.show()