(function(){
  var app = angular.module('mealPoints', []);
  //change the interpolation from {{ }} to [[ ]]
  app.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  });
  app.controller('mealPlannerCtrl', function(){
    this.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'];
  });
})();
