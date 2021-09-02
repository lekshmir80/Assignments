import socket
#Chat app

PORT = 3007
serv = socket.socket() #Creating socket

serv.bind(("",PORT))
serv.listen(10)
print("Listening")
conn,addr = serv.accept()
print(f"Connected to {addr[0]} on {addr[1]}")
while True:
	data = conn.recv(200)
	print(data)
	
conn.close()	
