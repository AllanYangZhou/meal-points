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
        if lst[i]== False:
            if i % 3 == 1:
                cost += 6
            elif i % 3 == 2:
                cost += 7
            elif i % 3 == 0:
                cost += 8
    if lst[0] == False:
        cost += 7
    if lst[1]== False:
        cost += 8
    if lst[2]== False:
        cost += 7
    if lst[3]== False:
        cost += 8
    daysLeft = date.today()
    semesterEnd = date(2014, 12, 19)
    delta = (semesterEnd-daysLeft).days
    weeks = delta//7
    fullcost = weeks*cost
    today = date.weekday(daysLeft)
    if today != 5:
        if today == 6:
            if lst[2] == False:
                fullcost += 7
            if lst[3] == False:
                fullcost += 8
            today = 0
        for i in range(today*3 + 4, len(lst)):
            if lst[i] == False:
                if i % 3 == 1:
                    fullcost += 6
                elif i % 3 == 2:
                    fullcost += 7
                elif i % 3 == 0:
                    fullcost += 8
                
    
    if points >= fullcost:
        return (points - fullcost, None, (points-fullcost)/weeks)
    if points < fullcost:
        return (points - fullcost, points//cost, 0)

@app.route("/results", methods = ["POST"])
def calculate():
	mealpoints = request.form['mealpoints']

	whichMeals = []

	def addlist(meals):
		if request.form.get(meals, True) == True:
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

	decision = mealOptimize(int(mealpoints), whichMeals)
	print(int(mealpoints))
	print(whichMeals)
	print(decision)

	if decision[1] == None:
		"""Too many meal points"""
		excess = decision[0]
		mealPointsPerWeek = decision[2]
		return render_template('results.html',current = mealpoints, excessPoints = excess, mealPointsPerWeek = mealPointsPerWeek)

	else:
		"""Too little meal points"""
		deficit = decision[0]
		weeksleft = decision[1]
		return render_template('deficit.html',current = mealpoints, deficitPoints = abs(deficit), weeksleft = weeksleft)

if __name__ == "__main__":
    app.run(debug=True)
