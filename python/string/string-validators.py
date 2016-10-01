line=input()

r1=False
r2=False
r3=False
r4=False
r5=False
for index in range(len(line)):
    if line[index].isalnum():
        r1=True
    if line[index].isalpha():
        r2=True
    if line[index].isdigit():
        r3=True
    if line[index].islower():
        r4=True
    if line[index].isupper():
        r5=True

print(r1)
print(r2)
print(r3)
print(r4)
print(r5)

