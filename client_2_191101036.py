import socket

serverName = "192.168.0.16"
serverPort = 12002
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#while True:

clientSocket.connect((serverName, serverPort))
message = clientSocket.recv(1024)
print(message.decode("utf-8"))
name = input()
bytes_name = bytes(name,"utf-8")

clientSocket.send(bytes_name)
message1 = clientSocket.recv(1024)
print(message1.decode("utf-8"))

credit_num = input()
byte_credit = bytes(credit_num,"utf-8")

clientSocket.send(byte_credit)
message2 = clientSocket.recv(1024)
print(message2.decode("utf-8"))

time = input()
byte_time = bytes(time,"utf-8")

clientSocket.send(byte_time)

message3 = clientSocket.recv(1024)
print(message3.decode("utf-8"))

security_code = input()
byte_security_code = bytes(security_code,"utf-8")
clientSocket.send(byte_security_code)
clientSocket.close()