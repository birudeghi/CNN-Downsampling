# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 10:33:41 2020

@author: birudeghi
"""
matrix = [[1,2,1,4],[0,0,3,0],[1,2,0,0],[0,0,0,0]]

def maxpooling(matrix, size, stride):
    x_out = int(((len(matrix[0]) - size)/stride) + 1)
    y_out = int(((len(matrix) - size)/stride) + 1)
    output = [[0 for j in range(x_out)] for i in range(y_out)]
    curr_y = 0
    output_y = 0
    while curr_y + size <= len(matrix):
        curr_x = 0
        output_x = 0
        while curr_x + size <= len(matrix[0]):
            #max and insertion sequence here by size, code below
            output[output_y][output_x] = max([max(matrix[i][curr_x:curr_x + size]) for i in range(curr_y, curr_y + size)])
            #shift in input matrix by stride, code below
            curr_x += stride
            output_x += 1
        #shift in input matrix vy stride, code below
        curr_y += stride
        output_y += 1
            
    return output
print(maxpooling(matrix, 2, 1))


