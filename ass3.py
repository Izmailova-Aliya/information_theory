count = dict()
f = open("ass2.txt", "r").read()
for x in list(f):
    if x == ' ':
        x = 'space'
    if x == '\n':
        x = 'new_line'
    if x in count.keys():
        count[x] += 1
    else:
        count[x] = 1
count
# count symbols/letters
count = dict(sorted(count.items(), key=lambda item: item[1])) #sort dictionary by probability


for x in count.keys():
    print(x + " - " + str(round(count[x] / len(f), 3)))
class Node: #  for each letter creating node
    letter = ""
    num = 0
    code = ""
    left = None
    right = None
