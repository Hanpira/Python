# Sorting
import random
import datetime
import prettytable                  # пакет для таблицы
import matplotlib.pyplot as plt     # библиотека для графика


def BubbleSort(A):                  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                a = A[j]
                A[j] = A[j+1]
                A[j+1] = a


def QuickSort(A, fst, lst):         # быстрая сортировка
    if fst >= lst:
        return

    #i, j = fst, lst
    pivot = A[fst]
    # pivot = A[random.randint(fst, lst)]
    first_bigger = fst+1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger+1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger-1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller-1)
    QuickSort(A, first_bigger, lst)


def InsertionSort(num):
    for i in range(1, len(num)):
        key = num[i]
        j = i-1
        while j >=0 and key < num[j] :
                num[j + 1] = num[j]
                j -= 1
        num[j + 1] = key
    return num

def MergeSort(num):
    if len(num) > 1:
        mid = len(num) // 2  # находим середину массива

        # делим массив на две части
        L = num[:mid]
        R = num[mid:]

        # рекурсивно сортируем две половины
        MergeSort(L)
        MergeSort(R)

        i = j = k = 0

        # сливаем отсортированные половины в один массив
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                num[k] = L[i]
                i += 1
            else:
                num[k] = R[j]
                j += 1
            k += 1

        # проверяем, не осталось ли элементов в какой-либо из половин
        while i < len(L):
            num[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            num[k] = R[j]
            j += 1
            k += 1
        return num




table = prettytable.PrettyTable(["List", "BubbleSort time", "QuickSort time", "InsertionSort time", "MergeSort time"])
x=[]
y1=[]
y2=[]
y3=[]
y4=[]


for N in range(1000,5001,1000):
    x.append(N)
    min=1
    max=N
    A=[]
    for i in range (N):
        A.append(int(round(random.random()*(max-min)+min)))

    #print(A)

    B = A.copy()
    I = A.copy()
    D = A.copy()
    # print(B)

    # BubbleSort(A)
    print("---")
    # print(A)


    # QuickSort(B, 0, len(B)-1)
    print("---")
    # print(B)

    t1 = datetime.datetime.now()
    BubbleSort(A)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    print("Пузырьковая сортировка   " +str(N)+"   заняла   "+str((t2-t1).total_seconds()) + "c")

    t3 = datetime.datetime.now()
    QuickSort(B, 0, len(B)-1)
    t4 = datetime.datetime.now()
    y2.append((t4 - t3).total_seconds())
    print("Быстрая   " +str(N)+"   заняла   "+str((t4-t3).total_seconds()) + "c")

    t5 = datetime.datetime.now()
    InsertionSort(I)
    t6 = datetime.datetime.now()
    y3.append((t6 - t5).total_seconds())
    print("Сортировка вставками   " +str(N)+"   заняла   "+str((t6-t5).total_seconds()) + "c")

    t7 = datetime.datetime.now()
    MergeSort(D)
    t8 = datetime.datetime.now()
    y4.append((t8 - t7).total_seconds())
    print("Сортировка слиянием   " +str(N)+"   заняла   "+str((t8-t7).total_seconds()) + "c")

    table.add_row([str(N),
                   str((t2-t1).total_seconds()),
                   str((t4-t3).total_seconds()),
                   str((t6-t5).total_seconds()),
                   str((t7-t8).total_seconds())])
print(table)

plt.plot(x, y1, "C0")
plt.plot(x, y2, "C1")
plt.plot(x, y3, "C2")
plt.plot(x, y4, "C3")
plt.show()