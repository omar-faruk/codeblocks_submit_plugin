#receiving script
import socket
s = socket.socket()
host = '192.168.0.108'
port = 12345
s.bind((host, port))
s.listen(5)
while True:
    c, addr = s.accept()
    l = c.recv(48)
    filename=l
    print filename+" Receiving..."
    f = open(filename,'wb')
    while (l):
        l = c.recv(1024)
        f.write(l)
    f.close()
    print "Done Receiving"
c.close()
s.close()
