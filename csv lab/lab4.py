import csv
f=open("A.csv","r+")
f2=open("sports.csv","w+",newline="")
S_writer=csv.writer(f2)
r=f.readlines()
S_writer.writerow(r[0].strip().split(","))

for i in r[1:]:
    s=i.strip().split(",")
    d=s[1].split("/")
    if s[3]=="sports":
        if(3<=int(d[1])<=4 and int(d[2])==16):
            S_writer.writerow(s)
f.close()
f2.close()

        
