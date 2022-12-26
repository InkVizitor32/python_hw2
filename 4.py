n = int(input('Введите количество учеников: '))
x = int(input('Введите рост Пети: '))
import random
from random import random, randrange, randint
import heapq

list=[randint(150,200) for i in range(n)] 
print(*list)


# print(*heapq.nsmallest(len(list), list)) # Вывели результат сортировки списка по возрастанию, 
                                        # причем: len(list) - количество элементов списка,
                                        # к которым нужно применить сортировку
print(*heapq.nlargest(len(list), list))  # по убыванию

k = 1
for i in range(n-1):
    if list[i] >=x:
        k+=1
print(k) 