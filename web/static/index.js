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
})
.directive('droppy', function($http) {
  return {
    link: function(scope, element) {
      var onError = function() {
        console.error.apply(console, arguments);
      };

      var onDropboxUploadSuccess = function() {
        console.log('Dropbox upload succeeded.');
        console.log.apply(console, arguments);
      };

      var onTaskCreateSuccess = function(reader, file) {
        return function() {
          console.log('Task creation succeeded.');

          $http.defaults.headers.common.Authorization = 'Bearer lDLOK96Bm08AAAAAAAGVMP08b3t_93anf58LHdqMBcjs61Ez2MtTLGxEcvnWDrI_';

          $http.post('https://api-content.dropbox.com/1/files_put/auto/' + file.name, reader.result)
            .success(onDropboxUploadSuccess)
            .error(onError);

          scope.tasks.push({
            name: file.name,
            path: file.name
          });
        }
      };

      element.on('dragover', function(event) {
        event.preventDefault();
      });

      element.on('drop', function(event) {
        event.preventDefault();

        var files = event.dataTransfer.files;

        if (files) {
          var reader = new FileReader();
          var file = files[0];

          reader.onloadend = function() {
            $http.post('/task/' + file.name)
              .success(onTaskCreateSuccess(reader, file))
              .error(onError);
          };

          reader.readAsBinaryString(file);
        }
      });
    }
  }
});
