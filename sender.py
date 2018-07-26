import socket                   # Import socket module

s = socket.socket()             # Create a socket object
host = '192.168.1.205'	        # Remote Server Address
port = 60000                    # Reserve a port for your service.
filename = "02_Rozana_SongsMp3_Com_.wav"
addr=(host,port)
buf=1024

s.connect((host, port))
s.sendto(filename,addr)
status = s.recv(128)
print status
f=open(filename,"rb")
data = f.read(buf)
while (data):
    if(s.sendto(data,addr)):
        print "sending ..."
        data = f.read(buf)

print('Successfully sent the file')
f.close()
s.close()
print('connection closed')
