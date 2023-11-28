# Write the python script for linear search

arr = []
n = int(input("Enter the no of elements in array:- "))
for i in range(n):
    element = int(input("Enter element {}:- ".format(i+1)))
    arr.append(element)

search_element = int(input("Enter the element to search:- "))

found = False
for i in range(len(arr)):
    if arr[i] == search_element:
        print("Element found at index:-", i)
        found = True
        break

if not found:
    print("Element not found in the array.")
