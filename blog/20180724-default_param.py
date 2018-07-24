# 定义具有默认参数的函数
def sayHello(name,greet='Hello'):
    print(greet,name)
# 调用函数
sayHello('Abra')
sayHello('Abra','Hey')

def sayHello(name,greet='hello',word='how are you?'):
    print(greet,name,word)

sayHello('Abra',word = 'are you Ok?')