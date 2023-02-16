a=(input("Enter a string:"))
n=a[0]
new=a[1:]
s=n+new.replace(n,"$")
print(s)
