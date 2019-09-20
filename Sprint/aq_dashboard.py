from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import openaq


APP = Flask(__name__)
APP.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
DB = SQLAlchemy(APP)


class Record(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    datetime = DB.Column(DB.String(25))
    value = DB.Column(DB.Float, nullable=False)

    def __repr__(self):
        return '< Time {} -- Value {} >'.format(self.datetime, self.value)

# making list of tuples from the 2 lists 
def make_list(list1, list2):
    list = [(list1[i], list2[i]) for i in range(0, len(list1))]
    return list

# getting list of tuples of datetimes and values
def get_datetimeValues(city, parameter):
    api = openaq.OpenAQ()
    status, body = api.measurements(city=city, parameter=parameter)
    if status == 200:
        utc_datetimes = [result['date']['utc'] for result in body['results']]
        values = [result['value'] for result in body['results']]
        tuple_list = make_list(utc_datetimes, values)
    return tuple_list
       

@APP.route('/')
def base():
    records = Record.query.filter(Record.value>=10).all()
    return render_template('base.html', records=records)    



@APP.route('/refresh')
def refresh():
    """Pull fresh data from Open AQ and replace existing data."""
    DB.drop_all()
    DB.create_all()
    # TODO Get data from OpenAQ, make Record objects with it, and add to db
    for time_value in get_datetimeValues('Los Angeles', 'pm25'):
        record = Record(datetime=str(time_value[0]), value=time_value[1])
        DB.session.add(record)
    DB.session.commit()
    return 'Data refreshed!'



if __name__ == '__main__':
    APP.run(debug=True)    