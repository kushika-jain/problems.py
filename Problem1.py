li=[]
M=int(input())
x=input()
i=0
while i<len(x):
    if x[i]!=';':
        if x[i]=='+':
            li.append(int(x[i+1]))
            i+=1
        elif x[i]=='-':
            li.append(-int(x[i+1]))
            i+=1
        else:
            li.append(int(x[i]))
    i+=1

add=0
for i in range(0,M):
    add=add+li[i]
print(add)
li