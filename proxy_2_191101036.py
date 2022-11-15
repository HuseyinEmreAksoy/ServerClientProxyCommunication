import socket

socket1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_port = 12001
bank_port = 12002
server_name = "192.168.0.16"

socket1.bind((server_name, bank_port))
socket1.listen(3)
socket2.connect((server_name, server_port))

bank, data = socket1.accept()
info = socket2.recv(1024)

print("Bank message > " + info.decode("utf-8"))
bank.send(info)
client_info = bank.recv(1024)

print("Client message > " + client_info.decode())
socket2.send(client_info)
info2 = socket2.recv(1024)

print("Bank message > " + info2.decode("utf-8"))
bank.send(info2)
client_info2 = bank.recv(1024)

print("Client message > " + client_info2.decode())
socket2.send(client_info2)
info3 = socket2.recv(1024)

print("Bank message > " + info3.decode("utf-8"))
bank.send(info3)
client_info3 = bank.recv(1024)

print("Client message > " + client_info3.decode())
socket2.send(client_info3)
info4 = socket2.recv(1024)

print("Bank message > " + info4.decode("utf-8"))
bank.send(info4)
client_info4 = bank.recv(1024)

print("Client message > " + client_info4.decode())
socket2.send(client_info4)

socket1.close()
socket2.close()


