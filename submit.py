import socket,sys,time

s = socket.socket()
filename=sys.argv[1]
host=input("host ip= ")
port = 12345
s.connect((host,port))
index=filename.rindex('\\')+1
fname=filename[index:]
s.send(fname.encode('utf-8'))
time.sleep(.2)
print ('Sending: '+fname)
f = open(filename,'rb')
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
f.close()
print ("Done Sending")
