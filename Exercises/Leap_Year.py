#isleap(): method that takes an integer year number and
#returns True if that year is a leap year, False otherwise
def isleap(year):
    #if the year is divisable by 4, it's a leap year
    if(year % 400 ==0):
        return(True)
    #if the year is divisable by 100, not a leap year
    if (year % 100 == 0):
         return(False)

    #If the year is divisable by 400, a leap year
    if(year % 4 == 0):
        return(True)

    #every other year is not a leap year
    return(False)
#unti tests
assert isleap(2019) == False, "Test #1 FAIL"
assert isleap(2020) == True,  "Test #2 FAIL"
assert isleap(2016) == True,  "Test #3 FAIL"
assert isleap(2003) == False, "Test #4 FAIL"
assert isleap(1964) == True,  "Test #5 FAIL"
assert isleap(1900) == False, "Test #6 FAIL"
assert isleap(1800) == False, "Test #7 FAIL"
assert isleap(1700) == False, "Test #8 FAIL"
assert isleap(1600) == True,  "Test #9 FAIL"
