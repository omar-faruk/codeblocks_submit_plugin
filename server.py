#receiving script
import socket
s = socket.socket()
tmp=socket.socket()
host = str([(tmp.connect(('8.8.8.8', 80)), tmp.getsockname()[0], tmp.close()) for tmp in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1])
port = 12345
s.bind((host, port))
s.listen(5)
print host+" is listening on port ",port
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
