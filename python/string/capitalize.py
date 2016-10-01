str=input()
beforeFlag = True
strBuffer = []

for index in range(len(str)):
    if beforeFlag and str[index] != " ":
        strBuffer.append(str[index].upper())
        beforeFlag=False
    else:
        if str[index] == " ":
            beforeFlag=True
        strBuffer.append(str[index])

print("".join(strBuffer))
