# Write the python script for binary search

arr = []
n = int(input("Enter the no of elements in array:- "))
for i in range(n):
    element = int(input("Enter element {}:- ".format(i+1)))
    arr.append(element)

search_element = int(input("Enter the element to search:- "))

found = False
low = 0
high = len(arr) - 1

while low <= high:
    mid = (low + high) // 2
    if arr[mid] == search_element:
        print("Element found at index:-", mid)
        found = True
        break
    elif arr[mid] < search_element:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("Element not found in the array.")
