# find the largest prime factor of a number

original_num = int(input("Enter a number: "))

num = original_num
largest = 0
i = 2

while i * i <= num:
    if num % i == 0:
        largest = max(largest, i)
        num = num // i
    else:
        i += 1

largest = max(largest, num)

print("The largest prime factor of", original_num, "is", largest)
