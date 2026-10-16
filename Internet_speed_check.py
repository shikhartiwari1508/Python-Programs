import subprocess
result = subprocess.run(["ping", "-c", "4", "8.8.8.8"], capture_output=True, text=True)
print(result.stdout.splitlines()[-1])