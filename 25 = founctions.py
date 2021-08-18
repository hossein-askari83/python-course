print("---------------------------------------------------------------") # PART 1.DEFIND A FOUNCTUIN

# founctions help us insted write a lot of command we just write it one time 
# for example , think "print founction" dont exist and we must write a lot of line of command just for print some thing
# methods are a special type of founction with some difirent 

# there is 4 type of founcuins : 
# 1. have a input and output
# 2. have a input and dont have output
# 3. dont have input and have a output
# 4. dont have input and our put

# now we whant creata a function : 

# def sayHello() : 
#     print("hello")
#     print("how are you")
# # sayhello funcion dont have a input and output so its type is 4
# sayHello() # for call a fanction we write his name and write ()

# print("---------------------------------------------------------------") # PART 2.RETURN

# def mul() : 
#     a = 3
#     b = 5
#     c = "simple text"
#     return c,a*b # if you whant use a varible or some thing in  out of founction you must return it
#     print("this text will not print") # commands after return dos not work
# result = mul()
# print(result)
# print("---------------------------------------------------------------") # PART 3.PARAMERRS AND ARGUMANTS



# def show_full_name(firstname , lastname) : # we can give varibales to function and we call them : "PARAMETERS"
#     fullName = f"{firstname} {lastname}"
#     return fullName

# print(show_full_name("ali" , "azimi")) # We need to set the values ​​of the parameters so that the function can be executed for those values
                                       # The value we give to the parameters is called the "ARGUMANTS"
# also we can give argumant to parameter like this ways : 
#1: 
# firstNumber = 3
# secendNumber = 5
# def sum_of_numbers(numberOne , numberTwo) : 
#     return numberOne + numberTwo
# print(sum_of_numbers(firstNumber , secendNumber)) 
#2:

# example = {"leassonName" : "math" , "score" : 19}

# def example_def(l_name , s) :
#     text = f"lesson name ==> {l_name}\nscore ==> {s}"
#     return text

# print(example_def(example["leassonName"] , example["score"]))
# print("--------------------------")

# def even_or_odd(number) : 
#     if number % 2 == 1 : 
#         return "odd"
#     else : 
#         return "even"
# print(even_or_odd(10))
# print(even_or_odd(9))
# print("--------------------")
# # in founction s we can remove "else" :
# def even_or_odd2(number) : 
#     if number % 2 == 1 : 
#         return "odd"
#     return "even"
# print(even_or_odd(10))
# print(even_or_odd(9))
# print("---------------------------------------------------------------") # PART 4.GIVE VALUES TO PARAMATERES

# def powered_number(number , power = 2) : # i whant every number that im write powered to 2 so im write it like this
#     return number ** power

# print(powered_number(3))
# print("---------------------")
# print(powered_number(3,4)) # if you change power value it work with new value that you write
# print("---------------------")
# print(powered_number(number=4 , power=3)) # also you can write it like this 


# print("---------------------------------------------------------------") # PART 5.*args and **kwargs

# when you whant give ukhow number of variables in function we use *args :
 
# def sum_of_numbers(*args) :  # we can use any name insted of args 
#     total = 0 
#     for number in args : 
#         total+=number
#     return total
# print(sum_of_numbers(1,23,4,7)) # and we can ukhow numbers of values
# print("-----")
# # if we whant use a list in *args :  
# numbersList = [1,23,4,7]
# def sum_of_numbers(*args) :
#     total = 0 
#     for number in args : 
#         total+=number
#     return total
# print(sum_of_numbers(*numbersList))  # we must write a * before list name 


# print("-------------------------------------")
# when you whant give ukhow number of keyword and values in founction we use **args :

# def  show_name(**kwargs) :   # we can use any name insted of kwargs 
#     for key,values in kwargs.items() : 
#         print(f"{key} : {values}")

# show_name(name = "ali" , lastName = "ahmadi" , age = 20 , email = "ali@gmail.com")

# print("-----")

#if we whant use a dictionary in **kyargs : 

# usersInfo = {"name" : "ali" , "lastname" : "ahmadi" , "age" : 20 , "email" : "ali@gmail.com"}
#
# def  show_name(**kargs) :
#     for items in kargs.items() :
#         print(items)
#
# show_name(**usersInfo) # we must write two ** before dictionry name.
#
#
print("--------------------------------")

# important : if we whant use all 4 parameters ways We do it in the following order : 

# 1.parameter
# 2.*args 
# 3.defult parameter
# 4.**kwargs
# example :
def display_info(a,b,*numbers,defult = "defult" , **name ) :
    return a,b,numbers,defult,name

print(display_info('a' , 'b' , 1,2,3 ,defult = "ali", name = "mohammad" , lastName = "askari"))

# print("-------------------------------------")


