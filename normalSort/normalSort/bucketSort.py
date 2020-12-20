def get_Min_Max(matrix) -> tuple:
    Max = matrix[0]
    Min = matrix[0]
    i = 0
    for each in matrix:
        if each > Max:
            Max = each
        if each < Min:
            Min = each
        i += 1
    return i, Max, Min

def bucketSort(matrix, sort=None, mode=True):
    length, Max, Min = get_Min_Max(matrix)
    buckets = [[] for _ in range(length // 100 + 1)]
    m = (length // 100) / (Max - Min)
    for each in matrix:
        buckets[int((each - Min) * m)].append(each)

    matrix = []
    if sort == None:
        for i in range(length // 100 + 1):
            buckets[i].sort(reverse=mode)
            matrix.extend(buckets[i])
    else:
        for i in range(length // 100 + 1):
            matrix.extend(sort(buckets[i], mode=mode))
    return matrix
