angular
  .module('automationStation', [])
  .controller('MainController', function($scope) {
    $scope.tasks = [{
      name: 'HelloWorld'
    }];

    $scope.newTask = {
      name: ''
    };

    $scope.addNewTask = function(newTask) {
      $scope.tasks.push(newTask);

      $scope.newTask = {
        name: ''
      };
    }
  });
