#QUESTION LAB 1
import csv
f=open("A.csv",'r+')
f2=open("Output.csv","w",newline="")
S_writer=csv.writer(f2)
r=f.readlines()
l=[]
S_writer.writerow(r[0].strip().split(","))
for i in r[1:]:
    s=i.strip().split(",")
    d=s[1].split("/")        
    if "CAPE TOWN" in i.upper():
        S_writer.writerow(s)
        
    elif(int(d[0])>2 and int(d[1])>1 and int(d[2])>=16):
        l.append(s)
                
S_writer.writerows(l)
f.close()
f2.close()
