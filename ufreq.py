'''You don't need to read input or print anything.
Your task is to complete the function isFrequencyUnique() which
take integer N andarray arr of size N as arguments, and returns a boolean.'''


N=6
arr=[2,2,6,-1,-1,-1,6,-1, 6]
l2=[]
print("Input:")
print(N)
print(arr)
def FrequencyUnique(n,l1):
    key=0
    while l1!=[]:
        num=l1[key]
        key=0
        count=0
        for i in l1:
            if i==num:
                count=count+1

        l2.append(count)
        
        for j in range(count):
            l1.remove(num)  

    flag=True
    for i in range(1):
        c2=0
        key=0
        for i in l2:
            if i == l2[key]:
                c2+=1
        key+=1        
        if c2>1:
            flag=False
        else:
            flag=True
            
        print("Output:",'\n',int(flag),flag)    
FrequencyUnique(N,arr)


