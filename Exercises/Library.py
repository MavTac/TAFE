def countUpper(str):
    count = 0
    for ch in str:
        if ch >= "A" and ch <= "Z":
            count = count + 1
    return(count)
def convertUpper(str):
    newstr = ""
    for ch in str:
        if ch >= "a" and ch <= "z" :
            newstr = newstr + chr(ord(ch)-32)
        else:
            newstr = newstr + ch

    return (newstr)

def convertUpper2(str):
    newstr1=convertUpper(str)
    newstr2=""
    for ch in newstr1:
        if ch >= 'A' and ch <= "Z":
            newstr2 = newstr2 + ch
    return(newstr2)
def sortString(str):
    return ''.join(sorted(str))
