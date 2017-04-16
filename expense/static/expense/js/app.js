var app = angular.module("app", ["chart.js"])

app.config(function($httpProvider, $interpolateProvider){
	$httpProvider.defaults.headers.common['Cache-Control'] = 'no-cache';
    $httpProvider.defaults.cache = false;
    $interpolateProvider.startSymbol('{[{').endSymbol('}]}');
});

app.controller("ListCtrl", function ($scope, $http) {
    $scope.labels = [];
    $scope.data = [];
    $http({ cache: false, url: 'http://127.0.0.1:8000/api/v1/expenses/', method: 'GET' }).success(function (data){
        $scope.expense = data; // get data from json      
    });
});

app.controller("PieCtrl", function ($scope, $http) {
	$scope.labels = [];
	$scope.data = [];
	$http({ cache: false, url: 'http://127.0.0.1:8000/expense/view_pie_expense/', method: 'GET' }).success(function (data){
		$scope.expense = data; // get data from json
        $scope.labels = $scope.expense.expense;
        $scope.data = $scope.expense.amount;      
    });
});

app.controller("BarCtrl", function ($scope, $http) {
	$scope.labels = [];
	$scope.data = [];
	$http({ cache: false, url: 'http://127.0.0.1:8000/expense/view_bar_expense/', method: 'GET' }).success(function (data){
		$scope.expense = data; // get data from json
        $scope.labels = $scope.expense.created_at;
        $scope.data = $scope.expense.amount;    
    });
});          