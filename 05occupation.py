from flask import Flask, render_template
import random
my_app = Flask(__name__)

@my_app.route('/')
def root():
	return "<h1>Welcome!</h1>"

#read through csv and create dictionary
fileocc = open('occupations.csv')
nextline = fileocc.readline()
#print nextline
jobs = {}
for nextline in fileocc:
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

#choose random occupation in dictionary
def chooseRandom():
    my_list = []
    for key in jobs:
        if key != 'Total':
            my_list += [key] * int((jobs[key] * 10))
        x = random.choice(my_list)
    return str(x) + "   " + str(jobs[x])

#occupations route, using a template
@my_app.route('/occupations')
def occupations():
	return render_template('content1.html', jobs= jobs, rand = chooseRandom())
	
	
	
if __name__ == '__main__':
	#my_app.debug = True
	my_app.run()


	