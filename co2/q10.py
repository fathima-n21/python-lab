n=int(input("Enter the number whose factors are to be found:"))
for i in range(1,n+1):
    if n%i==0:
        print(i)
