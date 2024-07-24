d1=dict(input("Enter the values of dictionary"))
stack=[]
def push():
    for key, val in d1.items():
        if val > 75:
            stack.append(key)
        
def pop():
    for i in range(len(stack)):
        print(stack.pop())


push()
pop()
