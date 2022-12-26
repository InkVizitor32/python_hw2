# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

n = int(input())

index=0

for i in range(n+1):
    index = index + i
print(index)
