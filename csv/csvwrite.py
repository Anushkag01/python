import csv
f=open("student.csv","w",newline="")
S_writer=csv.writer(f)
rec=[]
S_writer.writerow(["name","Roll","Marks"])
while True:
    name=input("Enter a name")
    roll=int(input("enter roll no."))
    marks=int(input("enter marks of student"))
    rec.append([name,roll,marks])
    ch=input("do want to cont?(Y?N)")
    if ch=="N":
        break
    
for i in rec:
    S_writer.writerow(i)

f.close()    
