
# comprenhnesion in dictionary is like comprenhnesion in lists :

numbers = dict(first=1, secend=2, theerd=3)
# we whant doubeld our numbers :

doubeld = {key: value * 2 for key, value in numbers.items()}
# in the above example insted numbers.items() we can write a list but our key may not so good :
doubeld2 = {num: num * 2 for num in [1, 2, 3]}
print(doubeld)
print(doubeld2)
print("-----------------")
# like lists comprenhnesion we can use  if and else in dictionary like this : 
evenOrOdd = {num: ("ODD" if num % 2 == 1 else "EVEN") for num in [1, 2, 3, 4, 5, 6]} 
print(evenOrOdd)
