str=input()
substr=input()
cnt=0
found=0

while found != -1:
    found = str.find(substr,found)
    if found != -1:
        found += 1
        cnt += 1
        
print(cnt)
