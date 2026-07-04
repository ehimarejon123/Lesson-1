def countdown(n):
    if n == 0:
        print("Blast Off!")
        return
    print(n)
    countdown(n - 1)
    
countdown(5)