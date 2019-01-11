fd = open('raw_data/batch_ht.csv')
headsTails = []

for l in fd.readlines():
	for i in range(31):
		portion = l.split(',')[i].replace('"',"").strip()
		print i
		print portion
		if i > 26 and len(portion) > 100:
			print len(portion)
			if i == 30:
				headsTails.append(portion)
			
print headsTails

fd = open("datasets/headstails.csv",'w')
for i in headsTails:
	fd.write(i+'\n')
fd.close()
