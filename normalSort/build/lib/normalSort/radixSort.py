# 基数排序
def radixSort(matrix, d, mode=True) -> list:
    for k in range(d):#d轮排序
        # 每一轮生成10个列表
        s=[[] for i in range(10)]#因为每一位数字都是0~9，故建立10个桶
        for i in matrix:
            # 按第k位放入到桶中
            s[i//(10**k)%10].append(i)
        # 按当前桶的顺序重排列表
        if mode == True:
            matrix=[j for i in s for j in i]
        else:
            matrix=[j for i in range(9, -1,-1) for j in s[i]]
    return matrix
