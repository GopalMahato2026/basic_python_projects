# Simple is_even function defination
def is_even( i ):
    '''
    INPUT: i, a positive int
    Returns True if i is even, otherwise False
    '''
    remainder = i % 2
    return remainder == 0

#using the is_even function later on in the code
print("All numbers between 0 and 20: Even or not")
for i in range(20):
    if is_even( i ):
        print(i, "Even")
    else:
        print(i,"Odd")  

print("This is the type of is_even function",type(is_even))          
