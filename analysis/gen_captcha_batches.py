import random
import numpy as np


def genRandomDigitString(stringLength):
	ret = []
	for i in range(stringLength):
		ret.append(str(random.randint(0,9)))
	return "".join(ret)


fd = open('../datasets/singleFinger.csv')
stringLength = 30

itemLength = 30

positives = []
lines = fd.readlines()
for i in range(len(lines)):
	sample = lines[i].strip()
	for z in range(20):
		halfway = int(len(sample)/2)-stringLength
		startIndex = random.randint(0,len(sample)-stringLength)
		aPortion = sample[startIndex:startIndex+stringLength]
		positives.append(aPortion)

# print positives


negatives = []

for i in range(len(lines)):
	sample = lines[i].strip()
	for z in range(20):
		negatives.append(genRandomDigitString(stringLength))

# print negatives

batchesUnsorted = []

for i in positives:
	features = list(i)
	label = 1
	batchesUnsorted.append([features,label])
for i in negatives:
	features = list(i)
	label = 0
	batchesUnsorted.append([features,label])

batches = []

for b in batchesUnsorted:
	batches.append((b[0],b[1]))

random.shuffle(batches)

x_train_pre = []
y_train_pre = []

x_test_pre = []
y_test_pre = []

splitPoint = len(batches) - int(len(batches)/5)

for b in batches[:splitPoint]:
	x_train_pre.append(b[0])
	y_train_pre.append(b[1])

for b in batches[splitPoint:]:
	x_test_pre.append(b[0])
	y_test_pre.append(b[1])	

x_train = np.array(x_train_pre,dtype=np.int)
y_train = np.array(y_train_pre,dtype=np.int)

x_test = np.array(x_test_pre,dtype=np.int)
y_test = np.array(y_test_pre,dtype=np.int)

print x_train,y_train










