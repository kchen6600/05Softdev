import random

#read through csv and create dictionary
fileocc = open('data/occupations.csv')
nextline = fileocc.readline()
#print nextline

def createDiction():
	jobs = {}
	for nextline in fileocc:
		#print nextline
		if (nextline.find('"') >= 0):
			new = nextline[1:]
			ind = new.find('"')
			jobType = new[:ind]
			ind2 = new.find("\r")
			percent = new[ind+2:ind2]
		else:
			ind = nextline.find(",")
			jobType = nextline[:ind]
			ind2 = nextline.find("\r")
			percent = nextline[ind+1:ind2]
		jobs[jobType] = float(percent)
	#print jobs
	return jobs

jobs = createDiction()
#print jobs
#choose random occupation in dictionary
def chooseRandom():
    my_list = []
    for key in jobs:
        if key != 'Total':
            my_list += [key] * int((jobs[key] * 10))
        x = random.choice(my_list)
    return str(x) + "   " + str(jobs[x])

#print chooseRandom()
