s1 = 'abcdefg'
s2 = 'abdght'

for index in range(len(s1)):
    if s1[index] in s2:
        print(s1[index])

for char in s1:
    if char in s2:
        print(char)

s = ''
print(len(s), s)

for i in range(5):
    s = s + 'a'
    print(len(s), s)