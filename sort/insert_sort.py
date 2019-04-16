import random

#插入排序
def insert_sort(L):
    #遍历数组中的所有元素，其中0号索引元素默认已排序，因此从1开始
    for x in range(1, len(L)):
        # 将该元素与已排序好的前序数组依次比较，如果该元素小，则交换
        # range(x-1,-1,-1):从x-1倒序循环到0
        for j in range(x - 1, -1, -1):
            # 判断：如果符合条件则交换(j+1第一次就是当前的x元素)
            print(L)
            if L[j] > L[j + 1]:
                L[j + 1], L[j] = L[j], L[j + 1]


if __name__ == '__main__':
    L = random.sample(range(0, 10), 10)
    print(L)
    insert_sort(L)
    print(L)







