import csv
f=open("A.csv",'r+')
f2=open("Output_date.csv","w",newline="")
S_writer=csv.writer(f2)
r=f.readlines()
for i in r[7:10]:
    s=i.split(",")
    d=(s[1]).split(" ")
    S_writer.writerow(d)
 
f.close()
f2.close()
