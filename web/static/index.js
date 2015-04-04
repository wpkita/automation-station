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
        method: 'POST'
      });
    };

    if (window.location.hash) {
      $http.post('/token', hashToDict(window.location.hash));
    }

    function hashToDict(hash) {
      var dict = {};

      // Split the query parameters from the hash
      angular.forEach(hash.replace(/#|\//g, '').split('&'), function(pair) {
        var tuple = pair.split('=');
        dict[tuple[0]] = tuple[1];
      });

      return dict;
    }
  });
