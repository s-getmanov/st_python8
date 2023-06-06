# #https://github.com/s-getmanov/st_python8.git

#Введем максимальную грузоподъемность лодки
m = 0
while not (1 <= m and m <= 10e6):
    m = int(input("Введите максимальный вес для одной лодки ((1 ≤ m ≤ 10e6)): ")) 

#Введем количество рыбаков
n = 0
while not (1 <= n and n <= 100):
    n = int(input("Введите количество рыбаков (от 1 до 100): "))

weights_list = []

#Введем веса рыбаков
for i in range(n):
    curr_w = 0
    #Вес одного рыбака не может быть больше максимального веса для лодки, иначе мы задачу не решим. 
    while not (1 <= curr_w and curr_w <= m):
        curr_w = int(input(f"Введите вес рыбака {i+1} из {n} (число от 1 до {m})"))
    weights_list.append(curr_w)

#Отсортируем рыбаков по весу
weights_list.sort()

boats = 0
skinny_fisherman, fat_fisherman = 0, n - 1

while skinny_fisherman <= fat_fisherman:
    
    if skinny_fisherman == fat_fisherman: #Рыбаки закончились
        boats += 1
        break
    #Самый худой и самый толстый рыбаки поместились в одну лодку, сажаем обоих в лодку и переходим к следующей паре.
    elif weights_list[skinny_fisherman] + weights_list[fat_fisherman] <= m:
        skinny_fisherman += 1
        fat_fisherman -= 1
        boats += 1
    #Самый худой и самый толстый рыбаки не поместились в одну лодку, сажаем только толстого и переходим к следующему по толщине, худого оставляем того-же.
    else:
        fat_fisherman -= 1
        boats += 1

print(f"Для перевозки всех рыбаков понадобится {boats} лодок")














# Можно решить эту задачу, используя жадный алгоритм:

# Отсортируйте массив весов рыбаков в порядке возрастания.
# Идите с двух концов массива и помещайте двух самых легких рыбаков в одну лодку. Если суммарный вес этих двух рыбаков превышает m, поместите в лодку только одного из них, который будет наименее тяжелым.
# Измените границы массива, отсекая уже помещенных в лодку рыбаков.
# Повторяйте шаги 2 и 3, пока все рыбаки не будут перевезены на другой берег.
# Вот решение на Python:

# m = int(input())
# n = int(input())
# weights = sorted([int(input()) for i in range(n)])

# boats = 0
# left, right = 0, n - 1
# while left <= right:
#     if left == right:
#         boats += 1
#         break
#     elif weights[left] + weights[right] <= m:
#         left += 1
#         right -= 1
#         boats += 1
#     else:
#         right -= 1
#         boats += 1

# print(boats)