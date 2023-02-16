l1 = [1, 3, 4, 32, 54, 43]
l2 = [6, 4, 3, 12, 34]

if len(l1)>len(l2):
  print("First list is greater")
elif(len(l1)<len(l2)):
  print("Second list is greater")
else:
  print("same")

if sum(l1) == sum(l2):
  print("Same sum")
else:
  print("Different sum")
  
print("Common elements: ", set(l1).intersection(l2))
   

    
