var app = angular.module("app", ["chart.js"])

app.controller("PieCtrl", function ($scope, $http) {
	$scope.labels = [];
	$scope.data = [];
	$http({ cache: false, url: 'http://127.0.0.1:8000/api/v1/expenses/', method: 'GET' }).success(function (data){
		$scope.expense = data; // get data from json
        for(var i=0;i<$scope.expense.length;i++){
        	$scope.labels.push($scope.expense[i].category + ": " + $scope.expense[i].description + "-->Rs");
        	$scope.data.push($scope.expense[i].amount);
        }      
    });
});
              