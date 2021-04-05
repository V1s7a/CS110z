# ---------------------------------------------------------------------
# Lab: HW6-1
# Author: Colton Willits
# Course: CS110Z, Fall 2019
# --------------------------------------------------------------------

num = int(input("Please input squadron"))


def main():
    if num <= 0 or num >=41:
        print("Invalid")
    if num < 30 or num >= 40:
        print("1")
        return()
    if num <=21 or num >= 30:
        print("2")
        return()
    if num <= 11 or num >= 20:
        print("3")
        return()
    if num <= 1 or num >=10:
        print("4")
    
main()
