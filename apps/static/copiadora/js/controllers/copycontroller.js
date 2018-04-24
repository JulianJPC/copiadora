copiadoraApp.controller('copyController',['$scope', '$location', 'copyService',
function($scope, $location, copyService){

    $scope.songs = null;
    $scope.fullSongs = null;

    $scope.uploadFile = function(){
        var file = $scope.myFile;

        //var fd = new FormData();
        //fd.append('file', file);
        //console.log('file is ' );
        //console.dir(file);
        
        copyService.file(file)(function(response){
            if(response.success){
                $scope.songs = response.songs;
                $scope.fullSongs = response.fullsongs;
            }
            if(response.error){
                console.log(response.error)
            }
        })
    };

}]);