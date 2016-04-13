from flask import Flask
from string import Template
app = Flask(__name__)

HTML_TEMPLATE = Template("""
<h1>Hello, ${place_name}!<h1>

<img src="https://maps.googleapis.com/maps/api/staticmap?size=700x300&markers=${place_name}" alt="map of ${place_name}">

<img src="https://maps.googleapis.com/maps/api/streetview?size=700x300&location=${place_name}" alt="street view of ${place_name}">
""")


UNIQUE_YOUTUBE_ID = Template("""
<iframe width="560" height="315" src="https://www.youtube.com/embed/${VIDID}" frameborder="0" allowfullscreen></iframe>
""")


@app.route("/")
def homepage():
	return"""
	<h1>Hello world!<h1>
	<p>This is my first web app!</p>
	"""
	#(UNIQUE_YOUTUBE_ID.substitute(VIDID=yyy))

@app.route("/places/<thing>")
def somepath(thing):
	return(HTML_TEMPLATE.substitute(place_name=thing))

@app.route("/weather/<blah>")
def weather_view(blah):
	s = """I don't know what the weather is in {zzz}"""
	return s.format(zzz=blah)

@app.route("/Chicago")
def blahpage():
	return """<h1>Chicago<h1>
	<iframe width="420" height="315" src="https://www.youtube.com/embed/pNFryicvxeE" frameborder="0" allowfullscreen></iframe>
	"""

@app.route("/LA")
def zzzz():
	return """<h1>L.A.<h1>
	<img src="http://readingpartners.org/wp-content/uploads/2015/02/LosAngeles.jpg">
	"""

@app.route("/rawr")
def gamesgames():
	return """
<!DOCTYPE html>
</head>
	<title>My title</title>
</head>
<body style="width: 880px; margin: auto;">
	<h1>RAWR!</h1>
	<p>here's a paragraph...</p>
	<p>And here's an image:</p>
	<a href="http://goodnature.nathab.com/wp-content/uploads/2011/03/19-baby-tiger.jpg">
		<img src="http://goodnature.nathab.com/wp-content/uploads/2011/03/19-baby-tiger.jpg" alt="it's a nice sunset">
	</a>
</body>
"""

@app.route("/for/<name>")
def mostly_for_max(name):
	s = """I don't know what the weather is in {blah}"""
	return(FOR_MAX.substitute(resident_name=name))

FOR_MAX = Template(""" 
<!DOCTYPE html>
</head>
	<title>My title</title>
</head>
	<body style="width: 880px; margin: auto;">
	<h1>Hello, ${resident_name}!<h1>
	<p>Welcome to my first web app.</p>
	<p>Here's a dog to keep you company:</p>
		<img src=https://s-media-cache-ak0.pinimg.com/736x/e6/58/8e/e6588e786571b615fc3efa842cd9bee3.jpg>
""")

#img_src = ""
	#if name == "Max":
	#	img_src == "http://i2.cdn.turner.com/cnnnext/dam/assets/150324154025-14-internet-cats-restricted-super-169.jpeg"
	#if name == "Ryan":
		#img_src == "https://s-media-cache-ak0.pinimg.com/736x/e6/58/8e/e6588e786571b615fc3efa842cd9bee3.jpg"
	#if name == "Hails":
		#img_src == ""



HTML_TEMPLATE = Template("""
<h1>Hello, ${place_name}!<h1>

<img src="https://maps.googleapis.com/maps/api/staticmap?size=700x300&markers=${place_name}" alt="map of ${place_name}">

<img src="https://maps.googleapis.com/maps/api/streetview?size=700x300&location=${place_name}" alt="street view of ${place_name}">
""")


if __name__ == '__main__':
	app.run(debug=True, use_reloader=True)

