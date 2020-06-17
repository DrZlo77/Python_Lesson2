# Задачи на циклы и оператор условия------
# ----------------------------------------


'''
Задача 1
Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.
'''

print('Задача 1', ' Вывести на экран циклом пять строк из нулей, причем каждая строка должна быть пронумерована.')

for i in range(1, 6):
    print(i, 00000000)
print()
'''
Задача 2
Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.
'''
print('Задача 2','Пользователь в цикле вводит 10 цифр. Найти количество введеных пользователем цифр 5.')

quantity_five = 0
for i in range(1, 11):
    numer = input("Введите цифру: ")
    while not numer.isdigit():
        numer = input('Введите целую простую цифру меньше 10:')
    numer = int(numer)
    if type(numer) != int:
       numer = int(numer)
    if numer == 5:
       quantity_five +=1
print('Число вводов цифры пять равно: ', quantity_five)
print()


'''
Задача 3
Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.
'''

print('Задача 3',' Найти сумму ряда чисел от 1 до 100. Полученный результат вывести на экран.')

sum = 0
for i in range(1, 101):
     sum += i
print('Ответ: ',str(sum))
print()
'''
Задача 4
Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран.
'''

print('Задача 4',' Найти произведение ряда чисел от 1 до 10. Полученный результат вывести на экран')

pr = 1
for i in range(1, 11):
    pr *= i
print('Ответ: ',str(pr))
print()
'''
Задача 5
Вывести цифры числа на каждой строчке.
'''

print('Задача 5', 'Вывести цифры числа на каждой строчке.')

numer = input("Введите число: ")

while not numer.isdigit():
    numer = input('Введите целое число:')

numer = int(numer)
list_of_numbers = []  # Создаем список
while numer > 0:

    list_of_numbers.append(numer % 10)
    numer = numer // 10

list_of_numbers.reverse()  # Переворачиваем список

for element in list_of_numbers:  # выводим значения
    print(element)
print()

'''
Задача 6
Найти сумму цифр числа.
'''
print('Задача 6',' Найти сумму цифр числа.')
numer = input("Введите число: ")
while not numer.isdigit():
    numer = input('Введите целое число:')

numer = int(numer)
sum = 0

while numer > 0:
    sum += numer % 10
    numer = numer//10
print('Ответ: ',str(sum))
print()
'''
Задача 7
Найти произведение цифр числа.
'''

print('Задача 7', 'Найти произведение цифр числа.')


numer = input("Введите число: ")
while not numer.isdigit():
    numer = input('Введите целое число:')

numer = int(numer)
pr = 1

while numer > 0:
    pr *= numer%10
    numer = numer//10
print('Ответ: ',str(pr))
print()

'''
Задача 8
Дать ответ на вопрос: есть ли среди цифр числа 5?
'''

print('Задача 8','Дать ответ на вопрос: есть ли среди цифр числа 5?')

numer = input("Введите число: ")
while not numer.isdigit():
    numer = input('Введите целое число:')

numer = int(numer)
five_on_board = False
while numer>0:
    if numer%10 == 5:
        five_on_board = True
    numer = numer//10
if five_on_board:
    print('В числе есть цифра 5')
else:
    print('В числе нет цифры 5')
print()
'''
Задача 9
Найти максимальную цифру в числе
'''

print('Задача 9','Найти максимальную цифру в числе')

numer = input("Введите число: ")
while not numer.isdigit():
    numer = input('Введите целое число:')

numer = int(numer)

maximum = 0

while numer > 0:
    if numer%10 >= maximum:
        maximum = numer % 10
    numer = numer//10

print('Ответ: ',str(maximum))
print()


'''
Задача 10
Найти количество цифр 5 в числе
'''

print('Задача 10','Найти количество цифр 5 в числе')

numer = input("Введите число: ")
while not numer.isdigit():
    numer = input('Введите целое число:')

numer = int(numer)

quantity_five = 0
while numer > 0:
    if numer%10 == 5:
        quantity_five +=1
    numer = numer//10
print(' Количество пятерок в числе: ', quantity_five)
