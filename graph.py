import pylab
from networkx import nx
import matplotlib.pyplot as plt
import networkx.algorithms.clique as cl
import sys
import warnings
from tkinter import *
import math

'''
Программа принимает матрицу смежности, строит на её основе граф,
находит максимальную клику, рисует граф, раскрашивая вершины и пути , входящие в максимальную клику,
в зелёный цвет, а остальные в красный
'''

warnings.filterwarnings("ignore", category=UserWarning)

class MatrixFormatError(Exception):
    '''Ошибка, отвечающая за правильное указание матрицы'''
    pass

def Matrix_check(matrix):
    #Не обязательное условие
    # for i in range(lenght):
    #     if(matrix[i][i] != 0):
    #         raise MatrixFormatError('элементы не должны иметь пути от самих себя')
    '''Проверяет матрицу на правильность '''
    lenght = len(matrix[0])
    for i in range(lenght):
        for j in range(lenght):
            if(matrix[i][j] != matrix[j][i]):
                raise MatrixFormatError
            if(not (matrix[i][j] == 1 or matrix[i][j] == 0)):
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

def chunks(lst, chunk_size):
    return [lst[i:i+chunk_size] for i in range(0, len(lst), chunk_size)]


def get_matrix():
    global graph_matrix
    graph_matrix = list(map(int, tex.get(1.0, END).split()))
    if (math.sqrt(len(graph_matrix)).is_integer()):
        graph_matrix = chunks(graph_matrix, int(math.sqrt(len(graph_matrix))))
        try:
            Matrix_check(graph_matrix)
            root.destroy()
        except:
            pass

if __name__ == '__main__':
    try:
        graph_matrix = []
        root=Tk()
        root.geometry('450x450')
        but=Button(root, text='Ok', command=get_matrix)
        tex=Text(root,height=20,width=40, font="Arial 16")
        tex.pack()
        but.pack()
        root.mainloop()

        graph = Graph_create(graph_matrix)
        clique_max_all = Graph_max_clique(graph)
        clique_max = clique_max_all[0]
        lenght = len(graph_matrix[0])
        #задание цвета вершинам
        color_node=[]
        for i in range(lenght * lenght - 1):
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

        if(lenght > 2):
            plt.text(-0.5, -1.1,'Максимальные клики: ' + clique_max_all_str)
        else:
            plt.text(-0.5, -0.01,'Максимальные клики: ' + clique_max_all_str)
        pylab.show()

    except:
        print('Ошибка в программе.')
        sys.exit(2)