def onlydigits(instr):
	#Variable set to null named newName
    newStr= ""
    #for all integer in input
    for char in instr:
        #if character is between range of 0 - 9
        if char >= "0" and char <= "9":
            #Attach current character to newname variable
            newStr = newStr + char
        #otherwise
        else:
            #do nothing
            pass
         #end if
    #end for
    #return value of newname to function
    return (newStr)

# Test 1
result= onlydigits("la545la")
if (result == "545"):
  print('Test 1 OK')
else:
  print('Test 1 error: ' + result)


# Test 2
result= onlydigits("hew009hew..")
if (result == '009'):
  print('Test 2 OK')
else:
  print('Test 2 error: ' + result)
