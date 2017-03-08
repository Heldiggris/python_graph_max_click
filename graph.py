import pylab
from networkx import nx
import matplotlib.pyplot as plt
import networkx.algorithms.clique as cl
import sys
import warnings

'''
Программа принимает матрицу смежности, строит на её основе граф,
находит максимальную клику, рисует граф, раскрашивая вершины и пути , входящие в максимальную клику,
в зелёный цвет, а остальные в красный
'''

warnings.filterwarnings("ignore", category=UserWarning)

class MatrixFormatError(Exception):
    '''Ошибка, отвечающая за правильное указание матрицы'''
    pass

def Matrix_check(matrix, lenght):
    #Не обязательное условие
    # for i in range(lenght):
    #     if(matrix[i][i] != 0):
    #         raise MatrixFormatError('элементы не должны иметь пути от самих себя')
    '''Проверяет матрицу на правильность '''
    for i in range(lenght):
        for j in range(lenght):
            if(matrix[i][j] != matrix[j][i]):
                raise MatrixFormatError
            if(matrix[i][j] != 1 and matrix[i][j] != 0):
                raise MatrixFormatError

def Graph_create(matrix):
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

def Graph_max_clique(graph):
    '''Принимает граф и возвращает все максимальные клики'''
    clique_max_all = []
    clique = [i for i in cl.find_cliques(graph)]
    max_len_clique = len(clique[0])
    for i in clique:
        if(max_len_clique <= len(i)):
            max_len_clique = len(i)
    for i in clique:
        if(max_len_clique ==len(i)):
            clique_max_all.append(i)
    return clique_max_all

if __name__ == '__main__':
    try:
        graph_matrix = []
        a = list(map(int, input().split()))
        graph_matrix.append(a)
        for i in range(len(a) - 1):
            a = list(map(int, input().split()))
            graph_matrix.append(a)

        Matrix_check(graph_matrix, len(a))

        graph = Graph_create(graph_matrix)
        clique_max_all = Graph_max_clique(graph)
        clique_max = clique_max_all[0]

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

        plt.hold(False)
        nx.draw_shell(
                      graph,
                      node_color = color_node,
                      width = 2,
                      with_labels = True,
                      edge_color = color_edge
                     )

        clique_max_all_str = ''
        for i in clique_max_all:
            if (clique_max_all_str == ''):
                clique_max_all_str = str(i)
            else:
                clique_max_all_str += ', ' + str(i)

        if(len(a) > 2):
            plt.text(-0.5, -1.1,'Максимальные клики: ' + clique_max_all_str)
        else:
            plt.text(-0.5, -0.01,'Максимальные клики: ' + clique_max_all_str)
        pylab.show()

    except MatrixFormatError:
        print('Ошибка: неправильно составлена матрица.')
        sys.exit(1)
    except:
        print('Ошибка в программе.')
        sys.exit(2)