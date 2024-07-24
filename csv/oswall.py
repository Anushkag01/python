import csv

def score():
    f=open("student.csv","r",newline='\r\n')
    r=csv.reader(f)
    for j in r:
        print(j)

    f.close()   
      
def count():
    f=open("student.csv","r",newline='\r\n')
    r=csv.reader(f)
    n=0
    counts=0
    for i in r:
        counts+=1
        n=len(i)
        
    print("the number of columns=",n)
    print("the number of rows=",counts)
    f.close()

score()     
count()       







 
