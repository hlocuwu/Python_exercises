c = input()

if 'A' <= c <= 'Z':
    next_char = chr((ord(c) - ord('A') + 1) % 26 + ord('a'))
elif 'a' <= c <= 'z':
    next_char = chr((ord(c) - ord('a') + 1) % 26 + ord('a'))

print(next_char)