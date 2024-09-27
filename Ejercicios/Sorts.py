import random
import time

def mcd(M, N):
    while N != 0:
        M, N = N, M % N
    return M


def bubble_sort(list):
    for i in range(len(list)-1,0,-1):
        swap = False
        for j in range(i):
            if list[j]>list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
                swap = True
        if not swap:
            break
    return list


def bogo_sort(list):
    while list != sorted(list):
        random.shuffle(list)


def cocktail_sort(list):
    swapped = True
    start = 0
    end = len(list)-1

    while True:
        swapped = False

        # Iteración hacia adelante
        for i in range(start, end):
            if (list[i] > list[i + 1]):
                list[i], list[i + 1] = list[i + 1], list[i]
                swapped = True
 
        if not swapped:
            break

        swapped = False
        end -= 1
 
        # Iteración hacia atrás
        for i in range(end-1, start-1, -1):
            if (list[i] > list[i + 1]):
                list[i], list[i + 1] = list[i + 1], list[i]
                swap = True
 
        if not swapped:
            break

        start += 1

    return list

list = [random.randint(0, 100) for _ in range(10000)]

t0 = time.time()
cocktail_sort(list)
print("Tiempo:", time.time() - t0)