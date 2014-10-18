from flask import Flask, render_template, request
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

def pointsToMeals(points):
    dayMeals = round(mealPointCalculator(points)[0]/7.5, 1)
    dayWeeks = round(mealPointCalculator(points)[1]/7.5, 1)
    return(dayMeals,dayWeeks)


@app.route("/results", methods = ["POST"])
def calculate():
	##print(point)
	# dd/mm/yyyy format
	##print (time.strftime("%d/%m/%Y"))
	#mealpoint = meal_point_calculator(mealpoint,datetime.today())
	mealpoints = request.form['mealpoints']

	return render_template('results.html', mealPoints = mealPointCalculator(int(mealpoints)), meals = pointsToMeals(int(mealpoints)))
	##return str(mealPointCalculator(request.form['mealPoints']))

if __name__ == "__main__":
    app.run(debug=True)
