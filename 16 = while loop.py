


# while loop syntax :
# while condisin == True :
#     run the order

number = 1 

while number <= 10 : 
    print(number)
    number+=1

print("--------------------------------")
# password example :

password = int(input("please crate a password :"))

confirmPassword = int(input("\nplease re enter the  password :"))

while confirmPassword != password :
    print("\nthe passwords not math please try again")
    confirmPassword = int(input("\nplease re enter the  password :"))

print("\nwelcome")