l1 = []
n = int(input("Enter the range: "))
for i in range(n):
    l1.append(int(input("Enter the numbers: ")))
l2 = [x for x in l1 if x>0]
print("Postive Numbers: ", l2)
l3 = [x*x for x in l2]
print("Square: ", l3)
s = input("Enter the string: ")
l = [x for x in s if x in 'aeiou']
print("Vowels: ", l)
l = [ord(x) for x in l]
print("Ordinal Value: ", l)

