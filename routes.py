from flask import Flask, render_template, redirect, request
from query import *
import json
import time

app = Flask(__name__)

# Main
@app.route('/')
def index():
   return redirect('/view')


# Main View
@app.route('/view', methods=['GET', 'POST'])
def view():
    db = Database()
    res = db.list_payment()
    return render_template('view.html', result=res, content_type='application/json')


# Delete Data
@app.route('/delete', methods=['GET', 'POST'])
def delete():
	if request.method == 'GET':
			return render_template('403.html')
	try:
		id = int(request.form['id_payments'])
	except:
		return redirect('/failedquery')
	db = Database()
	db.delete_payment(int(id))
	return redirect('/view')


# Inset Data Dari Modal Insert
@app.route('/db_insert', methods=['GET', 'POST'])
def db_insert():
	if request.method == 'GET':
			return render_template('403.html')
	try:
		item = str(request.form['Item'])
		count = int(request.form['Count'])
		price = int(request.form['Price'])
		inputs = [item, count, price]
	except:
		return redirect('/failedquery')
	db = Database()
	db.insert_payment(inputs)
	return redirect('/view')


# Update Data Dari Modal Update
@app.route('/db_update', methods=['GET', 'POST'])
def db_update():
	if request.method == 'GET':
			return render_template('403.html')
	try:
		item = str(request.form['Items'])
		count = int(request.form['Counts'])
		price = int(request.form['Prices'])
		paid = int(request.form['Paids'])
		id = int(request.form['id_payment'])
		inputs = [item, count, price, paid, id]
	except:
		return redirect('/failedquery')
	db = Database()
	db.update_payment(inputs)
	return redirect('/view')


# Get Data Untuk Default Value Dari Modal Update
@app.route('/db_list_update/<id>', methods=['GET', 'POST'])
def db_list_update(id):
	if request.method == 'GET':
			return render_template('403.html')
	try:
		db = Database()
		res = db.list_payment_updates(id)
		return json.dumps(res)
	except:
		return redirect('/view')


# Notifikasi Jika Query Gagal
@app.route('/failedquery', methods=['GET', 'POST'])
def failedquery():
	if request.method == 'POST':
			return render_template('403.html')
	return render_template('failed.html')
