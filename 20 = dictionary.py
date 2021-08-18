
# part 1 : strucher
# print("-------------------------------------------------------------------------------------")
# # we whant create a list of our items that we buy in a shop like this :

# # shopping list :
# #     item :
# #         name :
# #         number :
# #         price :
# #     item 2 :
# #         name :
# #         number :
# #         price :
# #     .....

# myShoping = [["candy", 2, 2000], ["toy", 1, 100000], ["video game", 1, 300000]]
# # well this is not good so we use DICTIONARY

# myShoping_3 = [{"name": "candy", "number": 2, "price": 2000},
#                {"name": "toy", "number": 1, "price": 100000},
#                {"name": "video game", "number": 1, "price": 300000}]

# # note : there is two way to defind dictionary : 1 = above example
# #  2 = following example :
# myShoping_4 = dict(name="new way", number=1, price=10000)

# # to access values in dictionary we do the same work for list but insted index we write keyvalue :
# print(myShoping_3[1]["name"])
# print(myShoping_4["name"])

# print("-----------------------------")

#  me = {"name": "hossein",
#        "family": "askari",
#        "age": 16}
#  to access every values in dctionary we write like this:

# for value in me.values():
#     print(value)

# print("-----------------------------")


# # to access every keys in dctionary we write like this:

# for key in me.keys():
#     print(key)


# print("-----------------------------")


# # to access every keys and values in dctionary we write like this:

# for item in me.items():
#     print(item)


# # or we write :

# for key,value in me.items():
#     print(key,value)

# print("-------------------------------------------------------------------------------------") # part 2 : methods


# in
# we whant chek a key exist in a dictionary or not :
# me_2 = {"name": "hossein", "family": "askari", "age": 16}
# print("phone" in me_2)
# print("name" in me_2)
# print("-----------------------")
# we whant chek a value exist in a dictionary or not :
# print("ahamad " in me_2.values())
# print("hossein" in me_2.values())




# print("-----------------------")
# # clear 
# me_2.clear() # remove all item in dictionary
# print(me_2)



# print("-----------------------")
# copy
# copyMe_2 = me_2.copy()
# print(me_2)
# print(copyMe_2)



# print("-----------------------")
# we whant create a dictionary with defult value 
# userName = {"name" : "unkhow" , "family" : "unkhow" , "age" : "unkhow"  , "phone" : "unkhow" } # ==> well this is not right way
# userName_2 = {}.fromkeys(["name","family","age","phone"],"unkhow") # ==> this is the right way 
# print(userName)
# print(userName_2)



# print("-----------------------")
# get 
# there is another way to access and chek values in dictionary and that is get method : 

# teachers_lesones = {"math" : "gharib zade" , "programming" : "rajabi" , "web" : "shariati" , "database" : "rezvanian"}

# print(teachers_lesones.get("math")) # ==> access to values 
# print(teachers_lesones.get("farsi")) # ==> chek the values and if not exist it write "None"




# print("-------------------------------------------------------------------------------------") # part 3 : remove and update
# me = {"name" : "ali" , "family" : "ahmadi" , "email" : "ali@gmail.com"}
# #me.pop("name")# remove key and value that you write it
# #print(me)

# #me.popitem() # remove last key and value 
# #print(me)

# print("----------------------------")

# secend = {"age" : 19 , "name" : "sara"}
# secend.update(me) 
# print(secend)
# print("------------")
# secend["family"] = "azizi" # if we whant update just one item we write like this
# print(secend)
