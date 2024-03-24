# Задание 3

# Var 5
# Для каждого четного по номеру элемента списка A
# найти его сумму со следующим элементом
# и записать эти суммы в новый список B.

A = [25, 2, 13, 15, 46, 7, 9, 24]
B = []

print("Список A: " + str(A))
for i in range(len(A)-1):
    if i % 2 == 0:
        B.append(int(A[i]+A[i+1]))
print("Сумма со следующим элементом = " + str(B))

# Var 13
# Найти для каждого элемента списка А
# сумму предыдущих элементов
# и записать эти суммы в новый список.

C = []
sumPreviousElements = 0
for i in range(len(A)):
    if i == 0:
        sumPreviousElements = 0
    else:
        sumPreviousElements += A[i-1]
    C.append(sumPreviousElements)
print("Сумма предыдущих элементов = " + str(C))
