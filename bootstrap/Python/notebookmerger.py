import os
with open("science-notes.txt", "r") as science:
    data = science.read()
    print("Science notes")
    print(data)
with open("maths-notes.txt", "r") as maths:
    print("\nMaths Notes Word Count")
    for line in maths:
        line = line.strip()
        words = line.split()
        print("Line:", line)
        print("Words:", len(words))
if not os.path.exists("all-notes.txt"):
    with open("science-notes.txt", "r") as s:
        science_data = s.read()
    with open("maths-notes.txt", "r") as m:
        maths_data = m.read()
    with open("all-notes.txt", "w") as all_notes:
        all_notes.write(science_data)
        all_notes.write("\n\n")
        all_notes.write(maths_data)
    print("\nFiles merged successfully!")
else:
    print("\nMerged file already exists.")
if os.path.exists("all-notes.txt"):
    os.remove("all-notes.txt")
    print("Merged file deleted successfully!")
else:
    print("Merged file not found.")