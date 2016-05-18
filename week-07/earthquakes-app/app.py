from flask import Flask
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")

    return """
    <h1>Latest Major Earthquakes Worldwide</h1>
    <p>According to the [USGS Earthquake Feeds](http://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php), there have been X major earthquakes in the past 30 days since {time}.</p>

    <p>See raw CSV: http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/significant_month.csv</p>

    <img src="http://loremflickr.com/600/400">
    """.format(time=the_time)

from urllib.parse import urlencode
GMAPS_URL = 'https://maps.googleapis.com/maps/api/staticmap?'
locations = ['Stanford, CA', 'Berkeley, CA', 'Napa, CA']
myparams = {'size': '800x400', 'maptype': 'satellite', 'markers': locations}

url = GMAPS_URL + urlencode(myparams, doseq=True)
# https://maps.googleapis.com/maps/api/staticmap?size=800x400&maptype=satellite&markers=Stanford%2C+CA&markers=Berkeley%2C+CA&markers=Napa%2C+CA

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)