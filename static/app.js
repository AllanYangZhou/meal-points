(function(){
  var app = angular.module('mealPoints', []);
  //change the interpolation from {{ }} to [[ ]]
  app.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  });
  app.controller('mealPlannerCtrl', ['$http', function($http){
    var planner = this;
    this.currentPts = 0;
    this.excessPts = 0;
    this.deficitPts = 0;
    this.mealPointsPerWeek = 0;
    this.weeksLeft = 'hello';
    this.hasResults = false;
    this.hasDeficit = false;
    this.weekEnds = [{name:'Saturday'}, {name:'Sunday'}];
    this.formData = {
      Mondaybreakfast : true,
      Mondaylunch: true,
      Mondaydinner: true,
      Tuesdaybreakfast : true,
      Tuesdaylunch: true,
      Tuesdaydinner: true,
      Wednesdaybreakfast : true,
      Wednesdaylunch: true,
      Wednesdaydinner: true,
      Thursdaybreakfast : true,
      Thursdaylunch: true,
      Thursdaydinner: true,
      Fridaybreakfast : true,
      Fridaylunch: true,
      Fridaydinner: true,
      Saturdaybrunch: true,
      Saturdaydinner: true,
      Sundaybrunch: true,
      Sundaydinner: true,
    };
    this.sendData = function(){
      $http.post('/results', this.formData)
        .success(function(data, status, headers, config){
          console.log(data.result)
          if(data.result=='true'){
            planner.hasResults = true;
            planner.hasDeficit= false;
            planner.currentPts = data.mealpoints;
            planner.excessPts = data.excess;
            planner.mealPointsPerWeek = data.mealPointsPerWeek;
          } else {
            planner.hasDeficit = true;
            planner.hasResults = false;
            planner.currentPts = data.mealpoints;
            planner.deficitPts = data.deficit;
            planner.weeksLeft = data.weeksLeft;
          }
        })
        .error(function(data, status, headers, config){
          console.log(data);
        });
    };
  }]);
})();
