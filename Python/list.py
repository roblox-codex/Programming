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
