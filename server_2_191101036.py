import socket

serverPort = 12001
serverName = "192.168.0.16"

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
serverSocket.bind((serverName,serverPort))
serverSocket.listen(3)
name = None
num = None
time = None
security_code = None

#while True:

serverSocket, information = serverSocket.accept()
byte_message = bytes(">İsim ve soyisminiz:","utf-8")
serverSocket.send(byte_message)
byte_sentence = serverSocket.recv(1024)
name = byte_sentence.decode("utf-8")

byte_message1 = bytes(">Kredi kartı numaranız:","utf-8")
serverSocket.send(byte_message1)
byte_sentence1 = serverSocket.recv(1024)
num = byte_sentence1.decode("utf-8")

byte_message2 = bytes(">Geçerlilik süresi","utf-8")
serverSocket.send(byte_message2)
byte_sentece2 = serverSocket.recv(1024)
time = byte_sentece2.decode("utf-8")

byte_message3 = bytes(">Güvenlik kodu","utf-8")
serverSocket.send(byte_message3)
byte_sentence3 = serverSocket.recv(1024)
security_code = byte_sentence3.decode("utf-8")
serverSocket.close()

folder = open(name + ".txt","w")
folder.write(num + "\n")
folder.write(time + "\n")
folder.write(security_code)
folder.close()