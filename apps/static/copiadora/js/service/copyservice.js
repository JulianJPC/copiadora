copiadoraApp.factory('copyService', ['$http', '$rootScope', '$location',
function($http, $rootScope, $location){
    var service = {};

    service.getajax = function(destiny, callback){
        var url = destiny;
        $http.get(url).
        success(function(response){
            callback(response);
        }).error(function(response){
            callback(response);
        });
    };

    return service;
}]);