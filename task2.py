with open ("output.txt", "wt") as fh:
    text = input("Enter text to write to the file: ")
    fh.write(text + "\n")
    print("Data is successfully written to output.txt")
print("\n")
with open ("output.txt", "at") as fh:
    text1 = input("Enter additional text to append: ")
    fh.write(text1 + "\n")
    print("Data is successfully appended.")
print("\n")
with open ("output.txt", "rt") as fh:
    data = fh.read()
    print("Final content of output.txt: ")
    print(data)
fh.close()