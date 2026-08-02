with open("class-notes.txt", "r") as file:
    n = int(input("How many characters do you want to preview? "))
    print("\nPreview:")
    print(file.read(n))

with open("class-notes.txt", "r") as file:
    lines= file.readlines()
print("\nALL Notes:")
for i in range(len(lines)):
    print(i + 1, "-", lines[i].strip())

skip_subject = input("\nEnter subject to skip: ")
print("\nChecking Notes:")
for line in lines:
    subject = line.strip()
    if subject == skip_subject:
        print("Skip ->", subject)
    else:
        print("Keep ->", subject)

with open("odd-notes.txt", "w") as new_file:
    for i in range(len(lines)):
        if i % 2 == 0:
            new_file.write(lines[i])
print("\nOdd-numbered lines copied to odd-notes.txt")