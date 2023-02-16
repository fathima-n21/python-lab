import os
import csv
path = os.getcwd()
if os.path.exists(path+"/names.csv"):
    with open(path+"/names.csv",newline='') as file:
        reader = csv.DictReader(file)
        col = input("Enter the col to display(id,name,First,age,course) : ")
        for row in reader:
            print(row[col])
else:
    print("File doesn't exist!")
