l=int(input("Enter length of rectangle:\n"))
b=int(input("Enter breadth of rectangle:\n"))
def rectangle_area(l,b):
    return(l*b)
ans1=rectangle_area(l,b)
print("Area of rectangle=",ans1)
def rectangle_perimeter(l,b):
    return(2*(l+b))
ans2=rectangle_perimeter(l,b)
print("Perimeter of rectangle=",ans2)
print("\n\n")
    
