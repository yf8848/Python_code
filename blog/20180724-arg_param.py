def sayHello(*saySomething):
    for tmp in saySomething:
        print(tmp)

sayHello('Sawadika','Jarry')
sayHello('nihao','BOBO','how do you do ?')
sayHello('hello','Tom','how are you ?')


somethings = ['nihao','Zhangye','how do you do ?']
sayHello(*somethings)