

# nested list ارایه تو در تو

myNumber = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(myNumber)

# if we whant a item in a list and that list is in another list we write it like this
number_5 = myNumber[1][1]
print(number_5)
print("-------------------")

# if we whant items in list and that list is in another list singly we write like this (with for loop) :
for item in myNumber:
    for num in item:
        print(num)
print("-------------------")

# if we whant items in list and that list is in another list singly we write like this (with Comprehension) :

copyList = [[print(num) for num in item] for item in myNumber]

print("------------------------------")

# now we whant create a nested list :
nestedList = [[num for num in range(3)] for item in range(3)]
nestedList2 = [["X" if num % 2 == 0 else "O" for num in range(3)] for item in range(3)] # like you khew before we can use if and else

print(nestedList)
print(nestedList2)