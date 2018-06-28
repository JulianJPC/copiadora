copiadoraApp.controller('copyController',['$scope', '$location', 'copyService',
function($scope, $location, copyService){

    $scope.error = false;

    $scope.numberblocks = "";
    $scope.startnumber = null;
    $scope.endnumber = null;
    $scope.counter = 0;

    $scope.looper = 0;
    $scope.keyLooper = false;
    $scope.endloop = 527639;

    $scope.offbutton = false;

    $scope.AllBlocks = [];
    $scope.DiffTime = [];

    $scope.getData= function(){

            $scope.buttonAction();

            if($scope.startnumber == null){
                $scope.startnumber = 1;
                $scope.endnumber = 51;
            }else{
                $scope.startnumber = $scope.counter * 50 + 1;
                $scope.endnumber = $scope.counter * 50 + 51;
            };

            if($scope.endnumber > parseInt($scope.endloop)){
                $scope.endnumber = parseInt($scope.endloop);
            }

            for(x = $scope.startnumber; x < $scope.endnumber; x++){
                if(x != $scope.endnumber - 1){
                    $scope.numberblocks = $scope.numberblocks + x.toString() + ",";
                }else{
                    $scope.numberblocks = $scope.numberblocks.toString() + x.toString()
                }
            };
            var apiPath = "https://chain.api.btc.com/v3/block/";

            var apiblocks = apiPath + $scope.numberblocks;

            $scope.counter = $scope.counter + 1;

            copyService.getajax(apiblocks, function(response){
                if(response == null){
                    $scope.counter = $scope.counter - 1;
                    $scope.error = true;
                    setTimeout(function() {
                        $scope.numberblocks = "";
                        $scope.buttonAction();
                        $scope.looper = $scope.looper + 1;
                        $scope.$digest();
                    }, 20000);
                }else{
                    $scope.numberblocks = "";
                    $scope.buttonAction();
                    for(x = 0; x < response.data.length; x++){
                        $scope.AllBlocks.push(response.data[x]);
                    }

                    if($scope.endnumber != parseInt($scope.endloop)){
                        setTimeout(function() {
                            $scope.looper = $scope.looper + 1;
                            $scope.$digest();
                        }, 2000);
                    }        
                }
                
            });       
    };

    $scope.watchblocks = function(){
        console.log($scope.AllBlocks);
    }
    $scope.countingCounter = function(){
        $scope.counter = ($scope.startnumber - 1)/50;
    }

    $scope.$watch('looper', function() {
        if($scope.endnumber < parseInt($scope.endloop)){
            if($scope.keyLooper == true){
                $scope.getData();
                console.log($scope.looper);
            }
        }
    });

    $scope.buttonAction = function(){
        if($scope.offbutton == true){
            $scope.offbutton = false;
        }else{
            $scope.offbutton = true;
        }
    }

    $scope.evalTime = function(blockData){       
        for (i = 0; i < blockData.length; i++) { 
            if (i != 0){
    
                if (blockData[i].height == blockData[i-1].height){
                    console.log("duplicate block", blockData[i].height);
                }
                var epoc1 = blockData[i].timestamp;
                var epoc2 = blockData[i-1].timestamp;

                var nowtime1 = new Date(0)
                var nowtime2 = new Date(0)

                nowtime1.setUTCSeconds(epoc1);
                nowtime2.setUTCSeconds(epoc2);
                
                //var d1 = Date.parse(nowtime1);
                //var d2 = Date.parse(nowtime2);
    
                var diff = Math.abs(nowtime1.getTime() - nowtime2.getTime());
                var json_file = new Object();
                json_file.numberBlock = blockData[i].height;
                json_file.timeFromLast = $scope.returnSeconds(diff);
                $scope.DiffTime.push(json_file);
    
            }
        }
        console.log($scope.DiffTime);
    
    };
    
    //
    // Return seconds from miliseconds
    //
    $scope.returnSeconds = function(time){
        return time/1000;
    }

}]);