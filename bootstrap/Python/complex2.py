numbers = [10, 20, 30, 40, 50, 60, 70]
target = 50
checks = 0
found = False
for number in numbers:
    checks +=1
    if number == target:
        found = True
        break
    if found:
        print("Number found")
    else:
        print("Number not found")