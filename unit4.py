
l=['yeah@yahoo.com','aghd@gmail.com','aygduhwu@qwe.com','effheiu@gmail.com']

new_l=list(filter(lambda x:'@gmail.com' in x,l))
l=list(map(len,new_l))
print(l)
'''
----------------------
SRNS = ["21ECS003","21ECS013","21ECS036","21ECS033"] 
x_marks = [98,99,80,90] 
y_marks = [91,90,84,92] 
s={}
for i in range(4):
    s[SRNS[i]]=(x_marks(i)+y_marks(i))
    
print(s)    
-----------------------
class ValueAbove100Error(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Entered value {value} is above 100.")

def get_user_input():
    user_input = int(input("Enter a value between 0 and 100 (inclusive): "))
    if user_input > 100:
        raise ValueAbove100Error(user_input)
    return user_input

try:
    user_value = get_user_input()
    print(f"Entered value: {user_value}")
except ValueAbove100Error as e:
    print(f"Error: {e}")
except ValueError:
    print("Error: Please enter a valid integer.")
-----------------------
'''

