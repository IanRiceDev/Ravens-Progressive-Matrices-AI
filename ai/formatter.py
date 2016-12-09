read = open ('problem1.txt','r')
read1 = open ('problem1.txt','r')
# opens text file were problem dicrepson is stored
readcount1 = 0
#declaers counter var for loop
first = read.readline()
#declaers var and puts text from frist line in string
while (readcount1 < 1):

    first = read.readline()
    # enters loop and redeclaers the var to the text on the second line
    readcount1 += 1
    #increses the value of the counter and then exits the loop


two = read1.readline()
#declears a var and puts info from line one
dec = [(0, two.split("."))]
#declears a array and puts the value of 0 at index 0 and adds the value of line one and splits and delets all "."



print dec
dec1 = dict(dec)
#convters dec1 to dictonary
print dec1#
list2Lang = dec1.__len__()
#declars var eqwile to dec1's langthe
list1 = dec1[0]
#declars var eqwile to dec1 at 0 index
print list1#








list1Lang = list1.__len__()
#declaers var eqwil to the lang of list1
list2 = str(list1[list1Lang - 1]).split('\n')

print list2#

list1.insert(list1Lang - 1,list2[0])



print list1Lang#
print list1
del list1[list1Lang]
#delets list at value of it's lang
print list1#


dec1.clear()
#clears the contents of dec1










read.close()
read1.close()
#closes connectsons to text file