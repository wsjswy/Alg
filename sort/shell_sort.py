import  random


#希尔排序：将待排序数组按照步长gap进行分组，
# 然后将每组的元素利用直接插入排序的方法进行排序；
# 每次将gap折半减小，循环上述操作；当gap=1时，完成排序


def shell_insert(L):
    gap = int(len(L) / 2)

    #第一层循环：依次改变gap值对列表进行分组
    while(gap >= 1):
        for x in range(gap, len(L)):
            for i in range(x -gap, -1, -gap):
                if L[i] > L[i + gap]:
                    L[i], L[i + gap] = L[i + gap], L[i]
        gap = (int)(gap / 2)

    print(gap)

if __name__ == '__main__':

    L = random.sample(range(0, 10), 10)
    shell_insert(L)
    print(L)