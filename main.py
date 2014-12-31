from flask import Flask, render_template, request
from pygeocoder import Geocoder

app = Flask(__name__)

@app.route('/')
def root():
   return render_template('index.html')

@app.route('/_geo')
def geocode():
   return str(Geocoder.geocode(request.args.get('address'))[0].coordinates)

@app.route('/_precinct')
def precinct():
   # take in coordinates through GET (POST?) and return either:
   # the corresponding geojson feature from Precincts.geojson, or
   # some kind of json error message if none exists

if __name__ == '__main__':
   app.run()
