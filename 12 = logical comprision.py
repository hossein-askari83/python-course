# logical oprators 


# and : every conditions must true to run 
print("-----------------------and--------------------")

chiting = True
score = 20 
if chiting == False and score == 20 : 
    print("your the best student")
else : 
    print("your not the best student")
print(f"True and True :{True and True} ")
print(f"True and False : {True and False}")
print(f"False and True : {False and True}")
print(f"False and False : {False and False}")




# or : if even one of the condition is True the program will run
print("----------------------or----------------------")
weather = "sunny"
if weather == "sunny" or weather == "cloudy":
    print("we can travel")
else :
    print("we cant travel") 
print(f"True or True :{True or True} ")
print(f"True or False : {True or False}")
print(f"False or True : {False or True}")
print(f"False or False : {False or False}")


#not : reverse the True or False 
print("-----------------------not--------------------")

training = True
if not training == True : 
    print("you fail just like others")
else : 
    print("you can do what ever you whant")
print(f"not True :{not True} ")
print(f"not False : {not False}")
print("-----------------------------------------------------")

# a example with all logical oprators : 

# we whant give some food to poor people  like this :     family members < 4 =  5 food 
#                                                         family members > 8 =  10 food
#                                                                   the rest =  8 food

# we can sove thos proublem in two ways like this : 

familyMember = 6

if (familyMember < 0) or (familyMember < 8 and familyMember > 4 ) : 
    print(" you get  8 food")

if not((familyMember < 4) or (familyMember>8)) :
    print(" you get  8 food")

