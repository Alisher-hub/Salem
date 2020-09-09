def learning(self):
    print("It's Time to Learn!")

def show_cost(self):
    print(f'Cost: {self.cost}')

info = {
    'subject':'Geographic',
    'cost':'life',
    'source':'',
    'learning':learning,
    'show_cost':show_cost
    }

class UpperMetaclass(type):
    def __new__(upperattr_metaclass, future_class, future_parents, future_attrs):
        new_attrs = dict()
        for name, value in future_attrs.items():
            if not name.endswith('__'):
                new_attrs[name.upper()] = value
        
        return type.__new__(upperattr_metaclass,future_class, (future_parents), new_attrs)


from six import with_metaclass

class Test(metaclass=UpperMetaclass):
    
    stakan = 'big'
    
t = Test()
print(t)