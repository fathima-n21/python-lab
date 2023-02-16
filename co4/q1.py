class Rectangle():
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def rectangle_area(self):
        return self.length*self.breadth
    def rectangle_perimeter(self):
        return 2*(self.length+self.breadth)

l1=int(input("Enter the length of the rectangle 1:"))
b1=int(input("Enter the breadth of the rectangle 1:"))
obj1=Rectangle(l1,b1)
l2=int(input("Enter the length of the rectangle 2:"))
b2=int(input("Enter the breadth of the rectangle 2:"))
obj2=Rectangle(l2,b2)
print("The area of first rectangle is ",obj1.rectangle_area())
print("The perimeter of first rectangle is ",obj1.rectangle_perimeter())
print("The area of second rectangle is ",obj2.rectangle_area())
print("The perimeter of second rectangle is ",obj2.rectangle_perimeter())
if obj1.rectangle_area()>obj2.rectangle_area():
    print("Rectangle 1 is bigger")
else:
    print("Rectangle 2 is bigger")
