import socket

def connectToServ() :
	address = ("localhost",8008)
	# address = ("192.168.43.193",1200)
	#creating UDP Socket
	clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	while True:
		sentence = input("Enter sentence: ")
		if (sentence == "exit") :
			break
		clientSocket.sendto(sentence.encode(), address)

		msgFromServ, servAddr = clientSocket.recvfrom(2048)
		print("message from server :", msgFromServ.decode())
		 

if __name__ == "__main__":
	try :
		connectToServ()
	except :
		print("couldn't connect to server")