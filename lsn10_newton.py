import math

def newtons_method(number, num_iters):
    approx = 1/2 * number
    for i in range(0, num_iters):
        better = (1/2)*(approx + number/approx)
        approx = better
    return approx

#ask for inputs
#call function
