'''Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
    Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
    Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
    Затем пользователь вводит сами элементы множеств.'''

print("Enter n: ")
n = int(input())
print('Fill list with n elements: ')
listn = [int(input()) for i in range(n)]
setn = set(listn)

print("Enter m: ")
m = int(input())
print('Fill list with m elements: ')
listm = [int(input()) for i in range(m)]
setm = set(listm)

generated = set.intersection(setn,setm)

print(sorted(generated))