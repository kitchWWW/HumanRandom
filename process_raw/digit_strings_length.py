fd = open('../raw_data/batch_ds_longer.csv')
singleFinger = []
bothFingers = []
allFingers = []

lineNo = 0
for l in fd.readlines():
	for i in range(30):
		portion = l.split(',')[i].replace('"',"").strip()
		if i > 26 and len(portion) > 100:
			print len(portion)
			if i == 27:
				singleFinger.append(portion)
			if i == 28:
				bothFingers.append(portion)
			if i == 29:
				allFingers.append(portion)
			

print singleFinger
print bothFingers
print allFingers

fd = open("../datasets/ds_one.csv",'w')
for i in singleFinger:
	fd.write(i+'\n')
fd.close()

fd = open("../datasets/ds_both.csv",'w')
for i in bothFingers:
	fd.write(i+'\n')
fd.close()

fd = open("../datasets/ds_full.csv",'w')
for i in allFingers:
	fd.write(i+'\n')
fd.close()

