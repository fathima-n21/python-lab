l=[]
n=int(input("Enter the limit:"))
print("Enter the colors:")
for i in range(0,n):
    val=(input())
    l.append(val)
print("Colors are:",l)
print(l[::len(l)-1])
