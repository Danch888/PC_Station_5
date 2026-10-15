import subprocess
try:
    with open("git_log.txt", "w") as f:
        f.write(subprocess.run(["git", "log", "-n", "3", "--oneline"], capture_output=True, text=True).stdout)
except Exception as e:
    pass
