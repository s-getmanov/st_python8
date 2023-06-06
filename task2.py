#https://github.com/s-getmanov/st_python8.git

# Вводим число элементов и сами элементы списка
N = 0
while not (1 <= N and N <= 100000):
    N = int(input("Введите количество элементов списка (1 ≤ N ≤ 100000): ")) 

work_list = []

# Обеспечим ввод строго нужного количества элеметов.
# Будем запрашивать ввод, пока не будет введено нужное количество элементов
while len(work_list) < N:
    ost = N - len(work_list)
    current_list = list(map(int, input(f"Введите {ost} элементов списка через пробел: ").split()))

    for i in current_list:
        # В рабочий список добавим только елементы, подходящие под условие задачи  
        if i >= 1 and i<= 10e9:
            work_list.append(i)            
        if len(work_list) == N:
            break    

print("Введен список: ", end=" ")
for m in work_list:
    print(m, end=" ")
print()
#Меняем список, по факту нам просто нужно переставить последний элемент в начало списка
work_list.insert(0, work_list.pop())

# Выводим измененный список на экран
print("Получен список:", end=" ")
for m in work_list:
    print(m, end=" ")

