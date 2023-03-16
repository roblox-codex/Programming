input_str = input("Enter a string: ")
words = input_str.split()
reversed_words = [word[::-1] for word in words]
output_str = " ".join(reversed_words)[::-1]
print(output_str)
