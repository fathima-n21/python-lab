list=[]
n=int(input("Enter the number of items in the list: "))
print("Enter the items:")
for i in range(n):
    n=int(input())
    list.append(n)
total=0
for i in range(0,len(list)):
    total=total+list[i]
print("The sum of all items in the list is:",total)    
    
    
    
