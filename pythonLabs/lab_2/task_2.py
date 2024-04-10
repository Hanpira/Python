# Functional programming methods
# 1. Используя функцию map() переписать функцию
items = [1, 2, 3, 4, 5]
# squared = []
# for i in items:
#     squared.append(i**2)
squared_map = list(map(lambda x: x**2, items))
print("Ex 1. map(): ", squared_map)

# 2. Используйте функцию reduce() и перепишите код
# product = 1
# list2 = [1, 2, 3, 4]
# for num in list2:
#     product = product * num

from functools import reduce
list2 = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, list2)
print("Ex 2. reduce(): ", product)

# 3. Используйте функцию map() и перепишите код
numbers = [1, 2, 3, 4, 5]
# squared = []
# for num in numbers:
#        squared.append(num ** 2)
def square(n):
    return n * 2
squared = list(map(square,numbers))
squared_l = list(map(lambda x: x*2, numbers))

print("Ex 3. map(): ", squared)
print("    or  map() + lambda: ", squared_l)


# 4. Объедините списки x = [1, 2, 3] и y = [4, 5, 6] с помощью функции zip()
x = [1, 2, 3]
y = [4, 5, 6]
union_zip = zip(x, y)
list_zip = list(union_zip)
# short version
zipped_list = list(zip(x,y))
print("Ex 4. zip(): ", list_zip)
print("    or short version: ", zipped_list)



# 5. Используйте функцию zip() чтобы преобразовать код:
name_hero = [
    'Hulk',
    'Mr. Fantastic',
    'Invisible Woman',
    'Doctor Strange',
    'Doctor Octopus',
    'Spider-Man',
]
name_real = [
    'Bruce Banner',
    'Reed Richards',
    'Sue Storm',
    'Stephen Strange',
    'Otto Octavius',
    'Peter Parker',
]
# for i in range(len(name_hero)):
#     print(name_hero[i], '-', name_real[i])
print("Ex 5. zip() with superheroes: ")
for hero, real_name in zip(name_hero, name_real):
    print(hero, ' - ', real_name)
print ("or as dictionary (key : value):")
hero_list = dict(zip(name_hero, name_real))

print(hero_list)


# 6. С помощью функции filter() переместите из списка
# numbers = [1, 2, 4, 5, 7, 8, 10, 11] нечетные элементы в новый список.
numbers = [1, 2, 4, 5, 7, 8, 10, 11]

odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("6. filter(): ", odd_numbers)