print("..................MENU...................")
print("................1.PUSH...................")
print("................2.POP....................")
print("................3.DISPLAY................")
print("................4.EXIT...................")

def push(stck,e):
    stck.append(e)
    print(stck)

def pop(stck):
    if(stck==[]):
        print("Its an underflow condition")

    else:
        print("the deleted element is ",stck.pop())

def display(stck):
    if stck==[]:
        print("the stack is empty")

    else:
        for i in range(len(stck)-1,-1,-1):
            print(stck[i])
            

stack=[]
while True:
    ch=int(input("Enter your chooice"))
    if ch==1:
        element=int(input("Enter the elemnt you want to add"))
        push(stack,element)

    elif ch==2:
        pop(stack)

    elif ch==3:
        display(stack)

    else:
        break
    
        
