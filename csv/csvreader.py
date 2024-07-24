import csv
f=open("student.csv",'r',newline="\r\n")
S_reader=csv.reader(f)
#print(len(S_reader))
print(csv.reader(f))
for i in S_reader:
    print(i)
f.close()    
