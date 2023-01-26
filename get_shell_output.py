import subprocess

def bash(command):
    cmdlist = command.split(" ")
    output = subprocess.run(cmdlist, capture_output=True)
    output = output.stdout.decode("utf-8")
    return output
print(bash("ls -al"))
print(bash("pwd"))
