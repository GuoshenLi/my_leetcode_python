class A():
    method = 'class'

    def __init__(self):
        self.method = 100
        pass
    #实例方法
    def normethod(self):
        print('I am the normal method')

    #静态方法
    @staticmethod
    def stamethod():
        print ('I am the static method')

    #类方法
    @classmethod
    def clsmethod(cls):
        print (f'I am the {cls.method} method')



a = A()
a.clsmethod()
print(a.method)