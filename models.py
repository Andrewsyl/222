


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