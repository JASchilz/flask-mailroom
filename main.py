import os
import base64

from flask import Flask, render_template, request, redirect, url_for, session

from model import Donation, Donor

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('all'))

@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        donor = Donor.select().where(Donor.name == request.values.get('name')).get()
        donation = Donation(donor=donor, value=request.values.get('donation') )
        donation.save()
        return redirect(url_for('all'))
    else:
        return render_template('donate.jinja2')

    

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    app.run(host='0.0.0.0', port=port)

