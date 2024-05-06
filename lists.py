# A List is a collection which is ordered and changeable. Allows duplicate members

# Create a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
fruits = ['Apples', 'Oranges', 'Grapes', 'Bannana']

# Use a constructor 
# numbers2 = list((1, 2, 3, 4 ,5 , 6, 7, 8, 9))
# print(numbers, numbers2)

# Get a value
print(fruits[1])

# Get a length
print(len(fruits))

# Append to list
fruits.append('Mango')

# Remove from list
fruits.remove('Grapes')

# Insert into a position
fruits.insert(2, 'Strawberries')

# Change value
fruits[0] = 'Blueberries'

# Remove with pop
fruits.pop(2)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Reverse Sort
fruits.sort(reverse=True)

print(fruits)