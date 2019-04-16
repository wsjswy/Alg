import  random


"""
1. 构建大顶堆


"""
# def max_heapify(L, start, end):
#     dad = start
#     son = dad * 2 + 1
#     while (son <= dad):
#         if (son + 1 <= end and L[son] <= L[son + 1]):
#             son = son + 1
#         if (L[dad] > L[son]):
#             return
#         else:
#             L[dad], L[son] = L[son], L[dad]
#             dad = son
#             son = dad * 2 + 1
#
#
#
# def heap_sort(L):
#     for i in range(len(L) // 2 - 1, -1, -1):
#         max_heapify(L, i, len(L) - 1)
#     #先将第一个元素和已排好元素前一位做交换，再重新调整，直到排序完毕
#     for i in range(len(L) - 1, 0, -1):
#         L[0], L[i] = L[i], L[0]
#         max_heapify(L, 0, i - 1)

def big_endian(arr, start, end):
    while True:
        child = start * 2 + 1  # 左孩子
        if child > end:  # 孩子比最后一个节点还大 也就意味着最后一个叶子节点了 就得跳出去一次循环已经调整完毕
            break
        if child + 1 <= end and arr[child] < arr[child + 1]:  # 为了始终让其跟子元素的较大值比较 如果右边大就左换右，左边大的话就默认
            child += 1
        if arr[start] < arr[child]:  # 父节点小于子节点直接换位置 同时坐标也得换这样下次循环可以准确判断是否为最底层是不是调整完毕
            arr[start], arr[child] = arr[child], arr[start]
            start = child
        else:  # 父子节点顺序正常 直接过
            break


# def heap_sort(arr):
#     # 无序区大根堆排序
#     first = len(arr) // 2 - 1
#     for start in range(first, -1, -1):  # 从下到上，从右到左对每个节点进调整 循环得到非叶子节点
#         big_endian(arr, start, len(arr) - 1)  # 去调整所有的节点
#
#     print(arr)
#     for end in range(len(arr) - 1, 0, -1):
#         arr[0], arr[end] = arr[end], arr[0]  # 顶部尾部互换位置
#         big_endian(arr, 0, end - 1)  # 重新调整子节点的顺序  从顶开始调整
#     return arr



def adjust_heap(L, start, end):
    while True:
        child = start * 2 + 1
        if child > end:
            break
        if child + 1 <= end and  L[child] < L[child + 1]:  #主要此处逻辑，先判断child+1是否越界，再判断二者大小
            child = child + 1
        if L[start] < L[child]:
            L[start], L[child] = L[child], L[start]
            start = child #继续向下判断
        else:
            break

def heap_sort(L):
    #从右往左，从下往上，调整堆，最后一个非叶子节点
    first = len(L) // 2 - 1
    for start in range(first, -1, -1):
        adjust_heap(L, start, len(L) - 1)

    for end in range(len(L) - 1, 0, -1):
        L[0], L[end] = L[end], L[0]
        adjust_heap(L, 0, end - 1)


if __name__ == '__main__':

    L = random.sample(range(0, 10), 10)
    print(L)
    heap_sort(L)
    print(L)