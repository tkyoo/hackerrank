n=input()
sticks = input().strip().split(' ')

sticks = [int(stick) for stick in sticks]

sticks.sort()

index = len(sticks) - 1

result = [ -1 ]

while index >= 2:
    if sticks[index - 2] + sticks[index - 1] > sticks[index]:
        result = [ sticks[index - 2], sticks[index - 1], sticks[index] ]
        break
    
    index -= 1

for element in result:
    print(element, end=" ")
