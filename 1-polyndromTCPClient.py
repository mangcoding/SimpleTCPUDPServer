import socket

def connectToServ() :
	address = ("localhost",2000)
	# address = ("192.168.43.193",1200)
	while True:
		#creating UDP Socket
		clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

		clientSocket.connect(address)
		sentence = input("Enter sentence: ")
		if (sentence == "exit") :
			clientSocket.close()
			break
		clientSocket.send(sentence.encode())
		
		msgFromServ = clientSocket.recv(4096)
		print("message from server :", msgFromServ.decode())
	
		clientSocket.close()

if __name__ == "__main__":
	try :
		connectToServ()
	except :
		print("couldn't connect to server")