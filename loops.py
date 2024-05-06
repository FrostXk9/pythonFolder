# A for loop is used for iterating over a sequence (that is either a list, tuple, a dictionary, a set, or a string)

people = [' John ', ' Paul ', ' Sara ', ' Susan']

# Simple for loop
# for person in people:
#     print(f'Current person: {person}')
    
    
    
#break
# for person in people:
#     if person == 'Sara':
#         break
#     print(f'Current person: {person}')
    
#continue
# for person in people:
#     if person == 'Sara':
#         continue
#     print(f'Current person: {person}')
    
    
    
for i in range(len(people)):
    print(people[i])
    
for i in range(0, 11):
    print(f'Number: {i}')
    

# While loops execute a set of statements as a long term condition is true

count = 0
while count <= 10:
    print(f'Count: {count}')
    count += 1