with open("test.txt", "r") as f:
    for line in f.readlines():
        if len(line.strip()) > 5:
            print(line.strip())
