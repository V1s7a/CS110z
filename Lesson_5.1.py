""" lsn05_examples_1of2.py - example code from lesson 5 """
__author__ = "CS110Z"

#  Strings as lists of characters
my_name = 'Troy Weingart'
print('The 6th character of %s is %c' % (my_name, my_name[5]))

# Why is the following incorrect?
"""   
my_name[5] = 'T'
"""
# How would you fix it?

my_name = 'Troy Teingart'

i = 0
while i < 6:
    if i == ' ':
        i+=1
    else:
        print(my_name[i])
        i+=1

# Lists - much more on this later

my_cars = ['Telsa Model 3', 'Acura MDX', 'Volkswagen Beetle']

print(my_cars)

my_cars.append('Toyota Camry')

print(my_cars)

# Tuples - like a list but cannot be changed

my_cars_tuple = ('Telsa Model 3', 'Acura MDX', 'Volkswagen Beetle')

print(my_cars_tuple)

print(len(my_cars_tuple))

# Conversion

x = 10.5
y = int(x)
print(y)

x = 100.5
y = str(x)
print(y)

n = 'the value is 100.5'
z = float(n)

