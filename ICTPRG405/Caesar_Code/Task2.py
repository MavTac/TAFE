#Author Jake Jones
#Date 16/08/2021
#API Caesar_code/Part 1

#This module is made to do the following:
	#take converted text input and traverse the string
	#shift the character by provided amount through shift value (input)
	#return encrypted string to function

#Define function for Caesar cipher
def caesar_Cipher(str, shift):
   
    #if shift is not an numerical value
    if not isinstance(shift,int):
        #raise error and ask for numerical input
        raise ValueError("Please input numerical value")
    #if input is null
    elif len(str) == 0:
        #ask for valid input string
        raise ValueError("Invalid string length")
#set return result to null
    result = ""
#for characters in input string
    for i in range(len(str)):
        #set character value to transverse the string input
        char = str[i]
        #if character is upper case
        if (char.isupper()):
                #convert character to Ascii value, take 65 from character, use remainder for mod expression "x % 26". add 65 onto this result to obtain correct Ascii Value
                result += chr((ord(char) + shift -65) % 26 + 65)
        #Anything other than above
        else:      
            #do nothing
                pass
        #end if
    #return result to function
    return (result)
    #end for
#fin



