from tkinter import *
root=Tk()
cv=Canvas(root,width=12,height=100,fill='light blue')
rectangle=cv.create_rect(10,10,20,100,fill="red",width=20)
mainloop()