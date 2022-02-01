from datetime import datetime
from email.policy import default
from tkinter import N
from flask import Flask, jsonify, redirect, render_template, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from importlib_metadata import os
import requests
import json
import datetime
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SESSION_TYPE'] = 'memcached'
app.config['SECRET_KEY'] = 'super secret key'

basedir = os.path.abspath(os.path.dirname(__file__))

# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')


db = SQLAlchemy(app)
migrate = Migrate(app, db)

class Weather(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Integer)
    wind_speed = db.Column(db.Integer)
    humidity = db.Column(db.Integer)
    sensor_id = db.Column(db.Integer, db.ForeignKey('sensor.id'))
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())
    


class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    country = db.Column(db.String(20),  nullable=False)
    city = db.Column(db.String(20),  nullable=False)
    weather = db.relationship('Weather',backref='weather')

    def __init__(self, city, country):
        self.city = city
        self.country = country

    def __repr__(self):
        return '<Name %r>' % self.id



# Home page lists all sensors from database
@app.route('/', methods=['GET', 'POST'])
def home():
    all_products = Sensor.query.all()
    if not all_products:
        all_products = []
    return render_template('home.html', data=all_products)

# Page for adding senors
@app.route('/add', methods=['GET', 'POST'])
def add():
    try:
        if request.method == 'POST':
            city = request.form.get('city').capitalize()
            country = request.form.get('country').capitalize()
            if not city.isalpha() or not country.isalpha():
                flash("Loactions must only contain letters.".format(city,country))
                return redirect('/add')
            new_sensor = Sensor(city, country)
            db.session.add(new_sensor)
            db.session.commit()
            flash("{}, {} Sensor Added.".format(city,country))
            return redirect('/')
    except Exception as e:
        print(e)
        return redirect('/')
    else:        
        return render_template('add_sensor.html')


@app.route('/sensor_info/<int:id>', methods=['GET','POST'])
def sensor_info(id):
    try:
        query_data = {}
        all_sensor_weather = Weather.query.filter_by(sensor_id=id).filter()
        sensor = Sensor.query.get_or_404(id)
        api_key = "32d282f95e85a07b04c4c1c7c0090202";
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(sensor.city,api_key)
        response = requests.get(url)
        data = json.loads(response.text)
        if request.method == 'POST':
            start_date = request.form.get('date-start')
            end_date = request.form.get('date-end')
            query_data['start_date'] = start_date
            query_data['end_date'] = end_date
            all_sensor_weather = Weather.query.filter_by(sensor_id=id).filter(Weather.created_at.between(start_date,end_date))
            hum = 0
            temp = 0
            wind_speed = 0
            count = 0
            for s_data in all_sensor_weather:
                temp += s_data.temperature
                hum += s_data.humidity
                wind_speed += s_data.wind_speed
                count +=1
            try:
                query_data['temp'] = str(round(temp/count, 2))
                query_data['wind_speed'] =  str(round(wind_speed/count, 2))
                query_data['hum'] = (round(hum/count, 2))
                return render_template('sensor.html', data=sensor,weather=data,query_data=query_data)
            except:
                flash('No weather data in that range. Please try a new range.')
                return render_template('sensor.html', data=sensor,weather=data)
        else:
            new_weather = Weather(temperature=data['main']['temp'],humidity=data['main']['humidity'], wind_speed=data['wind']['speed'], sensor_id=sensor.id)
            db.session.add(new_weather)
            db.session.commit()
            return render_template('sensor.html', data=sensor,weather=data)
    except Exception as e:
        print (e)
        return redirect('/')


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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')


if __name__ == '__main__':
    app.run()
