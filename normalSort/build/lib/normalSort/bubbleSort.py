def bubbleSort(matrix, mode=True):
    if mode == True:
        for i in range(0, len(matrix)):
            j = 0
            while j + 1 < len(matrix)-i:
                if matrix[j] > matrix[j+1]:
                    matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
                j += 1
    else:
        for i in range(0, len(matrix)):
            j = 0
            while j+1 < len(matrix)-i:
                if matrix[j] < matrix[j+1]:
                    matrix[j], matrix[j+1] = matrix[j+1], matrix[j]
                j += 1
    return matrix
