import  random


def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]





if __name__ == '__main__':
    L = random.sample(range(0, 10), 10)
    bubble_sort(L)
    print(L)