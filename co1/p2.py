curr_year=int(input("Enter the current year:"))
end_year=int(input("Enter the last year:"))
print("The first year is:",curr_year,"The last year is:",end_year)
print("List of leap years are:")
for i in range(curr_year,end_year):
    if(i%4==0)and(i%100!=0)or(i%400==0)and(i%100==0):
        print(i)
