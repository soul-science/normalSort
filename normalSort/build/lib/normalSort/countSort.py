def countSort(matrix, mode=True):
    length = max(matrix) + 1
    numbers = [0] * length

    for each in matrix:
        numbers[each] += 1

    matrix = []
    if mode == True:
        for i in range(length):
            matrix.extend([i]*numbers[i])
    else:
        for i in range(length-1, -1, -1):
            matrix.extend([i]*numbers[i])

    return matrix

