words = list()
for i in range(3):
    words.append(input())
s = input()
s = s.upper()
if len(words) == len(s):
    for i in range(len(words)):
        if words[i][0] != s[0]:
            break
    print("True")

else:
    print("Falsee")