

# sets in pytho like lists with some difirent :
# 1.Sets can't contain duplicates
# 2.Sets are unordered
# 3.In order to find an element in a set, a hash lookup is used (which is why sets are unordered).
# This makes __contains__ (in operator) a lot more efficient for sets than lists.
# 4.Sets can only contain hashable items (see #3). If you try: set(([1],[2])) you'll get a TypeError.

numbers = {1, 2, 3, 4}
print(numbers)

# number2 = {1,2,3,4,2,1,3}
# print(number2)# ==> Sets can't contain duplicates and delete duplicates and print 
print("--------------")
# numbers.add(5) # add value 
# print(numbers)
print("--------------")
# numbers.remove(2) # remove value 
# print(numbers)
# numbers.remove(5) note : if the value that write not exist in set you will get error
# print(numbers)
print("--------------")
# numbers.discard(5) # its work like remove but if valut that you write not exist you will not get error
# print(numbers)
print("--------------")
# numbers3 = numbers.copy() # copy of set 
# print(numbers3)
print("--------------")
numbers.clear()
print(numbers)
print("------------------------------------------")
#you can also get "اجتماع" and  "اشتراک" with sets lile this : 
python = {"ali" , "ahmad" , "hossein" , "reza"}
php = {"sara" , "arash" , "ali" , "reza"}
print(python | php) # اجتماع در ریاضی
print(python & php) # اشتراک در ریاضی
print("------------------------------------------")
# you can also use sets compretion : 

doubeldNumbers = {x**2 for x in range(10)}
helloWorld = {letter for letter in "hello world"}
print(doubeldNumbers)
print(helloWorld)
# big wrannig = sets dont have order , and print Messy | لیست ها نظم خاصی ندارند و در هم ور هم چاپ میکنند 
