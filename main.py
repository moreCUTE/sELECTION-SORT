import random

def selection_sort():
    for i in range(len(list)):
        a = list[i]
        for j in range(len(list)-i):
            if list[j+i]<a:
                a = list[j+i]
                toSwap = j+i
       

print ("How long do you want your list to be?")
x = int(input())
list = []
for i in range(x):
    list.append(random.randrange(0,100))
print(list)

random.shuffle(list)

selection_sort()

print(list)
