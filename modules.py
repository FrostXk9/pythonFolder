# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules.


# Core modules
# import datetime
# from date time only import date
from datetime import date
# import time
from time import time

today = date.today()
timeStamp = time()
print(today, timeStamp)

# Pip module
from camelcase import CamelCase

# import custom module
from validator import validate_email

email = 'test@test.com'
if validate_email(email):
    print('Email is valid')
else:
    print('Email is bad')


c = CamelCase()

# the CamelCase() object has a method called hump() 
# when running this it makes each letter of the first word uppercase

print(c.hump('hello there world'))

# pip3 install [module name] - this is how to install a core module for ex pip3 install camelcase
#  pip3 freeze - this is to check all the core modules installed in the package


