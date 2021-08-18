
numbers = [1, 2, 3, 4, 5]
numbers_2 = [6, 7, 8, 9, 10]

print(list(zip(numbers, numbers_2)))
print(dict(zip(numbers, numbers_2)))

# we whant something like this : ali :maximum score , sara : maximum score , ....

userName = ["ali", "sara", "hossein", "iman", "mohammad"]
score = [10, 19, 14, 13, 4]
final = [20, 13, 15, 7, 12]
print(list(zip(userName , score , final)))
# result = {pair[0] : max(pair[1] , pair[2]) for pair in zip(userName,score,final)}
# print(result)
# print("------------") # now we whant use map function : 
# result_2 = zip(userName , map(lambda pair : max(pair) , zip(score,final)))
# print(dict(result_2))