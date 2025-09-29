n = int(input())
if n <= 0:
    exit()

for i in range(n):
    string = input()
    
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
            
    most_frequent_char = max(char_count, key=char_count.get)
    print(most_frequent_char)
