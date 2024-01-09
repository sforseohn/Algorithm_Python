# 입력
word = input().lower()

c_count = dict()

for c in word:
    if c in c_count:
        c_count[c] += 1
    else:
        c_count[c] = 1

char_list = sorted(c_count.items(), key=lambda x:x[1], reverse=True)

if len(char_list) > 1:
    top_char = [item[1] for item in char_list[:2]] 
    if top_char[0] == top_char[1]:
        print('?')
    else:
        print(str(char_list[0][0]).upper())
else:
    print(str(char_list[0][0]).upper())