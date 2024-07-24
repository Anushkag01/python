#QUESTION LAB 3
import csv
f=open("A.csv",'r+')
f2=open("With_locations.csv","w",newline="")
S_writer=csv.writer(f2)
r=f.readlines()
r1="Location,"+r[0]
S_writer.writerow(r1.strip().split(","))
for i in r[1:]:
    s=i.strip().split(",")
    l=s[0].split(":")
    S_writer.writerow(l+s[1:])

f.close()
f2.close()



