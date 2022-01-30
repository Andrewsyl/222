from tkinter import N
from flask import Flask, jsonify, redirect, render_template, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from importlib_metadata import os
import requests
import json
from models import Sensor


app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'

basedir = os.path.abspath(os.path.dirname(__file__))

# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')


db = SQLAlchemy(app)


class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(20),  nullable=False)
    city = db.Column(db.String(20),  nullable=False)
    temperature = db.Column(db.Integer)
    wind_speed = db.Column(db.Integer)
    humidity = db.Column(db.Integer)

    def __init__(self, city, country):
        self.city = city
        self.country = country

    def __repr__(self):
        return '<Name %r>' % self.id

@app.route('/', methods=['GET', 'POST'])
def home():
    all_products = Sensor.query.all()
    if not all_products:
        all_products = []
    for product in all_products:
        print(product)
    return render_template('home.html', data=all_products)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        city = request.form.get('city').capitalize()
        country = request.form.get('country').capitalize()
        new_sensor = Sensor(city, country)

        db.session.add(new_sensor)
        db.session.commit()
        flash("{}, {} Sensor Added.".format(city,country))
        return redirect('/')
    else:        
        return render_template('add_sensor.html')


@app.route('/sensors', methods=['GET'])
def get_products():
    all_products = Sensor.query.all()
    if not all_products:
        all_products = None
    return all_products

@app.route('/sensor_info/<int:id>', methods=['GET'])
def sensor_info(id):
    sensor = Sensor.query.get_or_404(id)
    api_key = "32d282f95e85a07b04c4c1c7c0090202";
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&appid={}'.format(sensor.city,'IE',api_key)
    response = requests.get(url)
    data = json.loads(response.text)



    return render_template('sensor.html', data=sensor,weather=data)


@app.route('/delete/<int:id>')
def delete(id):
    sensor_to_delete = Sensor.query.get_or_404(id)
    db.session.delete(sensor_to_delete)
    db.session.commit()
    flash("{}, {} Was Deleted.".format(sensor_to_delete.city,sensor_to_delete.country))
    all_products = Sensor.query.all()
    if not all_products:
        all_products = []
    for product in all_products:
        print(product)
    return render_template('home.html', data=all_products)


if __name__ == '__main__':
    app.run()
