import math
def max_magnitude(user_val1, user_val2):
    if abs(user_val1) > abs(user_val2):
        return user_val1
    else:
        return user_val2

if __name__ == '__main__':
    # code that uses the function goes here (input, print, call, etc)
    # name and main in the comparison above are bracketed by two underscores
    x = int(input())
    y = int(input())
    
    print(max_magnitude(x,y))