myList=[5,3,8,6,4,2,36,7,24,27,888]
myList.sort(reverse=False) #升序排列-由大到小進行排
myList
for i in range(len(myList)):
#for i in range(myList):
	if myList[i] % 2>0:
		myList.insert(0,myList.pop(i))
		#myList.insert(0, )
		print(myList)