from Library import countUpper, convertUpper, convertUpper2, sortString

string = input("what is your sentence?")
count = countUpper(string)

print (f"The orignal count is {count}")

string1 = convertUpper(string)
print(string1)

alphaOnly = convertUpper2(string)
print(alphaOnly)

alphaBet = sortString(alphaOnly)
print(alphaBet)