# class Person:
#     """Class to respresent a Person"""
#     def __init__(self):
#       print('custom init', self)
#
# p = Person()

# class Person:
#     """Class to respresent a Person"""
#     def __init__(self):
#         self.first_name = "Erik"
#         self.last_name = "Idle"
#         print('custom init', self)
#
# p = Person()
# print(p.__dict__)

class Person:
    """Class to respresent a Person"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        

p = Person("Erik", "Idle")
print(p.__dict__)