

myNumbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# im whant doubeld my numbers
# doubeldnumbers = []
# for num in myNumbers:
#    doubeldnumbers.append(num * 2) # we do it with 3 lines of code but there is a easyer way :  list Comprehension
# we doubeld our numbers in just 1 line babyyyyy
doubeldnumbers = [num * 2 for num in myNumbers]
print(doubeldnumbers)


even = [num for num in myNumbers if num % 2 == 0]  # we can use if too
print(even)
print("---------------------")
myNumbers2 = [num * 2 if num % 2 == 0 else num * 3 for num in myNumbers] # if we whant use "else" we must write if and else in first
print(myNumbers2)


