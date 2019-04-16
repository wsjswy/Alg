import random



def quick_sort2(L, left, right):

    i = left
    j = right

    if (left >= right):
            return
    base = L[left]
    while i < j:
        while (i < j and  base <= L[j]):
            j = j - 1
        #此时走到L[j]比base小的地方，此时将L[j]赋值给L[i]
        L[i] = L[j]
        #此时走到L[i]比base大的地方将L[i]赋值给L[j]
        while (i < j and base >= L[i]):
            i = i + 1
        L[j] = L[i]
    L[i] = base
    quick_sort2(L, left, i - 1)
    quick_sort2(L, i + 1, right)

def quick_sort_3_python(L, left, right):
    i = left
    j = right

    if (left >= right):
        return
    base = L[left]

    while i < j:
        while (i < j and base <= L[j]):
            j = j - 1
        # 此时走到L[j]比base小的地方，此时将L[j]赋值给L[i]
        L[i] = L[j]
        # 此时走到L[i]比base大的地方将L[i]赋值给L[j]
        while (i < j and base >= L[i]):
            i = i + 1
        L[j] = L[i]
    L[i] = base
    quick_sort_3_python(L, left, i - 1)
    quick_sort_3_python(L, i + 1, right)

def quick_sort(data):
    """快速排序"""
    if len(data) >= 2:  # 递归入口及出口
        mid = data[0]  # 选取基准值，也可以选取第一个或最后一个元素
        left, right = [], []  # 定义基准值左右两侧的列表
        data.remove(mid)  # 从原始数组中移除基准值
        for num in data:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [mid] + quick_sort(right)
    else:
        return data
def quick_sort_python(data):
    if len(data) >= 2:
        base = data[0]
        right, left = [], []
        data.remove(base)
        for num in data:
            if num > base:
                right.append(num)
            else:
                left.append(num)
        return  quick_sort(left) + [base] + quick_sort(right)
    else:
        return data


def quick_sort_4_python(L):
    if len(L) >= 2:
        base = L[0]
        left, right = [] , []
        L.remove(base)
        for data in L:
            if data < base:
                left.append(data)
            else:
                right.append(data)
        return quick_sort_4_python(left) + [base] + quick_sort_4_python(right)
    else:
        return L

if __name__ == '__main__':

    L = random.sample(range(0, 10), 2)
    #
    print(L)
    # quick_sort_3_python(L, 0, 9)
    #
    # quick_sort2(L, 0, len(L) - 1)
    print(L)


    # print(quick_sort_3_python(L, 0, len(L) - 1))
