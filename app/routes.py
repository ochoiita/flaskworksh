from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Valeria'}
	events = [
		{
			'name': 'Workshop Python',
			'date': 'May 10'
		},
		{
			'name': 'Captura la bandera',
			'date': 'May 11'		
		}
	]
	
	return render_template('index.html', user=user,title='UPSLP',events=events)