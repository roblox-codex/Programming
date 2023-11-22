# find number of solutions to modular equation

import math 

print("Find Number of Solutions")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
n = int(input("Enter n: "))

s = 0; old_s = 1  
t = 1; old_t = 0
r = n; old_r = a 

while r != 0:
    quotient = old_r // r
    old_r, r = r, old_r - quotient * r
    old_s, s = s, old_s - quotient * s 
    old_t, t = t, old_t - quotient * t
    
gcd = old_r

if b % gcd != 0:
    num_sols = 0
else:
    num_sols = gcd

print(f"Number of solutions = {num_sols}")
