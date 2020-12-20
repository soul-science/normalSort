def quickSort(matrix, mode=True):
    if len(matrix) < 2:
        return matrix
    else:
        standard = matrix[0]
        less = [each for each in matrix[1:] if each <= standard]
        great = [each for each in matrix[1:] if each > standard]
        if mode == True:
            return quickSort(less) + [standard] + quickSort(great)
        else:
            return quickSort(great, False) + [standard] + quickSort(less, False)
    
