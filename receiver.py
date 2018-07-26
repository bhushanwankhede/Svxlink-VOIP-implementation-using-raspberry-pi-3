import socket                   # Import socket module

port = 60000                    # Reserve a port for your service.
s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
s.bind(('192.168.1.202', port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print 'Server listening....'

conn, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
filename = conn.recv(1024)
print('Receiving', repr(filename))
f = open(r'/home/pi/'+filename, 'wb')
conn.send('200ok')
print('Receiving Data')

with open(filename, 'wb') as f:
    print 'file opened'
    while True:
        print('receiving data...')
        data = conn.recv(1024)
        print('data=%s', (data))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()







print('Done receiving')
conn.send('Thank you for connecting')
conn.close()
