from flask import Flask
import os 
app = Flask(__name__)
from flask import Flask, render_template, request, redirect, g

@app.route("/")
def home():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")

@app.route("/art")
def art():
	arts_small = []
	arts_big = []
	app_dir = "/var/www/FlaskApp/FlaskApp/" 
	img_folder = "/var/www/FlaskApp/FlaskApp/static/img/paintings"
	for f in os.listdir(img_folder):
		arts_small.append(os.path.join(img_folder, f).replace(app_dir, ""))
		arts_big.append(os.path.join(img_folder, f).replace(app_dir, ""))
		
        return render_template("art.html", photos_small=enumerate(arts_small), photos_big=enumerate(arts_big))

@app.route("/contact")
def contact():
        return render_template("contact.html")

@app.route("/tech")
def tech():
	return render_template("tech.html") 


if __name__ == "__main__":
    	app.run(debug=True, host='0.0.0.0')
