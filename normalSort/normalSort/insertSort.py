def insertSort(matrix, mode=True):

    if mode == True:
        for i in range(1, len(matrix)):
            m = matrix[i]
            t = 1
            while i - t >= 0:
                if matrix[i-t] > m:
                    matrix[i-t+1] =  matrix[i-t]
                else:
                    matrix[i-t+1] = m
                    break
                t += 1
    else:
        for i in range(1, len(matrix)):
            m = matrix[i]
            t = 1
            while i - t >= 0:
                if matrix[i-t] < m:
                    matrix[i-t+1] =  matrix[i-t]
                else:
                    matrix[i-t+1] = m
                    break
                t += 1

    return matrix
