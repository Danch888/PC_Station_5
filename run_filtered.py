import sys
with open("parsed.txt", "r") as f:
    for line in f.readlines():
        if "WARNING" not in line and "The command" not in line and "random sample" not in line and not line.startswith("['core/libs") and not line.startswith("```"):
            print(line.strip())
