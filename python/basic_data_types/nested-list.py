from functools import cmp_to_key

n=int(input())
studentList=[]
MIN=float(9999)

for x in range(n):
    name=input()
    grade=float(input())
    student=[]
    student.append(name)
    student.append(grade)

    studentList.append(student)
        
def customSort(x, y):
    if x[1] != y[1] :
        return x[1] - y[1]
    else:
        if min(x[0], y[0]) == x[0]:
            return -1
        else:
            return 1
    
studentList = sorted(studentList, key=cmp_to_key(customSort))

index=0
MIN=studentList[index][1]

while index < len(studentList):
    if MIN < studentList[index][1]:
        break
    index += 1
    
grade=studentList[index][1]

while index < len(studentList) and grade == studentList[index][1]:
    print(studentList[index][0])
    grade=studentList[index][1]
    index += 1
