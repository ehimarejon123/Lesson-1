def print_factor(number):
    print("The factors are", number, "are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)
number = int(input("Enter a number: "))
print_factor(number)