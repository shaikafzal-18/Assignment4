try:
    with open ("sample.txt", "rt") as fh:
        count = 0
        for line in fh:
            count += 1
            print(f"Line {count}: {line.strip()}")
except FileNotFoundError:
    print(f"The file sample.txt was not found.")