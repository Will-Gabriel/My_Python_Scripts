import paramiko

host = "127.0.0.1"
user = "kali"
passwd = "kali"

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=user, password=passwd)

while True:
    stdin, stdout, stderr = client.exec_command(input("Command: "))
    for line in stdout.readlines():
        print(line.strip())

    error = stderr.readlines()
    if error:
        print(error)
