class Car:
    def __init__(self, model, speed):
        self.model = model
        self.speed = speed
    
    def forward(self):
        print('Ready! Go!')
        
        
class Ford(Car):
    
    def __init__(self, model, speed, engine, secret):
        self.__secret = secret
        super().__init__(model, speed)
        self.engine = engine
    
    
    @property
    def secret(self):
        return self.__secret
    
    
    @secret.setter
    def secret(self, new):
        if len(new) <= 3:
            raise ValueError('Неверное значение')
        else:
            self.__secret = new
            return self.__secret
            
        
    def run(self):
        print(f'{self.model} RUN!')

# audi = Car('Audi S8', 50)
# print(audi.model)
# 
# bmw = Car('BMW M3', 45)
# print(bmw.model)

mustang = Ford('Mustang', 100, 'V8', 'Design')
mustang.secret = 'bla'
print(mustang.secret)

# mustang.run()
# print(mustang.engine)


# def test(*n):
#     print(n)
#     for i in n:
#         print(i*2)
# 
# test(12,3,3,534,23,32)

# def test2(**kwargs):
#     print(kwargs)
#     
# test2(name = 'Ivan', age=15)