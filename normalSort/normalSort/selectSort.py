def selectSort(matrix, mode=True):
    i = 0
    if mode == True:
        while i < len(matrix):
            j = i+1
            Min = i
            while j < len(matrix):
                if matrix[Min] > matrix[j]:
                    Min = j
                j += 1
            
            matrix[i], matrix[Min] = matrix[Min], matrix[i]
            i += 1
    else:
        while i < len(matrix):
            j = i+1
            Max = i
            while j < len(matrix):
                if matrix[Min] < matrix[j]:
                    Max = j
                j += 1
            
            matrix[i], matrix[Max] = matrix[Max], matrix[i]
            i += 1
    return matrix
