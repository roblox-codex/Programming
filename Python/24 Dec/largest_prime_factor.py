def largest_prime_factor(number):
    n = number
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

def main():
    user_input = int(input("Enter a number: "))
    result = largest_prime_factor(user_input)
    print("The largest prime factor of", user_input, "is", result)

if __name__ == "__main__":
    main()
