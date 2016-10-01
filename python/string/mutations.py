line=input()
strBuffer=list(line)
line=input().split(" ")
strBuffer[int(line[0])] = line[1]
print("".join(strBuffer))
