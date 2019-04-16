import random

"""
从待排序序列中，找到关键字最小的元素；
如果最小元素不是待排序序列的第一个元素，将其和第一个元素互换；
从余下的 N - 1 个元素中，找出关键字最小的元素，重复(1)、(2)步，直到排序结束。
因此我们可以发现，简单选择排序也是通过两层循环实现。
第一层循环：依次遍历序列当中的每一个元素
第二层循环：将遍历得到的当前元素依次与余下的元素进行比较，符合最小元素的条件，则交换。
"""
def select_sort(L):
    for i in range(len(L)):
        minmum = L[i]
        for j in range(i + 1, len(L)):
            if L[j] < minmum:
                L[j], minmum = minmum, L[j]
        L[i] = minmum #将最小值赋给当前元素


if __name__ == '__main__':
    L = random.sample(range(0, 10), 10)
    select_sort(L)
    print(L)