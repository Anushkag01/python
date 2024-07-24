N = [12, 34, 7, 13, 56, 55, 98, 0]
stack = []

def push(list2):
    for i in list2:
        if i % 2 == 0:
            stack.append(i)
    
def pop(stck):
    for j in range(len(stack)):
        print (stck.pop())

push(N)
pop(stack)
