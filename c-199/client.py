import socket
from threading import Thread

nickname =input("Enter your name ")

ip_address = '127.0.0.1'
port = 8000

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((ip_address,port))

print("Connected with the server")

def receive():
    while True:
        try:
            message=client.recv(2048).decode('utf-8')
            if message=="NICKNAME":
                client.send(nickname.encode('utf-8'))
            else:
                print(message)
        except:
            print("An Error Occured")
            break


def write():
    while True:
        message=f"{nickname}:{input()}"
        client.send(message.encode("utf-8"))
receive_thread = Thread(target=receive)
receive_thread.start()
write_thread = Thread(target=write)
write_thread.start()
