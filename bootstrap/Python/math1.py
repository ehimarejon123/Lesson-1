numbber = int(input("Enter a number: "))
temp = number
digits = len(str(number))
total = 0
while number > 0:
    digit = number % 10
    total = total + digit ** digits
    number = number // 10

if total == temp:
    print("It's an armstrong number")
else:
    print("It's not an armstrong number")