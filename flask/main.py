from flask import Flask, render_template, request
import requests

app = Flask(__name__)
@app.route('/')
def main():
    return render_template('index.html')

@app.route('/request', methods=['POST'])
def hello():
    query = request.form['queryInput']
    method = request.form['methodInput']
    return routeRequest(method, query)

def routeRequest(method, query):
	switcher = {
		'GET': requests.get(query, verify=False).text,
		'POST': requests.post(query, verify=False).text,
		'PUT': requests.put(query, verify=False).text,
		'DELETE': requests.delete(query, verify=False).text,
	}
	return switcher.get(method, 'Invalid REST method');
