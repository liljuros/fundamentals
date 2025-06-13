class Person:
    '''This string can be used to document the class -
    caleld a docstring'''

p1 = Person

p1.__name__ = 'John'
print(p1.__dict__)
p1.first_name = 'Smurf'
p1.last_name = 'gargamel'
print(p1.__dict__)