list=[]
n=int(input())
values=input().split()
MAX=int(0)
secondMax=int(0)

for value in values:
    list.append(int(value))

list.sort()

MAX=list[ len(list) - 1]
secondMax=list[0]

index = len(list) - 1

while index >= 0:
    value = list[index]

    if value != MAX:
        secondMax = value
        break
    
    index -= 1

print(secondMax)
