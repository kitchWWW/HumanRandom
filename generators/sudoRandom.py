import random

sudoRandom = []
for people in range(100):
	guess = []
	for i in range(random.randint(100,200)):
		guess.append(str(random.randint(0,9)))
	sudoRandom.append("".join(guess))
	print "".join(guess)

fd = open("../datasets/sudoRandom.csv",'w')
fd.write("\n".join(sudoRandom))
fd.truncate()
fd.close()
