import numpy as np
import matplotlib.pyplot as plt



for file in ['both','full','one']:

	fd = open("../datasets/ds_"+file+".csv")
	data  = []
	for l in fd.readlines():
		data.append(l.strip())

	allDigits = list("".join(data))

	totalDigits = len(allDigits)

	x = []
	y = []
	for i in range(10):
		y.append(i)
		x.append(allDigits.count(str(i)) / (totalDigits+0.0) * 100)
	plt.clf()
	plt.bar(y, x, align='center', alpha=0.5)
	plt.xticks(y, y)
	plt.ylabel('% Usage')
	plt.title("key frequency for " +file)
	 
	plt.savefig("../img/key_freq_"+file+".png")


	plt.clf()




	digitPairs = []
	for i in range(10):
		digitPairs.append([])
		for j in range(10):
			digitPairs[i].append(0)

	for i in range(len(allDigits)-1):
		digitPairs[int(allDigits[i])][int(allDigits[i+1])] += 1

	digPairs= np.array(digitPairs)
	print digPairs

	fig, axis = plt.subplots() # il me semble que c'est une bonne habitude de faire supbplots
	heatmap = axis.pcolor(digPairs, cmap=plt.cm.Blues) # heatmap contient les valeurs
	plt.colorbar(heatmap)
	plt.title("key pair counts for "+file)
	plt.savefig("../img/key_pair_"+file+".png", dpi=100)



