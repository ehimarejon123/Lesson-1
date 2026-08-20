guess = input("At n = 1000, O(n^2) takes how many steps? ")
input("Watch O(n) and O(n^2) grow. Press Enter ")
for n in [10, 100, 1000]:
    input("n = " + str(n) + "  Press Enter ")
    print(" O(n) =", n, " O(n^2) =", n * n)
print(" your guess:", guess)