# 归并排序
def mergeSort(matrix,mode=True):
    All = []
    for i in range(0, len(matrix), 2):
        if i+1 < len(matrix):
            All.append(matrix[i:i+2])
        else:
            All.append([matrix[i]])
    while len(All)!= 1:
        for i in range(0, len(All)//2):
            if mode == True:
                All[i].sort()
                All[i+1].sort()
            else:
                All[i].sort(reverse=True)
                All[i+1].sort(reverse=True)
            All[i:i+2] = [All[i] + All[i+1]]
    if mode == True:
        All[0].sort()
    else:
        All[0].sort(reverse=True)
    All = All[0]
    
    return All
        
