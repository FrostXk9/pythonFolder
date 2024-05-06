# JSON is commonly used with data API's.Here how we can parse JSON into a python  dictionary

import json

# Sample json
userJson = '{"first_name": "John", "Last_name" : "Doe", "age": 26}'

# Parse to a dictionary 
user = json.loads(userJson)

print(user)
print(user['first_name'])

# python dictionary
car = {'make': 'Ford', 'model' : 'Mustang', 'year' : 1970}

carJSON = json.dumps(car)

print(carJSON)

