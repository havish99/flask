from flask import *
import json
app=Flask(__name__)

@app.route('/hi',methods=['POST','GET'])
def lol():
	d={}
	if request.method=='POST':
		d=request.json
		print d['11']
		return json.dumps(d)

if __name__ == '__main__':
   app.run(debug = True)