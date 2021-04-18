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

    arr = []
for x in count.keys():
    temp = Node()
    temp.letter = x
    temp.num = count[x]
    arr.append(temp)
arr

def sortingFunciton(arr):
    for x in range(len(arr)):
        for y in range(x):
            if arr[x].num > arr[y].num:
                temp = arr[x]
                arr[x] = arr[y]
                arr[y] = temp
    return arr

arr = sortingFunciton(arr)
for x in arr:
    print(x.letter + " - " + str(x.num))
counter = 1 
while len(arr) != 1:
    temp = Node()
    temp.letter = "Node" + str(counter)
    temp.num = arr[len(arr) - 1].num + arr[len(arr) - 2].num
    temp.left = arr[len(arr) - 2]
    temp.right = arr[len(arr) - 1]
    
    tempArr = []
    print(temp.letter + ": " + temp.left.letter + ", " + temp.right.letter + " - " + " sum " + str(round(temp.num/len(f),3)))
    
    for x in range(len(arr) - 2):
        tempArr.append(arr[x])
    tempArr.append(temp)
    arr = sortingFunciton(tempArr)
    counter += 1
    
tempArr[0].letter     

def tree(node, arr, s):
    if node == None:
        return arr
    tree(node.left, arr, s + "0")
    node.code = s
    arr.append(node)
    tree(node.right, arr, s + "1")
    return arr
tarr = []
newArr = tree(tempArr[0], tarr, "")

to_delete = []
for x in range(len(newArr)):
    if "Node" in newArr[x].letter:
        to_delete.append(x)
for x in range(len(to_delete)):
    for y in range(x):
        if to_delete[x] > to_delete[y]:
            temp = to_delete[x]
            to_delete[x] = to_delete[y]
            to_delete[y] = temp
for x in to_delete:
    newArr.remove(newArr[x])

    for x in newArr:
    print(x.letter + " - " + str(round(x.num / len(f) , 3)) + " - " + x.code)
def finder(nodes, letter):
    for x in nodes:
        if letter == x.letter:
            return x.code

newstr = ""
for x in f:
    if x == ' ':
        newstr += finder(newArr, 'space')
        continue
    if x == '\n':
        newstr += finder(newArr, 'new_line')
        continue
    newstr += finder(newArr, x)

text_file = open("ass3.txt", "w")
n = text_file.write(newstr)
text_file.close()

text_file = open("ass3.txt", "r")
text_file.read()
print("Number of bits in the original text: " + str(len(f) * 8) + " bits")
print("Number of bits in the compressed text: " + str(len(newstr)) + " bits")
print("Compression ratio: " + str(len(f) * 8 / len(newstr)))
print("Average code length: " + str(len(newstr) / len(f)))
