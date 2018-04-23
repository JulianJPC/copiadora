var copiadoraApp = angular.module('copiadoraApp', ['ngRoute']);

copiadoraApp.config(function ($routeProvider, $locationProvider) {
	$routeProvider.when("/", {
		templateUrl: "html/copystart.html",
		controller: 'copyController',
	});
	$locationProvider.html5Mode(true);

});