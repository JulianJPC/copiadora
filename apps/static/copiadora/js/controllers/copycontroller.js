copiadoraApp.controller('copyController',['$scope', '$location', 'copyService',
function($scope, $location, copyService){

    $scope.uploadFile = function(){
        var file = $scope.myFile;
        
        console.log('file is ' );
        console.dir(file);
        
        //var uploadUrl = "/fileUpload";
        //fileUpload.uploadFileToUrl(file, uploadUrl);
    };


}]);