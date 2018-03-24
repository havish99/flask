from flask import Flask, request, render_template, redirect,url_for 

app=Flask(__name__)

@app.route('/lol')
def hello():
	return render_template('index.html')




if __name__ == '__main__':
	app.run()