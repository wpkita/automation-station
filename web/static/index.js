angular
.module('automationStation', ['ngResource'])
.controller('MainController', function($http, $scope) {
    $http.get('/tasks')
      .success(function(response) {
        $scope.tasks = response.tasks;
      });

    $scope.runTask = function(task) {
      $http({
        url: '/run/' + task.name,
        method: 'PUT'
      });
    };

    // TODO: Create directive for this
    var dragDrop = document.getElementById('newTask');
    dragDrop.addEventListener('dragover', function(event) {
      event.stopPropagation();
      event.preventDefault();
    });
    dragDrop.addEventListener('drop', function(event) {
      event.stopPropagation();
      event.preventDefault();

      var files = event.dataTransfer.files;

      for (var i = 0; i < files.length; i++)
      {
        $http.post('/task/' + files[i].name);
      }
    });

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
