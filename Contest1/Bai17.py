c = input()

if 'A' <= c <= 'Z':
    print('UPPER')
elif 'a' <= c <= 'z':
    print('LOWER')
elif '0' <= c <= '9':
    print('DIGIT')
else:
    print('SPECIAL')