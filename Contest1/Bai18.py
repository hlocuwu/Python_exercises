c = input()
if 'A' <= c <= 'Z':
    c = chr(ord(c) + 32)
elif 'a' <= c <= 'z':
    c = chr(ord(c) - 32)

print(c)