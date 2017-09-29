from flask import Flask, render_template
from utils.occupations import createDiction, chooseRandom, jobs

my_app = Flask(__name__)


@my_app.route('/')
def root():
	return "<h1>Welcome!</h1>"

#occupations route, using a template
@my_app.route('/occupations')
def occupations():
	return render_template('content1.html', jobs= jobs, rand = chooseRandom())
	
	
	
if __name__ == '__main__':
	my_app.debug = True
	my_app.run()


	