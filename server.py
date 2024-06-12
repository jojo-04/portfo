import csv

from flask import Flask, render_template, request, redirect
import os


app = Flask(__name__)


def data_csv(data):
    with open('database.csv', 'a') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


@app.route("/")
def home_page():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data_submitted = request.form.to_dict()
        data_csv(data_submitted)
        return redirect('/thankyou.html')
    else:
        return 'The form was not submitted correctly. Please try again.'


app.run()
