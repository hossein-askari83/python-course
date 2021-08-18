

print(list(range (10, 20))) 

print("----------------------------")


print(list(range (10, 20, 2)))

print("----------------------------")


print(list(range (10, 20, 2)))

print("----------------------------")

print(list(range (10))) # if you dont write the first number thats defult => 0 

print("----------------------------")


# solusion 1 
for num in range(10):
    print("*" * num) # ==>  "*" * 1 = "*" , "*" * 2 = "**" ,"*" * 3 = "***" ,....."*" * 9 = "*********" ;

print("----------------------------")

# my solusion 
result = ""
for item in range(10) :
    # for num in range(1)  : # this for loop work to the value of item in range(10)
    result += "*" # ==>  "" = "" + "*" 
    print(result)  
print("----------------------------")


# solusion 2 (for in for) 
for num in range(1, 10):  # [1,2,3,4,5,6,7,8,9]
    stars = ""
    for star in range(1, num + 1):  # [1, ..., num]
        stars += "*"
    print(stars)
