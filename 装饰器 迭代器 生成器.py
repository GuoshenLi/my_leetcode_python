# 闭包
def create_adder(x):
    def adder(y):
        return x + y
    return adder


add_15 = create_adder(15)
print(add_15(10))



# 装饰器

def decor1(func):
    def inner():
        x = func()
        return x * x
    return inner

@decor1
def num():
    return 10

print(num())