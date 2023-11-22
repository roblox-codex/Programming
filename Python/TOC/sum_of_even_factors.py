# find the sum of even factors of numbers

num = int(input("Enter a number: "))

sum = 0
for i in range(1, num+1):
    if (num % i == 0) and (i % 2 == 0):
        sum += i
        
print("The sum of even factors of", num, "is", sum)
