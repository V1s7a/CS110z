""" lsn14_examples_1ofX.py - example code from lesson 14 """
__author__ = "CS110Z"


# Use a list to store the names of your favorite NFL Quarterbacks
# User must enter each name individually and use a sentiel value
# to halt input.

qb_names = []

qb_name = input('Enter qb name: ')
while qb_name != 'END':
    qb_names.append(qb_name)
    qb_name = input('Enter qb name: ')

# Print out the entered names
for i in range(len(qb_names)):
    print('%d of %d: %s' % (i, len(qb_names), qb_names[i]))
    
# Use a list to store the names of your favorite NFL Quarterbacks
# User must enter all names on a line and use a sentiel value to
# halt input.

inputs = input('Enter all qb''s names seprated by a space: ')
qb_names = inputs.split()
qb_names.remove('END')

for i in range(len(qb_names)):
    print('%d of %d: %s' % (i, len(qb_names), qb_names[i]))