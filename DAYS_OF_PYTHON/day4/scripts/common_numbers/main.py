
with open("file1.txt","r",encoding="utf-8") as f:
    list1 = f.readlines()

with open("file2.txt","r",encoding="utf-8") as f:
    list2 = f.readlines()

list3 = [int(i) for i in list1 for j in list2 if i == j]
list3 = list(set(list3)) # mükererrer kayıttan kurtulmak için
list3.sort()
print(list3)

