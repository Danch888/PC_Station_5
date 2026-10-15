with open("git_log.txt", "r") as f:
    for line in f.readlines():
        if "commit " in line or "Author:" in line or "Date:" in line or "    " in line:
            print(line.strip())
