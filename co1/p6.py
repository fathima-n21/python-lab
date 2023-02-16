n = int(input("Enter the size: "))
l=[]
for i in range(n):
  l.append(input("Enter name: "))
print(l)
di = dict()
for i in l:
  di[i] = i.count('a')
print(dict(sorted(di.items(), key = lambda t:t[1], reverse = True)))



