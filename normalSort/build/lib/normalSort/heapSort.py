import sys


sys.setrecursionlimit(9000000)


def heapSort(matrix, length, mode=True):
    if length == 1:
        return
    else:
        if mode == True:
            for i in range(length//2-1, -1, -1):
                for j in range(i*2+1, min(i*2+3, length)):
                    if matrix[i] < matrix[j]:
                        matrix[i], matrix[j] = matrix[j], matrix[i]

            for i in range(1, length//2):
                for j in range(i*2+1, min(i*2+3, length)):
                    if matrix[i] < matrix[j]:
                        matrix[i], matrix[j] = matrix[j], matrix[i]
        else:
            for i in range(length//2-1, -1, -1):
                for j in range(i*2+1, min(i*2+3, length)):
                    if matrix[i] > matrix[j]:
                        matrix[i], matrix[j] = matrix[j], matrix[i]

            for i in range(1, length//2):
                for j in range(i*2+1, min(i*2+3, length)):
                    if matrix[i] > matrix[j]:
                        matrix[i], matrix[j] = matrix[j], matrix[i]

        matrix[0], matrix[length-1] = matrix[length-1], matrix[0]
        heapSort(matrix, length-1, mode)



