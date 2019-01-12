fd = open('../raw_data/batch_ds_longer.csv')

data = []

lineNo = 0
for l in fd.readlines():
	person = []
	for i in range(30):
		portion = l.split(',')[i].replace('"',"").strip()
		if i > 26 and len(portion) > 100:
			print len(portion)		
			person.append(portion)
	data.append(person)

fd.close()

print data		

toPrintA = []
toPrintB = []
for d in data:
	if len(d)>0:
		toPrintA.append(",".join(d))
		toPrintB.extend(d)

out = open('../datasets/ds_three_per.csv','w')
out.write("\n".join(toPrintA))
out.close()

out = open('../datasets/ds_dump.csv','w')
out.write("\n".join(toPrintB))
out.close()

