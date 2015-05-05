import socket,sys,time,platform

s = socket.socket()
filename=sys.argv[1]

host=raw_input("host ip= ")
port = 12345
s.connect((host,port))

if(platform.system() is 'Linux' or 'Linux'):
	index=filename.rindex('/')+1  
elif(platform.system() is 'Windows' or 'windows'):
	index=filename.rindex('\\')+1
	
if(index>0):
	fname=filename[index:]
else:
	fname=filename
	
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
