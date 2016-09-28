lists=[]
n=int(raw_input())

for cnt in xrange(n):
	cmd = raw_input()
	cmd = cmd.split()
	if cmd[0] == "insert":
		lists.insert(int(cmd[1]), int(cmd[2]))
	elif cmd[0] == "append":
		lists.append(int(cmd[1]))
	elif cmd[0] == "reverse":
		lists.reverse()
	elif cmd[0] == "sort":
		lists.sort()
	elif cmd[0] == "print":
		print(lists)
	elif cmd[0] == "remove":
		lists.remove(int(cmd[1]))
	elif cmd[0] == "pop":
		lists.pop()
