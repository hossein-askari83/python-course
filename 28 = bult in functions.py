

number = [0, 9, 6, 5, 4, 3, -7, 1, 2.6]

print("-----------")  # all , any

print(any(number)) # if just one of values was true it show : true (1 and other numbers is true)
print(all(number)) # if just one of values was false it show : false (0 is false)

print("-----------")  # min , max

print(max(number)) # show maximum of numbers
print(min(number)) # show minimum of numbers

print("-----------")  # sorted , reversed

print(sorted(number)) # sort numbers from smallest to biggest
print(list(reversed(number))) # show reversed list

print("-----------")  # len , abs
print(len(number)) # show number of value in list
print(abs(number[6])) # abs = absolute : show "قدر مطلق"

print("-----------") # sum , round
print(sum(number)) # show sum of list values 
# note : sum (varible , some sumber)  if write a number after varible it show sum of "numbers + number"
print(round(number[8]))