

# map function is one of lambda uses

numbers = [1, 2, 3, 4, 5]

# im whant doubeld my numbers 

doubels = [] 
for number in numbers : 
    doubels.append(number * 2 )
print(doubels)

print("----------------")

doubels_2 = map(lambda x : x * 2 , numbers) 
# map function syntax = map (funcion , varible)
print(doubels_2)
print(list(doubels_2)) # we must convert to list , to show numbers .
print(list(doubels_2)) # map funcions just one time iterate values in varible

print("-------------------------------------------")

# im whant upper case my names : 
names = ["mohammad" , "hossein" , "iman" , "reza"] 
uppes = map( lambda name : name.upper() , names)
print(list(uppes))

print("-------------------------------------------")

# im whant show my familys : 

persons = [
            {"name" : "mohammad" , "family" : "ordookhani" , "age" : 20} ,
            {"name" : "hossein" , "family" : "askari" , "age" : 20} ,
            {"name" : "iman" , "family" : "madaeni" , "age" : 20}  ]

print(list(map(lambda family : family["family"] , persons))) # with map : in just 1 line

familys = []
for people in persons :
    familys.append(people["family"])
print(familys) # with for : in 3 lines


print("---------------------------------------------------------------------------------------------")
 # filter function

evens = [1,2,3,4,5,6]

print(list(filter(lambda even : even % 2== 0 , evens))) # filter did like if and filter values 

