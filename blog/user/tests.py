from django.test import TestCase

# Create your tests here.

class Tedu:
    def __init__(self):
        self.name = 'xiaowang'

a = Tedu()


print(hasattr(a,'age')) 

setattr(a,'age',18)
print(a.age)
print('----------------')
print(getattr(a,'age'))