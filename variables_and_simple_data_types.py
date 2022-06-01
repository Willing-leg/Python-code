
# page 26 


message = "Hello Python World!"
print(message)

message_2 = "Hello Python Crash Course World!"
print(message)


message_3 = "Dylan is a slag:)"

print(message_3)

message_4 = "Jake is a slag"

print(message_4)


name = "ethan rawstron"
print(name.title())

print(name.upper())
print(name.lower())

first_name = "ethan"
last_name = "rawstron"
full_name = first_name + " " + last_name
print(full_name)

print("Hello, " + full_name.title() + "!")

message_5 = "Hello, " + full_name.title() + "!"

print(message_5)

print("\tPython")

print("Languages:\nPython\nC\nJavaScript")


favorite_language = ' python '

print(favorite_language + " is great")

print(favorite_language.rstrip() + ' is great!')

favorite_language = favorite_language.rstrip()


print(favorite_language.rstrip() + ' is the best!')

print("I don't know what to write " + favorite_language)


print("I don't know what to write " + favorite_language.lstrip())

favorite_language = '      python      '

print("I don't know what to write " + favorite_language + "is the best!")

print("I don't know what to write " + favorite_language.strip() + " is the best!")


#integers
#you can add,subtract,multiply and divide integers in python

print(2+3) 
#5
print(3-2)
#1
print(2*3)
#6
print(3/2)
#1.5




print(3**2)
#9
print(3**3)
#27
print(10**6)
#1000000

#order of operations 
print(2+3*4)
#14
print((2+3)*4)
#20

#Floats, numbers with a decimal point



# you can sometimes get an arbitrary number when combining decimal numbers

age = 23
# message_birthday = "Happy " + age + "rd Birthday!"
# print(message_birthday)     this will display an error message, you python does not know how to combine int and str values 

message_birthday = "Happy " + str(age) + "rd Birthday!"

print(message_birthday)

