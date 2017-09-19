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
	init_dirname = os.path.dirname(os.path.abspath(__file__))
	img_folder = os.path.join(init_dirname, "static/img/paintings")
	for f in os.listdir(img_folder):
		arts_small.append(os.path.join(img_folder, f).replace(init_dirname, ""))
		arts_big.append(os.path.join(img_folder, f).replace(init_dirname, ""))
        return render_template("art.html", photos_small=enumerate(arts_small), photos_big=enumerate(arts_big))

@app.route("/contact")
def contact():
        return render_template("contact.html")

@app.route("/tech")
def tech():
	return render_template("tech.html") 


if __name__ == "__main__":
    	app.run(debug=True, host='0.0.0.0')
