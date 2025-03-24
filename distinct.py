Y = int(input("enter a year loser"))

def next_distinct_year(Y):
    checking = True
    while checking == True: 
        Y += 1
        digit_unique = False
        zero = False
        one = False
        two = False
        three = False
        four = False
        five = False 
        six = False
        seven = False
        eight = False
        nine = False
        for digit in str(Y).split():
            if digit == "0":
                if zero == True:
                    digit_unique = False
                    break
                else:
                    zero = True
            if digit == "1":
                if one == True:
                    digit_unique = False
                    break
                else:
                    one = True
            if digit == "2":
                if two == True:
                    digit_unique = False
                    break
                else:
                    two = True
            if digit == "3":
                if three == True:
                    digit_unique = False
                    break
                else:
                    three = True
            if digit == "4":
                if four == True:
                    digit_unique = False
                    break
                else:
                    four = True
            if digit == "5":
                if five == True:
                    digit_unique = False
                    break
                else:
                    five = True
            if digit == "6":
                if six == True:
                    digit_unique = False
                    break
                else:
                    six = True
            if digit == "7":
                if seven == True:
                    digit_unique = False
                    break
                else:
                    seven = True
            if digit == "8":
                if eight == True:
                    digit_unique = False
                    break
                else:
                    eight = True
            if digit == "9":
                if nine == True:
                    digit_unique = False
                    break
                else:
                    nine = True
    if digit_unique != False:
        checking = False
        print(Y)

next_distinct_year(Y)