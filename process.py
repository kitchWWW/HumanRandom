fd = open('raw_data/batch.csv')
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

fd = open("datasets/singleFinger.csv",'w')
for i in singleFinger:
	fd.write(i+'\n')
fd.close()

fd = open("datasets/bothFingers.csv",'w')
for i in bothFingers:
	fd.write(i+'\n')
fd.close()

fd = open("datasets/allFingers.csv",'w')
for i in allFingers:
	fd.write(i+'\n')
fd.close()

