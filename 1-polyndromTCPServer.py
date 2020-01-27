import socket

serverAddr = "localhost"
port = 2000
server = (serverAddr, port)

def reverse(msg) :
	return msg[::-1]

def isPalindrome(msg) :
	#cheking method
	rev = reverse(msg)

	if (msg == rev):
		return True
	return False 

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(server)

#TCP server starts listening
serverSocket.listen(1)

print("TCP Server is ready to receive")

while True:
	connectSocket, clientAddress = serverSocket.accept()
	print("From: ", clientAddress)

	sentence = connectSocket.recv(4096).decode()
	print("Received Message:", sentence)

	rcvMessage = sentence.lower()
	result = isPalindrome(rcvMessage)
	
	if (result) :
		resultMessage = '%s is Palindrome'%format(rcvMessage)
	else:
		resultMessage = '%s is not Palindrome'%format(rcvMessage)
	
	connectSocket.send(resultMessage.encode())
	connectSocket.close()