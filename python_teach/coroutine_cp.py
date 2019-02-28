
def consumer():
    r=''
    while True:
        n=yield r
        if not n:
            return
        print('Consuming %s ...' % n)
        r='200 ok'


def productor(c):
    c.send(None)
    n=0
    while n<5:
        n=n+1
        print("Producting %s ..." % n)
        r=c.send(n)
        print("Consuming return %s..." % r)
    c.close()

c=consumer()
productor(c)