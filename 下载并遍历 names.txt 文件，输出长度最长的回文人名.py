def is_pamax(name):
    low = 0
    up = len(name)-1
    while low < up:
        if name[low] != name[up]:
            return  False
        low += 1
        up -= 1
    return True


f = open("E:/Desktop/Python_study/names.txt")

max_length = 0
for line in f:
    name = line.strip()
    if is_pamax(name):
        temp_length = len(name)
        if temp_length > max_length:
            max_length=temp_length

print(max_length)

f.close()

# maxlength=8
f = open("E:/Desktop/Python_study/names.txt")
for line in f:
    name = line.strip()
    if is_pamax(name):
        if 8 == len(name):
            print(name)
f.close()
