import textwrap
str=input()
wrapped=textwrap.wrap(str,int(input()))
for e in wrapped:
    print(e)
