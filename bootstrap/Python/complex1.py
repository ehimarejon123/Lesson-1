n = 100
total = n * (n + 1) // 2
print(total)

n = 100
total = 0
for i in range(1, n+1):
    total = total + i
print(total)

numbers = [1, 2, 3, 4, 5]
for i in numbers:
    for j in numbers:
        print(i, j)