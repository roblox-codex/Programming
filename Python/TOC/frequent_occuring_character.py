text = input("Enter a string: ")

char_freq = {}  
for char in text:
    if char in char_freq:
        char_freq[char] += 1
    else:
        char_freq[char] = 1
        
max_count = 0
most_freq_char = ''
for char, count in char_freq.items():
    if count > max_count:
        max_count = count
        most_freq_char = char
        
print("Most frequent character:", most_freq_char)
print("Its count:", max_count)
