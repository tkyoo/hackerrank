dic={}

n=int(input())

for cnt in range(n):
    line = input().split()
    dic[line[0]] = line[1:]

name=input()

avg = 0.0
for score in dic[name]:
    avg += float(score)
    
avg /= len(dic[name])

print("%.2f" % avg)
    
