(function(){
  var app = angular.module('mealPoints', []);
  //change the interpolation from {{ }} to [[ ]]
  app.config(function($interpolateProvider){
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  });
  app.controller('mealPlannerCtrl', function(){
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
  });
})();
