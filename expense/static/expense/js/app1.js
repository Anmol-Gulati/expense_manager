var add = angular.module("add", [])

add.controller('myCtrl', ['$scope', function($scope) {
    $scope.custom = false;
    $scope.Custom = function() {
        $scope.custom = true;
    };
}]);
    