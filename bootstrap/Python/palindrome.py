number int(input("Enter your number: "))
original_number = number
reverse = 0
while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original_number == reverse:
    print("It is a palindrome")
else:
    print("It is not a palindrome")