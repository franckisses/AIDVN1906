from django.test import TestCase
from functools import wraps

# Create your tests here.

import time

def timer(func):
    @wraps(func)
    def inner(*args,**kwargs):
        """this is inner func"""
        print('innner')
        a = 1
        return a
    return inner

@timer
def func_test():
    """nihao  这是func_test"""
    return 

print(func_test.__name__) # func_test
print(func_test.__doc__)  # """nihao  这是func_test"""

