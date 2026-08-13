n = 5
total = n * (n + 1) // 2

5 * 6 / 2 = 30 // 2

n = 5
total = 0
for i in range(1, n + 1):
    total = total + i
print(total)

n = 5
total = 0
for i in range(1, n + 1):
    points = 0
    for j in range(i):
        points = points + 1
    total = total + points

print(total)