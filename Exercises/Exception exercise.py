#Author Jake Jones
#D.O.C  09/08/2021

#definefunction to count first 3 lower case letters

def firstThreeLower(instr):

    #check for input type exception
    if not isinstance(instr, str):
        raise ValueError("Invalid input type")

    #check for input length exception
    if len(instr) == 0:
        raise ValueError("Invalid string length")

    #Initialise variable
    result = ""
    lowerCount = 0
    i = 0

    #while more characters in string and less than three lowercase characters found
    while (i < len(instr) and lowerCount < 3):
        #if lowercase letter found
        if (instr[i] >= 'a' and instr[i] <= 'z'):
            #append it to the result
            result = result + instr[i]
            # and increment lowercase counter
            lowerCount = lowerCount+ 1
        #end if
        #increment string counter
        i = i + 1
    #end while
    #return results
    return(result)
#end function

assert firstThreeLower("piano") == "pia",  "Test #1 Fail"
assert firstThreeLower("Cat Dog Fish") == "ato", "test #2 Fail"
assert firstThreeLower("$#@!#fXYYYZu700_-gFER") == "fug", "Test #3 Fail"
assert firstThreeLower("ONLY Two LOWERCASE") == "wo", "Test #4 Fail"
assert firstThreeLower("Elan Sithirasenan") == "lan", "Test #5 Fail"