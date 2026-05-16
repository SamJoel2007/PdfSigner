import subprocess

subprocess.run("pyinstaller --onefile pdfsign.py", shell=True)