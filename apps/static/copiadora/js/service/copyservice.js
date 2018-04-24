 var copyWebServiceURL = "";

copiadoraApp.factory('copyService', ['$http', '$rootScope', '$location',
function($http, $rootScope, $location){
    var service = {};

    service.file = function(file, callback){
        var url = copyfileURL;
        $http.post(url, file).
        success(function(response){
            callback(response);
        }).error(function(response){
            callback(response);
        });
    };

    return service;
}]);