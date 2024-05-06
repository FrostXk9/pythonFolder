# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create a dict
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 200
}

# Use a constructor
# person2 = dict(first_name='Sara', last_name='Williams')

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '10-111'

# get dict keys 
print(person.items())
print(person.keys())

print(person)

# Copy dict
person2 = person.copy()
person2['city'] = 'Cape Town'

# Remove item
del(person['age'])
person.pop('phone')

# Clear
person.clear()

# Get length
print(len(person2))


# list of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kevin', 'age': 25}
]

print(people[1]['name'])

# print(person)