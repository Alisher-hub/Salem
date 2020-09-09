# a = 5
# b = 'test'
# 
# def f():
#     pass
# 
# class Test():
#     pass

# print(a.__class__.__class__)
# print(b.__class__.__class__)
# print(f.__class__.__class__)
# print(type(Test))
# print(type(type))


# def create_info(info):
#     if info == 'learn':
#         class Learn:
#             pass
#         
#         return Learn
#     else:
#         class Simple:
#             pass
#         
#         return Simple
# 
# cls = create_info('learn')
# print(cls())

# class Learn():
#     pass

# l = Learn()
# print(l.__class__)

# type(<имя создаваемого класса>, <кортеж из родительских классов>,<словарь с полями и методами>)

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

# Study = type('Study',(), info)
# # print(type(Study))
# s = Study()
# print(s.subject)
# s.show_cost()
# 
# StudyChild = type('StudyChild',(Study,), {})
# print(StudyChild)


def upper_attr(future_class, future_parents, future_attrs):
    new_attrs = dict()
    for name, value in future_attrs.items():
        if not name.endswith('__'):
            new_attrs[name.upper()] = value
    
    return type(future_class, (future_parents,), new_attrs)
    
    


class Test(upper_attr):
    stakan = 'big'

t = Test()

print(t.STAKAN)