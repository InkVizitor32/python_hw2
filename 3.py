# Требуется найти наименьший натуральный делитель целого числа N, отличный от 1.

n = int(input())
for min in range(2,n+1):    
     if  n % min == 0:
        print(min)  
        break
    