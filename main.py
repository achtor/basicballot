from flask import Flask, render_template, request
from pygeocoder import Geocoder

app = Flask(__name__)

@app.route('/')
def root():
   return render_template('index.html')

@app.route('/_geo')
def geocode():
   return str(Geocoder.geocode(request.args.get('address'))[0].coordinates)

if __name__ == '__main__':
   app.run()
