import subprocess

result = subprocess.run(
    "ls | grep requirements.txt",
    shell=True,
    capture_output=True,
    text=True
)

filename = result.stdout.strip()

save = subprocess.run(
    f'pip freeze > {filename}',
    shell=True
)

with open(filename,"r") as f:
    print(f.read())


