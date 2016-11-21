
read = open ('ai.txt','r')
read1 = open ('ai.txt','r')
readcount1 = 0
while (readcount1 < 2):
    first = read.readline()
    readcount1 += 1



two = read1.readline()

dec1 = []
dec2 = []
#print test.split("\n")
first.split("\n")
#test.
#test1 = dec1.li

dec1.insert(0,two.split("\n"))


dec2.insert(0,first.split("\n"))
#print test1





del dec1[0][1]
del dec2[0][1]
print dec1
print dec2
print(cmp(dec1,dec2))
read.close()
read1.close()