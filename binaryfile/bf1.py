import pickle
fobj=open("file1.dat",'wb')
dict1={}
l1=[]
dict1={"Name":"Ram","age":"5","marks":"55","class":"2"}
l1=["Amit","priyanka","anvay","Anushka"]
pickle.dump(dict1,fobj)
pickle.dump(l1,fobj)
fobj.close()

f=open("file1.dat",'rb')
dict2={}
l2=[]
print(pickle.load(f))
print(pickle.load(f))
f.close()
'''THIS is TEST'''

