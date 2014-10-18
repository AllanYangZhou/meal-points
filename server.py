from flask import Flask, render_template
from datetime import datetime
import time


app = Flask(__name__)

@app.route("/")
def index():
    render_template('index.html')

def meal_point_calculator(mealpoints, date):
	"""Returns a tuple"""


"""Render home page"""


"""Throws back a number"""
@app.route("/<number>")
def calculate():
	## dd/mm/yyyy format
	print (time.strftime("%d/%m/%Y"))
	##mealpoint = meal_point_calculator(mealpoint,datetime.today())

if __name__ == "__main__":
    app.run(debug=True)
