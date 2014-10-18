from flask import Flask, render_template
from datetime import datetime, date
import time


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

def mealPointCalculator(points):
    daysLeft = date.today()
    semesterEnd = date(2014, 12, 19)
    delta = (semesterEnd-daysLeft).days
    return (round((points/delta),1), round((points*7/delta),1))


"""Render home page"""


"""Throws back a number"""
@app.route("/results", methods = ["POST"])
def calculate():
	# dd/mm/yyyy format
	##print (time.strftime("%d/%m/%Y"))
	#mealpoint = meal_point_calculator(mealpoint,datetime.today())
	return str(mealPointCalculator())

if __name__ == "__main__":
    app.run(debug=True)
