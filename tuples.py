# A Tuple is a collection which is ordered and unchangable. Allows duplicate members.

# Create tuple
fruits = ('Apples', 'Oranges', 'Grapes') # If no trailing comma its type is identified as a string(str)
# fruits2 = tuple(('Apples', 'Oranges', 'Grapes'))

# Single value needs trailing comma
fruits2 = ('Apples',)

# Get value
print(fruits[1])

# Cant change the value
# fruits[0] = 'Pears'


# Delete a tuple
del fruits2

print(len(fruits))

# A set is a collection which is unoredered and unindexed. No duplicate members

# Create a set 
fruits_set = {'Apples', 'Oranges', 'Mango'}


# Check if in a set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grape')

# Add duplicate
fruits_set.add('Apples')
# Result in no erroe but will not add a duplicate to the set

# Remove from set
fruits_set.remove('Grape')

# Clear set
fruits_set.clear()

print(fruits_set)