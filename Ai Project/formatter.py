read = open ('ai.txt','r')
read1 = open ('ai.txt','r')

readcount1 = 0

while (readcount1 < 2):
    first = read.readline()
    readcount1 += 1



two = read1.readline()

dec = [('1', two.split(".")),('b', 1),('c', 2),('d', 3),('e', 4)]






dec1 = dict(dec)
print dec1#
print dec1['1']#
list1 = list(dec1['1'])
print list1#









list2 = str(list1[1]).split('\n')
print list2#
list1.insert(1,list2[0])
print list1#

list1Lang = list1.__len__()
print list1Lang#

del list1[list1Lang - 1]
print list1#
dec1.update(dict(list1))









read.close()
read1.close()