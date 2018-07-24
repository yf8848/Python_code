# 定义一个关键字参数
def sayHello(**saySomething):
    print(saySomething)

# 调用关键字参数的函数
sayHello(name='TOM',greet='hello',word='How do you do')
sayHello(name='BOBO',word='how are you')
sayHello(name='JHON')

para = {'name':'BOBO','greet':'nihao'}
# 调用
sayHello(**para)
