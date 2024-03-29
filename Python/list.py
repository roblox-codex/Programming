def swapList(newList):
    size = len(newList)
     
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
     
    return newList
     
newList = [12, 30, 19, 26, 21]
 
print(swapList(newList))

# Another approach
# The usage of * operand

list = [1, 2, 3, 4]
 
a, *b, c = list
 
print(a)
print(b)
print(c)


# To find the length of list
li = [20, 50, 70]
n = len(li)
print("The length of list is: ", n)


# Check element exist or not in list
lst=[ 1, 2, 3, 4, 5, 6 ]
i=7
if i in lst:
    print("exist")
else:
    print("not exist")


# Reverse the list with user input
lst = input("Enter a list of numbers separated by spaces: ")
lst = [int(x) for x in lst.split()]
lst.reverse()
print(lst)

# Smallest number in list
input_str = input("Enter a list of numbers separated by commas: ")
numbers = [int(x) for x in input_str.split(',')]
smallest_number = min(numbers)
print("The smallest number in the list is:", smallest_number)
