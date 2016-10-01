str=input()
str_list = []
for index in range(len(str)):
    if str[index] >= 'a' and str[index] <= 'z':
        str_list.append(str[index].upper())
    elif str[index] >= 'A' and str[index] <= 'Z':
        str_list.append(str[index].lower())
    else:
        str_list.append(str[index])

print("".join(str_list))
        
