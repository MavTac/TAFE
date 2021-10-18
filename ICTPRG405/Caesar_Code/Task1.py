#author Jake Jones
#Date 26/07/21
#API Ceasar code/ Part 1

#Function to be used by system to convert input string into usable format
#for Caesar encoding, Acceptable format is as follows:
    #Convert string into uppercase
    # No spaces
    # "." will be replaced with "X"
    # anything outside rang of A-Z will be ignored

#expected input is various length of string

#Create function called convert_to_Caesar
def convert_to_Caesar(instr):
    #convert input to upper
    instr = instr.upper()
	#Variable set to null named newName
    newName = ""
    #for all character in input
    for char in instr:
        #raise error if null input
        if len(instr) == 0:
            raise ValueError("Invalid string length")
        #if character is uppercase from A to Z
        if char >= 'A'and char <= "Z":
            #Attach current character to newname variable
            newName = newName + char
        #if character is “.”
        if char == ".":
            #replace newname value with 'X'
            newName = newName + "X"
        #if anything else

        else:
            #do nothing
            pass
         #end if
    #end for
    #return value of newname to function
    return (newName)
#fin
