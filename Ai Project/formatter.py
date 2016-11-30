read = open ('ai.txt','r')
read1 = open ('ai.txt','r')

readcount1 = 0

while (readcount1 < 2):
    first = read.readline()
    readcount1 += 1



two = read1.readline()

dec = [(1, two.split("."))]






dec1 = dict(dec)
print dec1#
list1 = dec1[1]
print list1#









list2 = str(list1[1]).split('\n')
print list2#
list1.insert(1,list2[0])
print list1#

list1Lang = list1.__len__()
print list1Lang#

del list1[list1Lang - 1]
print list1#


dec1.clear()
dec1.update({1 : list1[0]})
dec1.update({2 : list1[1]})
print cmp(dec1[1],dec1[2])#
print dec1#







read.close()
read1.close()