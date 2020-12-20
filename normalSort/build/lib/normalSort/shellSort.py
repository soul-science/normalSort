def shellSort(matrix, mode=True):
    step = len(matrix) // 2

    while step != 0:
        for i in range(step, len(matrix), step):
            t = matrix[i]
            if mode == True:
                for j in range(step, i+step, step):
                    if t < matrix[i-j]:
                        matrix[i-j+step] = matrix[i-j]
                        matrix[i-j] = t
                    else:
                        matrix[i-j+step] = t
                        break
            else:
                for j in range(step, i+step, step):
                    if t > matrix[i-j]:
                        matrix[i-j+step] = matrix[i-j]
                        matrix[i-j] = t
                    else:
                        matrix[i-j+step] = t
                        break
        step = step // 2

    return matrix
