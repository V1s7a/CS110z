""" lsn14_examples_4of5.py - example code from lesson 14 """
__author__ = "CS110Z"
import random

my_list = []
# Fill a list with 20 random test scores between 0 and 100
for i in range(20):
    my_list.append(random.randint(0, 100))
                   
# print the list
print(my_list)
    
max = -1
min = 999
sum = 0
index_of_min = 0
index_of_max = 0
for i in range(20):
    # compute sum
    sum += my_list[i]
    
    # find min and where occured in the list
    # what if <= were used vs < ?
    if my_list[i] < min:
        min = my_list[i]
        index_of_min = i
    
    # find max and where occured in the list
    # what if >= were used vs > ?
    if my_list[i] > max:
        max = my_list[i]
        index_of_max = i

print('The sum of all items in the list is %d.' % sum)
print('The min is %d and it is element %d in the list' % (min, index_of_min))
print('The max is %d and it is element %d in the list' % (max, index_of_max))