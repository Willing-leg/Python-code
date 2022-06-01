# a collection of items in a particular order, they do not have to be related and are indicated by square brackets []

bicycles = ['trek','cannondale','redline','specialized']

print(bicycles)

#how to access individual items in a list
#lists are ordered by collections, you can access them by telling python the items position(index)

print(bicycles[0])
#you can use title case on it too
print(bicycles[0].title())

#index position starts at 0 not 1

print(bicycles[1])
print(bicycles[3])

#by asking for print(bicycles[-1]) this prints the last item in the list

print(bicycles[-1].title())
#this convention works with other items in the list, -2 will index the second to last item in the list

message = "My first bicycle was a " + bicycles[0].title() + "."


print(message)


friends_names = ['Dylan','Jake','Toby','Ben','Robin','Fin']

print(friends_names[0])

print(friends_names[1])

print(friends_names[2])

print(friends_names[3])

print(friends_names[4])

print(friends_names[5])

print("Your a big slag," + friends_names[0])
print("Your a big slag," + friends_names[1])
print("Your a big slag," + friends_names[2])
print("Your a big slag," + friends_names[3])
print("Your a big slag," + friends_names[4])
print("Your a big slag," + friends_names[5])


transportation = ['car','bus','train','bike','motorbike','on foot']
print('I would like to own a honda ' + transportation[-2])
print(transportation[-1] + ' is not fun.')
print("I can't drive a " + transportation[0])
print('I take the ' + transportation[1] + ' to college.')
print( 'I can ride a ' + transportation[3] +'.')
print('I take the ' + transportation[2] + ' to college.')

#changing, adding and removing elements

motorcycles = ['honda', 'yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

#simple way of adding data to a list this is called appending the item to the list
motorcycles = ['honda', 'yamaha','suzuki']
motorcycles.append('ducati')
print(motorcycles)

del motorcycles[1]
print(motorcycles)

#Removing using the pop() method, if you want to use a value after removing it from a list

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)


motorcycles = ['honda','yamaha','suzuki']

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned.title() + ".")

#popping items from any position in the list, every time you use pop the item you use is no longer in the list

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned.title() + ".")

#Removing an item by value
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)
#you can use the remove method to work with the value thats being removed

motorcycles = ['honda','yamaha','suzuki','ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)

print("\nA " + too_expensive.title() + " its too expensive for me.")






