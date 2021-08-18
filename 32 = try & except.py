

# when you write a command in try computer chek he can run the command without any problems or not when he cant run the
# command its go to except command and run it 
# else : when try command run else is run too
# finally : the finally section run the command with any situation
def divide(firstNum , secendNum) : 
    try:
        return firstNum / secendNum
    except ZeroDivisionError :
        return"you cant divide a number to 0"
    else:
        print("its else section")
    finally :
        print("this is finally section")
    
print(divide(1,1))

