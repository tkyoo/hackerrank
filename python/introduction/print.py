import sys
n=int(raw_input())
cnt=1
while( cnt <= n):
	sys.stdout.write(str(cnt))
	cnt=cnt+1

sys.stdout.flush()
