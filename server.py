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

def mealOptimize(points, lst):
    cost = 0
    for i in range(4, len(lst)):
        if lst[i]:
            if i % 3 == 1:
                cost += 6
            elif i % 3 == 2:
                cost += 7
            elif i % 3 == 0:
                cost += 8
    if lst[0]:
        cost += 7
    if lst[1]:
        cost += 8
    if lst[2]:
        cost += 7
    if lst[3]:
        cost += 8
    daysLeft = date.today()
    semesterEnd = date(2014, 12, 19)
    delta = (semesterEnd-daysLeft).days
    weeks = delta//7
    fullcost = weeks*cost
    today = date.weekday(daysLeft)
    if today != 5:
        if today == 6:
            if lst[2]:
                fullcost += 7
            if lst[3]:
                fullcost += 8
            today = 0
        for i in range(today*3 + 4, len(lst)):
            if lst[i]:
                if i % 3 == 1:
                    fullcost += 6
                elif i % 3 == 2:
                    fullcost += 7
                elif i % 3 == 0:
                    fullcost += 8
                
    
    if points >= fullcost:
        return (points - fullcost, None)
    if points < fullcost:
        return (points - fullcost, points//cost)

@app.route("/results", methods = ["POST"])
def calculate():
	mealpoints = request.form['mealpoints']

	whichMeals = []

	def addlist(meals):
		if meals in request.form == True:
			whichMeals.append(True)
		else:
			whichMeals.append(False)

	addlist("Saturday-brunch")
	addlist("Saturday-dinner")
	addlist("Sunday-brunch")
	addlist("Sunday-dinner")
	addlist("Monday-breakfast")
	addlist("Monday-lunch")
	addlist("Monday-dinner")
	addlist("Tuesday-breakfast")
	addlist("Tuesday-lunch")
	addlist("Tuesday-dinner")
	addlist("Wednesday-breakfast")
	addlist("Wednesday-lunch")
	addlist("Thursday-breakfast")
	addlist("Thursday-lunch")
	addlist("Thursday-dinner")
	addlist("Friday-breakfast")
	addlist("Friday-lunch")
	addlist("Friday-dinner")

	mealPointsPerDay = mealPointCalculator(int(mealpoints))[0]
	mealPointsPerWeek = mealPointCalculator(int(mealpoints))[1]
	meals = pointsToMeals(int(mealpoints))
	return render_template('results.html',mealPoints = mealpoints ,mealPointsPerDay = mealPointsPerDay, mealPointsPerWeek = mealPointsPerWeek, meals = meals)


if __name__ == "__main__":
    app.run(debug=True)
