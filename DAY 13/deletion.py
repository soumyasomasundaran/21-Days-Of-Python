person = {'Name': 'Alex',
          'Age': 19,
          'Marks': [50, 60, 70],
          'Place': 'Chennai'
          }

# pop()
person.pop('Name')
print(person)

# popitem()
person.popitem()
print(person)

# del

del person['Age']
print(person)

# clear
person.clear()
print(person)
