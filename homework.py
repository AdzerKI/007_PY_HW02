# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

number = input("Enter float: ")
sum = 0

if number.find(".") < 0:
    a = int(number)
    while a > 0:
        sum += a % 10
        a //= 10
else:
    x = number.split(".") 
    a = int(x[0])
    b = int(x[1])

    while a > 0:
        sum += a % 10
        a //= 10
    while b > 0:
        sum += b % 10
        b //= 10

print(f"{number} -> {int(sum)}")


# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

number = int(input("Enter N: "))

if number < 1:
    print("wrong N")
else:
    temp = 1
    arr = []

    for i in range (0, number):
        temp = temp * i
        arr.append(temp)

    print(f"Пусть N = {number}, тогда {arr}")



# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

number = int(input("Enter N: "))

if number < 1:
    print("wrong N")
else:
    arrOne = []
    temp = 0
    for i in range (0, number):
        temp += 1
        arrOne.append(temp)
    
    arrTwo = []
    temp = 0
    for i in range (0, number):
        if i < 1:
            i = 1
        temp += (1 + 1 / i) ** i
        arrTwo.append(temp)

    # сидел долго, единственное решение - неверное условие или неверный пример
    print(f"Для n = {number}: ", end='')
    for i in range(0, number):
        if i < number - 1:
            print(f"{arrOne[i]}:{arrTwo[i]}, ", end='')
        else:
            print(f"{arrOne[i]}:{arrTwo[i]}", end='')


# Реализуйте алгоритм перемешивания списка.

# метод shuffle нельзя скопировать как понимаю
import random
arr = [1, 2, 3, 4, 5, 6]

print(arr)
for i in range (0, len(arr)):
    temp = 0
    j = random.randint(0, len(arr)-1)
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
print(arr)

