l=int(input("Enter the length of cuboid:\n"))
b=int(input("Enter the breadth of cuboid:\n"))
h=int(input("Enter the height of cuboid:\n"))
def cuboid_area(l,b,h):
    return(2*(l*b+b*h+l*h))
ans1=cuboid_area(l,b,h)
print("Area of cuboid=",ans1)
def cuboid_perimeter(l,b,h):
    return(4*(l+b+h))
ans2=cuboid_perimeter(l,b,h)
print("Perimeter of cuboid=",ans2)
print("\n\n")
