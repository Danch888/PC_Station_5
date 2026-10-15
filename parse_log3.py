with open("git_log.txt", "r") as f:
    for line in f.readlines():
        if "WARNING" not in line and "The command" not in line and "random sample" not in line and "```" not in line and "['core/libs" not in line:
            print(line.strip())
