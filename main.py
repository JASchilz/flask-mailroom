import logging
import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session, flash


logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

from model import Donation, Donor

app = Flask(__name__)
app.secret_key = b'\x9d\xb1u\x08%\xe0\xd0p\x9bEL\xf8JC\xa3\xf4J(hAh\xa4\xcdw\x12S*,u\xec\xb8\xb8'


@app.route('/')
def home():
    return redirect(url_for('all'))


@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/add/', methods=['GET', 'POST'])
def add():
    if request.method == 'GET':
        return render_template('add.jinja2')
    else:
        donor_name = Donor(name=request.form['name'])
        donation_amount = request.form['donation']
        
        #find the donor using peewee wrapper
        donor = Donor.select().where(Donor.name == donor_name).get()

        # Make a donation entry peewee object
        donation = Donation(value=donation_amount, donor=donor)
        donor = Donor(donor_name)
        donation.save()
        logging.info('Trying to add name')

        return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(debug=True)  # TODO Remove after testing
    # port = int(os.environ.get("PORT", 6738))
    # app.run(host='0.0.0.0', port=port)
