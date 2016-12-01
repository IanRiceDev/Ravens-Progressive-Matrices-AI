read = open ('ai.txt','r')
read1 = open ('ai.txt','r')

readcount1 = 0

while (readcount1 < 2):
    first = read.readline()
    readcount1 += 1



two = read1.readline()

dec = [(0, two.split("."))]





print dec
dec1 = dict(dec)
print dec1#
list2Lang = dec1.__len__()
list1 = dec1[0]
print list1#








list1Lang = list1.__len__()

list2 = str(list1[list1Lang - 1]).split('\n')
print list2#

list1.insert(list1Lang - 1,list2[0])



print list1Lang#
#list1[list1Lang - 1].split("\n")
print list1
del list1[list1Lang]
print list1#

x = 0
dec1.clear()
dec1 = {x:0}
while  x > list1Lang:

    dec1.update({x: list1[x]})
    x += x
    if  x > list1Lang:
        break

#print cmp(dec1[1],dec1[2])#
print dec1#







read.close()
read1.close()