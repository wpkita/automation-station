angular
.module('automationStation', ['ngResource'])
.controller('MainController', function($http, $scope) {
    $http.get('/tasks')
      .success(function(response) {
        $scope.tasks = response.tasks;
      });

    $scope.runTask = function(task) {
      $http({
        url: '/task/' + task.name,
        method: 'GET'
      });
    };
  });
