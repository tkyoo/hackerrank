n = int(raw_input())
cmd = raw_input().split()
t1 = ()

for i in range(n):
	t1 += (int(cmd[i]),)

print hash(t1)
