import socket
address = ("localhost",8008)

#creating UDP socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(address)

def reverse(msg) :
	return msg[::-1]

def isPalindrome(msg) :
	#cheking method
	rev = reverse(msg)

	if (msg == rev):
		return True
	return False 


print("The Server is ready to receive")

while True:
	message, clientAddress = serverSocket.recvfrom(2048)
	rcvMessage = message.decode().lower()
	print("Received Message:", rcvMessage)
	print("From: ",clientAddress)
	result = isPalindrome(rcvMessage)

	if (result) :
		resultMessage = '%s is Palindrome'%format(rcvMessage)
	else:
		resultMessage = '%s is not Palindrome'%format(rcvMessage)

	serverSocket.sendto(resultMessage.encode(), clientAddress)

