fd = open('batch.csv')
singleFinger = []
bothFingers = []
allFingers = []

lineNo = 0
for l in fd.readlines():
	if lineNo <2:
		lineNo+=1
		continue
	for i in range(30):
		portion = l.split(',')[i].replace('"',"").strip()
		if i == 27:
			singleFinger.append(portion)
		if i == 28:
			bothFingers.append(portion)
		if i == 29:
			allFingers.append(portion)
		if i > 26:
			print len(portion)

print singleFinger
print bothFingers
print allFingers


