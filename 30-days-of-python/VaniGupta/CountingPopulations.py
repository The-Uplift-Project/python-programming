## Given a list of dictionaries representing user preferences
## First: Write a function to count the number users whose favorite genre is "Comedy"
## Next: Create a function that returns the population of users for every favorite genre
## Stretch: Count the population of the given user preference key rather than a specific population

users = [
  {"name": "Victor", "favorite genre": "Comedy"},
  {"name": "Valerie", "favorite genre": "Drama"},
  {"name": "Ada", "favorite genre": "Action"},
  {"name": "Pascal", "favorite genre": "Comedy"},
  {"name": "Eve", "favorite genre": "Documentary"},
  {"name": "Alice", "favorite genre": "Action"},
  {"name": "Bob", "favorite genre": "Comedy"},
  {"name": "Erin", "favorite genre": "Romance"},
  {"name": "Geneva", "favorite genre": "Drama"},
  {"name": "Carl", "favorite genre": "Comedy"},
  {"name": "Eve", "favorite genre": "Comedy"},
  {"name": "Charlie", "favorite genre": "Action"},
  {"name": "Dan", "favorite genre": "Comedy"},
  {"name": "Faythe", "favorite genre": "Romance"},
  {"name": "Grace", "favorite genre": "Drama"},
  {"name": "Heidi", "favorite genre": "Romance"},
  {"name": "Ivan", "favorite genre": "Comedy"},
  {"name": "Judy", "favorite genre": "Romance"},
  {"name": "Mallory", "favorite genre": "Drama"},
  {"name": "Michael", "favorite genre": "Comedy"},
  {"name": "Niaj", "favorite genre": "Romance"},
  {"name": "Olivia", "favorite genre": "Drama"},
  {"name": "Oscar", "favorite genre": "Action"},
  {"name": "Peggy", "favorite genre": "Documentary"},
  {"name": "Pat", "favorite genre": "Documentary"},
  {"name": "Rupert", "favorite genre": "Action"},
  {"name": "Merlin", "favorite genre": "Documentary"},
]

## There are 8 Comedy Lovers in the list above - write a loop to determine that

c = 0
for i in users:
  if i['favorite genre'] == 'Comedy':
    c += 1
print(c)

## Next, write a function to return a dict like this:
# population = {'Comedy': 8, 'Drama': 5, 'Action': 5, 'Documentary': 4, 'Romance': 5}

population = {}
for i in users:
  population[i['favorite genre']] = population.get(i['favorite genre'], 0) + 1
  
print(population)

## Last, try to write a function like the one below: 

def populations(input_list,key):
  population = {}
  for i in input_list:
    population[i['name']] = population.get(i['name'], 0) + 1
  return population

## This function call:
print(populations(users,"name"))

## should return this
# populations_return_value = {'Victor': 1, 'Valerie': 1, 'Ada': 1, 'Pascal': 1, 'Eve': 2, 'Alice': 1, 'Bob': 1, 'Erin': 1, 
# 'Geneva': 1, 'Carl': 1, 'Charlie': 1, 'Dan': 1, 'Faythe': 1, 'Grace': 1, 'Heidi': 1, 'Ivan': 1, 'Judy': 1, 'Mallory': 1, 
# 'Michael': 1, 'Niaj': 1, 'Olivia': 1, 'Oscar': 1, 'Peggy': 1, 'Pat': 1, 'Rupert': 1, 'Merlin': 1}
