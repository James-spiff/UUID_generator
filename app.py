from flask import Flask, jsonify
import datetime
import uuid
import pandas as pd 


app = Flask(__name__)


@app.route("/", methods = ['GET'])
def create_uuid():
	api = True
	keylist = {}
	while api:
	#for key in range(100):
		time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
		token = uuid.uuid4()
		key = token
		keylist[time] = key
		if len(keylist) > 10000:
			break
	return keylist


if __name__ == '__main__':
	app.run(debug=True)