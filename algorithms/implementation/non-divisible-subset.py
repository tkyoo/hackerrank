nk = input().split(' ')
n = int(nk[0])
k = int(nk[1])

arr = [int(c_temp) for c_temp in input().strip().split(' ')]

a = {}

for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if (arr[i] + arr[j]) % k != 0:
            a[arr[i]] = 1
            a[arr[j]] = 1

print(len(a))
