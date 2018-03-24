from flask import Flask,redirect,url_for,request,render_template

app=Flask(__name__)

@app.route('/')											#basic way of creating routes
def hello():							
	return render_template('login.html')
@app.route('/success/<name>')
def success(name):
	return name
# @app.route('/hello/<name>')								#adding variable attribute to routes
# def hello_name(name):
# 	return name
# @app.route('/hello/<int:lol>')							#int type
# def sqr(lol):
# 	return str(lol+2)
# @app.route('/choose/<name>')
# def choose(name):										#route for redirecting and usage of url_for			
# 	if(name=='sqr'):
# 		return redirect(url_for('sqr',lol=3))
# 	if(name=='name'):
# 		return redirect(url_for('hello_name',name=name))

@app.route('/login',methods = ['POST', 'GET'])
def login():
	if request.method=='POST':
		usr=request.form['nm1']
		return "YAY"
if __name__ == '__main__':
	app.run(debug=True)