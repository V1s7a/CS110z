def miles_to_laps(user_miles):
    x = user_miles/0.25
    return x


if __name__ == '__main__':
    # code that uses the function goes here (input, print, call, etc)
    # name and main in the comparison above are bracketed by two underscores
    x = float(input())
    print('%0.2f' % miles_to_laps(x))
    