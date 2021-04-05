""" lsn14_examples_2ofX.py - example code from lesson 14 """
__author__ = "CS110Z"


# Use a list to store the names of your favorite NFL Quarterbacks
# User must enter each name individually

num_qbs = int(input('How many names do you wish to enter: '))
qb_names = []

for i in range(num_qbs):
    qb_names.append(input('Enter qb %d: ' % i))

# Print out the entered names
for i in range(num_qbs):
    print('%d of %d: %s' % (i, num_qbs, qb_names[i]))
    
    
# Use a list to store the names of your favorite NFL Quarterbacks
# User must enter all names on a line

inputs = input('Enter all qb''s names seprated by a space: ')
qb_names = inputs.split()

for i in range(len(qb_names)):
    print('%d of %d: %s' % (i, len(qb_names), qb_names[i]))