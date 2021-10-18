def convert_to_Caesar(str):
    #convert input to upper
    str = str.upper()
	#Variable set to null named newName
    newName = ""
    #for all character in input
    for char in str:
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