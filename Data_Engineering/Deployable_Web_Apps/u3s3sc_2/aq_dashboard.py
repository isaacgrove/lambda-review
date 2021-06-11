"""OpenAQ Air Quality Dashboard with Flask."""
from flask import Flask
import openaq # from .openaq ???
from flask_sqlalchemy import SQLAlchemy

APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(APP)


class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return '<Time {} --- Value {}>'.format(self.datetime, self.value)


@APP.route('/')
def root():
    """Base view."""

    tuples = Record.query.filter(Record.value >= 10).all()
    list_of_tuples = []
    for u in tuples:
        list_of_tuples.append((u.__dict__['datetime'],u.__dict__['value']))


    return str(list_of_tuples)

@APP.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    # TODO Get data from OpenAQ, make Record objects with it, and add to db
    list_of_tuples = list_of_tuples_creator()
    for u in list_of_tuples:
        u = Record(datetime=str(u[0]), value=u[1])
        DB.session.add(u)

    DB.session.commit()
    return 'Data refreshed!'


def list_of_tuples_creator():
    '''contains the python logic for root route'''
    list_of_tuples = []

    api = openaq.OpenAQ()
    status, body = api.measurements(city='Los Angeles', parameter='pm25')

    for dict in body['results']:
        inner_dict = dict.get('date')
        inner_inner = inner_dict.get('utc')
        value = dict.get('value')
        list_of_tuples.append((inner_inner, value))

    return list_of_tuples