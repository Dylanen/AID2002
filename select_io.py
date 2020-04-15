from select import select
from socket import *
s=socket()
s.bind(('127.0.0.1',8080))
s.listen(3)
s.setblocking(False)

rlist=[s]
wlist=[]
xlist=[]
while True:
    rs,ws,xs=select(rlist,wlist,xlist)
    for r  in rs:
        if r is s:
            c,addr=r.accept()
            print('connect,from:',addr)
            c.setblocking(False)
            rlist.append(c)
        else:
            data=r.recv(1024).decode()
            if not data:
                rlist.remove(r)
                r.cloce()
                continue
            print(data)
            wlist.append(r)
            # r.send(b'ok')
    for w in ws:
        w.send(b'ok')
        wlist.remove(w)
    for x in xs:
        pass
