#https://github.com/s-getmanov/st_python8.git

#Запросим размер массива
N = int(input("Введите количество элементов массива: ")) 

#По условиям размер 1 ≤ N ≤ 10000
while not (1 <= N and N <= 10000):
    print(f"Количество элементов должно быть в интервале 1 ≤ N ≤ 10000! Вы ввели {len(N)}!")
    N = int(input("Введите количество элементов массива: ")) 

numbers = []

# Введем числа
for i in range(N):
    num = int(input())
    #   Ограничим ввод числами не больше 10е5
    if num <= 10e5:
      numbers.append(num)
    else:
       print(f"Число {num} превышает 10е5 и не будет включено в результат!")

# Перевернем массив
numbers.reverse()

#Вывод результата
for num in numbers:
  print(num)