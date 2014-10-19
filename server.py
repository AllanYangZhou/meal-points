from flask import Flask, render_template, request, jsonify
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

def mealCalculate(points, lst):
    cost = 0
    for i in range(4, len(lst)):
        if lst[i]== True:
            if i % 3 == 1:
                cost += 6
            elif i % 3 == 2:
                cost += 7
            elif i % 3 == 0:
                cost += 8
    if lst[0] == True:
        cost += 7
    if lst[1]== True:
        cost += 8
    if lst[2]== True:
        cost += 7
    if lst[3]== True:
        cost += 8
    daysLeft = date.today()
    semesterEnd = date(2014, 12, 19)
    delta = (semesterEnd-daysLeft).days
    weeks = delta//7
    fullcost = weeks*cost
    today = date.weekday(daysLeft)
    if today != 5:
        if today == 6:
            if lst[2] == True:
                fullcost += 7
            if lst[3] == True:
                fullcost += 8
            today = 0
        for i in range(today*3 + 4, len(lst)):
            if lst[i] == True:
                if i % 3 == 1:
                    fullcost += 6
                elif i % 3 == 2:
                    fullcost += 7
                elif i % 3 == 0:
                    fullcost += 8
                
    print(fullcost)
    if points >= fullcost:
        return (points - fullcost, None, (points-fullcost)/weeks)
    if points < fullcost:
        return (points - fullcost, points//cost, (points-fullcost)/weeks)

@app.route("/results", methods = ["POST"])
def calculate():
    json_data = request.get_json()
    mealpoints = json_data['mealpoints']
    whichMeals = []
    def addlist(meals):
        if json_data[meals] == True:
            print(meals)
            whichMeals.append(True)
        else:
            whichMeals.append(False)

    addlist("Saturdaybrunch")
    addlist("Saturdaydinner")
    addlist("Sundaybrunch")
    addlist("Sundaydinner")
    addlist("Mondaybreakfast")
    addlist("Mondaylunch")
    addlist("Mondaydinner")
    addlist("Tuesdaybreakfast")
    addlist("Tuesdaylunch")
    addlist("Tuesdaydinner")
    addlist("Wednesdaybreakfast")
    addlist("Wednesdaylunch")
    addlist("Wednesdaydinner")
    addlist("Thursdaybreakfast")
    addlist("Thursdaylunch")
    addlist("Thursdaydinner")
    addlist("Fridaybreakfast")
    addlist("Fridaylunch")
    addlist("Fridaydinner")
    print(whichMeals[0])
    decision = mealCalculate(float(mealpoints), whichMeals)

    if decision[1] == None:
        """Too many meal points"""
        excess = decision[0]
        mealPointsPerWeek = decision[2]
        #return render_template('results.html',current = mealpoints, excessPoints = excess, mealPointsPerWeek = mealPointsPerWeek)
        #return [mealpoints, excess, mealPointsPerWeek]
        f = {'result': 'true', 'mealpoints': mealpoints, 'excess': excess, 'mealPointsPerWeek': mealPointsPerWeek}
        return jsonify(**f)

    else:
        """Too little meal points"""
        deficit = decision[0]
        weeksleft = decision[1]
        additionPoints = decision[2]
        #return render_template('deficit.html',current = mealpoints, deficitPoints = abs(deficit), weeksleft = weeksleft, additionPoints = abs(additionPoints) )
        #return [mealpoints, abs(deficit), weeksleft]
        f = {'result': 'false', 'mealpoints': mealpoints, 'deficit': abs(deficit), 'weeksleft': weeksleft}
        return jsonify(**f)

if __name__ == "__main__":
    app.run(debug=True)
