# 定义一个命名关键字参数函数
def sayHello(name, *, greet='nihao', word):
    print(greet,name, word)
# 调用
sayHello('TOM',greet='hello',word='how are you')
sayHello('TOM',word='how do you do')