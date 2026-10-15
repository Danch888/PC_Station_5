with open("log.txt", "r") as f:
    for line in f:
        print(line.strip()[:100])
