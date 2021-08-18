
# print("------------------------------------------------------------------------------------------")# part 1 : chek elements 

# myFavarite = ["coding" , "song" , "video game" , "eminem" , "movie"]

# numberRange = range(10) # to print the values in a range must convert that to list(or array)

# print (list(numberRange))

# print("-----------------------")

# print(len(numberRange)) # ==> to khow a varible have how many value we use the "len" founction 

# print(len(myFavarite))

# print("-----------------------")

# print(myFavarite[0]) # to use a value that you whant in a list , you must type "[]" and type index of value in [] 

# print(myFavarite[4]) # note : index start from 0
# print(myFavarite[-1]) # IMPORTANTE : if you put a "-" index start from the end to first and it not start with 0 its start from 1

# print("-----------------------")

# isEmineminlist = "eminem" in myFavarite # to khow that a value in a list or not  you can use "in"
# isEmineminlist = "Eminem" in myFavarite # python language is sensitive to loower or upper letters 

# print(isEmineminlist)



# print("------------------------------------------------------------------------------------------")# part 2 : print lists

# mylist = ["blue", "green", "red", "gray", "orange", "purple", 15.5]

# for item in mylist: # if we whant to print the member of a list we can use the for loop like this :
#     if type(item) == str :
#         print(f"the {item}  a color ")
#     else :
#         print(f"the {item} a number")

# print("----------------------------------")

# index = 0 
# while index < len(mylist) : # if we whant to print the member of a list , with while loop we do the following : 
#     if type(mylist[index]) == str:
#         print(f"{mylist[index]} is color")
#     else :
#         print(f"{mylist[index]} is number")

#     index += 1 

# print("------------------------------------------------------------------------------------------")# part 3 : add a value
 
# myFirends  = ["ali", "mammd", "hossein", "hashem", "ahmad", "mahdi"]
# print(myFirends)

# myFirends.append("sajad") # if we whant to add one(just one) item in a list from end , we use "append" function
# print(myFirends)

# print("---------------------")

# myFirends_2 = ["jvad", "matin"]
# myFirends.extend(myFirends_2) # if we whant to add one(just one) list to the way the values is part part ,
# # in a list from end , we use "extend" function
# print(myFirends)

# print("---------------------")

# myFirends.insert(0,"reza") # if we whant to add one(just one) item in a list in every where we whant
# # , we use "insert" function , first we write the index and then write value
# print(myFirends)

# print("------------------------------------------------------------------------------------------")# part 4 : remove value

# favoriteSongs = ["lose yourself", "guts over fear", "arabe", "not afraed", "lose it", "void", "with outme", "void", "adam"]
# print(favoriteSongs)

# favoriteSongs.pop(2) # remove value that you write hes index 
# print(favoriteSongs)
# favoriteSongs.pop() # if not write the index it will remove last element 
# print(favoriteSongs)

# favoriteSongs.remove("void") # remove value that you write it 
# # note : if there are more then one that value you write it , it just remove the first one
# print(favoriteSongs)

# favoriteSongs.clear() # delete all elements 
# print(favoriteSongs)

# print("------------------------------------------------------------------------------------------")# part 5 : more functions 

# index 

# favoritMovies = ["avengers", "avatar", "lucy", "8mile", "wandavision", "lucy"]
# print(favoritMovies.index("8mile")) # index : write object and give you the object`s index 
# print(favoritMovies.index("8mile" ,1,4)) # index("8mile" ,srart index ,end index)
# print("--------------------------")

# #count
# print(favoritMovies.count("lucy")) # count : give you number of how many of this value is there
# print("--------------------------")

# # reverse
# number = [1,2,3,4,5,6,7,8,9]
# print(number)
# number.reverse() # reverse : reverse your list from end to start 
# print(number)
# print("--------------------------")

# # sort 
# unsortList = [45, 63, 25, 10, 9]
# print(unsortList)
# unsortList.sort() # sort : sort your list from lowest to biggest 
# # note : if your values is string it will sort from A to Z 
# print(unsortList)
# print("--------------------------")

# # join
# myLesson = ["math", "science", "programming", "web", "python"]
# print(myLesson)
# print(" - ".join(myLesson)) # join : put all of your objects in a string
# print("--------------------------")

# print("------------------------------------------------------------------------------------------")# part 6 : slicing lists

# note : slicing list is not a method or function its a kind of coding

# myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(myNumbers)
# copyOfMynumbers = myNumbers[0:9:1] # slicing list : to make a copy or select object of another list
# slicing list syntax : listname[start index :end index: step]
# note : slicing list dosent show the last index so in above example in end index we write 9 to print last object
# print(copyOfMynumbers)
# print("\n\n-----------------")
# print(myNumbers[0:] )   # if we not write end index its print from start index that we write to last index
# print("-----------------")
# print(myNumbers[:9] )   # if we not write start index its print from first index  to end index that we write 
# print("-----------------")
# print(myNumbers[::2]     )   # if we not write end and start index and just write step its print from first to last with that step that we write
# print("-----------------")
# print(myNumbers[:]  )     # if we not write end and start index and step , its print from first to last with one step 
# print("-----------------")
# print(myNumbers[::-1])    # if we write negative number in step its will print from last to first with that step that we write
# print("-----------------")
# myName = "hossein"
# print(myName[::-1])        #importante note : all of these notes is work for string type too

