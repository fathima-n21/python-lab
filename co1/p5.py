l=[]
n=4
print("Enter the numbers:")
for i in range(n):
    num=int(input())
    l.append(num)
print(l)
for i in range(len(l)):
    if(l[i]>100):
        l[i]="Over"
print(l)
