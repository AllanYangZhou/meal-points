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
	mealpoints = request.form['mealpoints']
	
	
	mealPointsPerDay = mealPointCalculator(int(mealpoints))[0]
	mealPointsPerWeek = mealPointCalculator(int(mealpoints))[1]
	meals = pointsToMeals(int(mealpoints))
	return render_template('results.html',mealPoints = mealpoints ,mealPointsPerDay = mealPointsPerDay, mealPointsPerWeek = mealPointsPerWeek, meals = meals)


if __name__ == "__main__":
    app.run(debug=True)
