import math
l=[]
l_limit=int(input("Enter the lower limit: "))
u_limit=int(input("Enter the upper llmit: "))
for i in range(l_limit,u_limit+1):
    for j in str(i):
        if int(j)%2!=0:
            break
    else:
            s=math.sqrt(i)
            if (s%2==0):
                l.append(i)
print(l)                
