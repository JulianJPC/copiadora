copiadoraApp.controller('copyController',['$scope', '$location', 'copyService',
function($scope, $location, copyService){

    $scope.error = false;

    $scope.numberblocks = "";
    $scope.startnumber = 1;
    $scope.endnumber = 51;
    $scope.counter = 0;

    $scope.looper = 0;
    $scope.keyLooper = false;
    $scope.endloop = 527639;

    $scope.offbutton = false;

    $scope.AllBlocks = [];
    $scope.DiffTime = [];

    $scope.getData= function(){

            $scope.buttonAction();

            if($scope.startnumber == null){                   //If there is not initial numbers it will start from 1 and 51
                $scope.startnumber = 1;
                $scope.endnumber = 51;
            }else{
                $scope.startnumber = parseInt($scope.counter) * 50 + 1; //Else it will take the conunter to place the start and end number
                $scope.endnumber = parseInt($scope.counter) * 50 + 51;
            };

            if($scope.endnumber > parseInt($scope.endloop)){  //If the endnumber is bigger than the endloop the end number will take the value of endloop
                $scope.endnumber = parseInt($scope.endloop);
            }

            for(x = $scope.startnumber; x < $scope.endnumber; x++){ //Makes the number array to query the api
                if(x != $scope.endnumber - 1){
                    $scope.numberblocks = $scope.numberblocks + x.toString() + ",";
                }else{
                    $scope.numberblocks = $scope.numberblocks.toString() + x.toString()
                }
            };
            var apiPath = "https://chain.api.btc.com/v3/block/";

            var apiblocks = apiPath + $scope.numberblocks;

            $scope.counter = parseInt($scope.counter) + 1; //counter will set the next 50 numbers

            copyService.getajax(apiblocks, function(response){
                if(response == null){
                    $scope.counter = parseInt($scope.counter) - 1; //If fail it will make counter as the beginig
                    $scope.error = true;
                    setTimeout(function() { // It will reactivate the query button and the numberblocks
                        $scope.numberblocks = "";
                        $scope.buttonAction();
                        $scope.$digest();
                    }, 20000);
                }else{
                    $scope.numberblocks = ""; //Restart the button in case of success and push the block info in to the array
                    $scope.buttonAction();
                    for(x = 0; x < response.data.length; x++){
                        $scope.AllBlocks.push(response.data[x]);
                    }

                    if($scope.endnumber != parseInt($scope.endloop)){ //In case of not ending the loop will continue
                        setTimeout(function() {
                            $scope.looper = $scope.looper + 1;
                            $scope.$digest();
                        }, 2000);
                    }        
                }
                
            });       
    };

    $scope.watchblocks = function(){ //See array of info of blocks
        console.log($scope.AllBlocks);
    }
    $scope.countingCounter = function(){ //Counter calculator
        $scope.startnumber = parseInt($scope.counter) * 50 + 1;
        $scope.endnumber = 50 + 50 * parseInt($scope.counter) + 1;
    }

    $scope.$watch('looper', function() {                    //Loops get data in change of looper var
        if($scope.endnumber < parseInt($scope.endloop)){
            if($scope.keyLooper == true){
                $scope.getData();
                console.log($scope.looper);
            }
        }
    });

    $scope.buttonAction = function(){       //Chages button avaliabity
        if($scope.offbutton == true){
            $scope.offbutton = false;
        }else{
            $scope.offbutton = true;
        }
    }

    $scope.evalTime = function(blockData){       //Gets time between blocks and puts it to an array
        for (i = 0; i < blockData.length; i++) { 
            if (i != 0){//To not compare block array [0] and [-1]
    
                if (blockData[i].height == blockData[i-1].height){ //In case of error
                    console.log("duplicate block", blockData[i].height);
                }
                var epoc1 = blockData[i].timestamp;     //Takes out the timestamp var out of the blocks
                var epoc2 = blockData[i-1].timestamp;

                var nowtime1 = new Date(0)              //New variables of date
                var nowtime2 = new Date(0)

                nowtime1.setUTCSeconds(epoc1);          //Gets the epoc to UTC into the new variables
                nowtime2.setUTCSeconds(epoc2);
                
                var diff = Math.abs(nowtime1.getTime() - nowtime2.getTime()); //time between blocks
                var json_file = new Object();                                 //Dummy object
                json_file.numberBlock = blockData[i].height;                  //Gets the block height to the object
                json_file.timeFromLast = $scope.returnSeconds(diff);          //Gets the time between blocks in seconds
                $scope.DiffTime.push(json_file);                              //Makes the bigger time
    
            }
        }
        console.log($scope.DiffTime);
    
    };
    
    $scope.returnSeconds = function(time){ // Return seconds from miliseconds
        return time/1000;
    }

}]);