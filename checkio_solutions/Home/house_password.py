#!/usr/bin/env checkio --domain=py run house-password

# https://py.checkio.org/mission/house-password/

# 
# END_DESC

def checkio(data: str) -> bool:

    #replace this for solution
    #--flags--#
    upper = False
    lower = False
    digit = False
    length = False
    
    if len(data) >= 10:
        length = True
        print("LENGTH")
    for x in data:
        if x.isupper() and upper == False: #the loop stops when it finds atleast one uppercase
            print("UPPER") #print for debugging
            upper = True #setting the flag as true
        if x.isdigit() and digit == False:
            print("DIGIT")
            digit = True
        if x.islower() and lower == False:
            print("LOWER")
            lower = True
    if upper and lower and digit and length == True: #checks if all the flags are true
        return True
    return False
        

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == True, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")