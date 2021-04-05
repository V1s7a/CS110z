def seconds_to_jiffies(user_seconds):
    x = user_seconds*100
    return float(x)

if __name__ == '__main__':
    # code that uses the function goes here (input, print, call, etc)
    # name and main in the comparison above are bracketed by two underscore
    seconds = int(input())
    print('%0.2f' % seconds_to_jiffies(seconds))
        
        


