

# we whant raise (make) error : 
# syntax = raise errorType (error message)
print("--------------------")
#raise IndexError ("ridi")
# example : 
colors_list = ('green','blue','yellow', 'black' )
def color_chose(color) : 
    if color not in colors_list :
        raise ValueError("you must type one color")
    elif type(color) is not str : 
        raise IndexError ("you must type words")
    else :
        print(f"{color} is a color")

#color_chose("ali")
#color_chose(3)
#color_chose('green')

