#Find & replace
words = "It's thanksgiving day. It's my birthday,too!"
word_day = "day"
words.find(word_day)
print words.replace("day", "month", 1)


#Min and Max
list=[1, "plate", 3, 4, "flower"]
newList = []
for i in list:
	if type(i)==int:
		newList.append(i)
print min(newList)
print max(newList)

#First and Last
list=["hello",2,54,-2,7,12,98,"world"]
print list[0]
print list[len(list)-1]
newList = list[0], list[len(list)-1]
print newList

#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x  #sorted our list
first_half=x[:len(x)/2]
second_half = x[len(x)/2:]
print first_half
print second_half
second_half[0]=first_half
print second_half





