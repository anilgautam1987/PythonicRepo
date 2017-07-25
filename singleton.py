class MySingleton(object):
    
    __instance = None
    
    def __new__(self):
        
        if not self.__instance:
            self.__instance = super(MySingleton,self).__new__(self)
            self.y = 10 
        return self.__instance
    
x = MySingleton()
# get the y value from class
print x.y

# Change Y to 20
x.y = 20

z = MySingleton()
# Retunr the previous object where y has value 20 
print z.y
 
 
def singleton(myclass):
    instances = {}
    def getInstance(*args , **kwargs):
        if myclass not in instances:
            instances[myclass] = myclass(*args,  **kwargs)
        return instances[myclass]
    return getInstance

@singleton
class TestClass(object):
    pass


        