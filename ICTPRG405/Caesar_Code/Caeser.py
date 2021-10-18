#Author Jake Jones
#Date 23/08/2021
#API main program used for Caeser Encryptor

#Import modules into main program
from Task1 import convert_to_Caesar
from Task2 import caesar_Cipher
#import system functions
import sys


if len(sys.argv) < 3:
    print("two arguements expected")
elif not sys.argv[1].isdigit():
    print("Invalid input, please enter numeric value to shift")
elif type(sys.argv[2]) != str:
    print ("Invalid input, please input phrase to encode")

    
else:

    #try to use other modules with command line input as arguements, catch errors and test code
    try:
        #command line arguements input
        str1 = sys.argv[2]
        shift = int(sys.argv[1])
        #use convert_to_caesar with first command line input, assign return value to variable called 
        convertedText = convert_to_Caesar(str1)
        encriptedText = caesar_Cipher(convertedText, shift)
        print (encriptedText)
    except ValueError as err:
        print("Error", err)

assert convert_to_Caesar("Hello there") == "HELLOTHERE", "Test 1 Fail"
assert convert_to_Caesar("AppLE") == "APPLE", "Test 2 Fail"
assert convert_to_Caesar("ELanISgreaT") == "ELANISGREAT", "Test 3 Fail"
assert convert_to_Caesar("HEshouldmarkme") == "HESHOULDMARKME", "Test 4 fail"
assert convert_to_Caesar("ReallyHIGH100%") == "REALLYHIGH", "Test 5 fail"
assert convert_to_Caesar("Kuz he is kind :)") == "KUZHEISKIND", "Test 6 Fail"
assert convert_to_Caesar(" rawr ") == "RAWR", "Test 7 Fail"
assert convert_to_Caesar("IsaacTouchedME") == "ISAACTOUCHEDME", "Test 8 Fail"
assert convert_to_Caesar("@#%#$)*^#^*)#@($%^") == "", "Test 9 Fail"
assert convert_to_Caesar("Pew Pew") == "PEWPEW", "Test 10 Fail"

assert caesar_Cipher("ISAACWASGENTLE",3) == "LVDDFZDVJHQWOH", "Test 1 Fail"
assert caesar_Cipher("BUTHADANIMALISTIC",7)== "IBAOHKHUPTHSPZAPJ", "Test 2 Fail"
assert caesar_Cipher("VIGOURWASPUNGENT",-4) == "RECKQNSWOLQJCAJP", "Test 3 Fail"
assert caesar_Cipher("PLAYERHASENTEREDTHEGAME",-1) == "OKZXDQGZRDMSDQDCSGDFZLD", "Test 4 Fail"
assert caesar_Cipher("KERMITWORKFORALQAEDA",5) =="PJWRNYBTWPKTWFQVFJIF", "Test 5 Fail"
assert caesar_Cipher("SEANBEENPALMPILOTING",7) == "ZLHUILLUWHSTWPSVAPUN", "Test 6 Fail"
assert caesar_Cipher("FORASLONGASHEREMEMBERS",1) == "GPSBTMPOHBTIFSFNFNCFST", "Test 7 Fail"
assert caesar_Cipher("SEANSGIRLFRIEND",-1) == "RDZMRFHQKEQHDMC", "Test 8 Fail"
assert caesar_Cipher("SAYSHEHASGREYHAIRSNOW",6) == "YGEYNKNGYMXKENGOXYTUC", "Test 9 Fail"
assert caesar_Cipher("DONTFAILMEPLZ",8) == "LWVBNIQTUMXTH", "Test 10 Fail"
