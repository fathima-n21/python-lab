s = input("Enter string: ")
l = s.split()
big = l[0]
for i in range(1, len(l)):
  if len(big) < len(l[i]):
    big = l[i]
print("Longest word:",big,"\nLength: ", len(big))
       
