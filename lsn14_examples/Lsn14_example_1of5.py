""" lsn14_examples_1ofX.py - example code from lesson 14 """
__author__ = "CS110Z"

# Initialize a list with the following values 1, 23, 57, 98

my_list = [1, 23, 57, 98]
print(my_list)

# Change the 2nd element from a 23 to a -57

my_list[1] = -57
print(my_list)

# print the last element in the list
print(my_list[-1])

# add 10 to each element of the list
for i in range(len(my_list)):
    my_list[i] += 10
    
print(my_list)