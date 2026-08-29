number = int(input("Enter a number: "))
if number <= 1:
    print("It's not a prime number.")
else:
    count = 0
    for i in range(1, number + 1):
        if number % i == 0:
            count += 1
    if count == 2:
        print("It's a prime number")
    else:
        print("It's a prime number")