import numpy as np

class Node:
    def __init__(self, data):
        self.data = data
        self.step = {}
        #self.step = [] #maybe?

def chain(matrix):
    my_chain = [Node(i) for i in range(1, len(matrix) + 1)]
    for i in range(len(matrix)):
        row = matrix[i]
        for j in range(len(row)):
            p = row[j]
            if p > 0:
                my_chain[i].step[my_chain[j]] = p
    return my_chain

def create_path(num, my_chain, matrix):
    for i in range(len(my_chain)):
        print("Start: ", i + 1)
        current = my_chain[i]
        for j in range(num):
            print(str(current.data) + " -> ", end='')
            values = np.random.uniform()
            S = 0
            path = 0
            while values > S:
                S += list(current.step.values())[path]
                if S > values:
                    current = list(current.step.keys())[path]
                path += 1
        print("\n________")

matrix = [[0/10, 0/10, 6/10, 4/10, 0/10, 0/10, 0/10, 0/10],
            [0/10, 5/10, 0/10, 0/10, 4/10, 0/10, 1/10, 0/10],
            [4/10, 0/10, 0/10, 0/10, 0/10, 6/10, 0/10, 0/10],
            [7/10, 0/10, 0/10, 0/10, 0/10, 3/10, 0/10, 0/10],
            [0/10, 3/10, 0/10, 0/10, 2/10, 0/10, 5/10, 0/10],
            [0/10, 0/10, 3/10, 7/10, 0/10, 0/10, 0/10, 0/10],
            [0/10, 2/10, 0/10, 0/10, 2/10, 0/10, 6/10, 0/10],
            [0/10, 0/10, 1/10, 0/10, 4/10, 0/10, 4/10, 1/10]]
my_chain = chain(matrix)
num = 1000
num += 1
create_path(num, my_chain, matrix)