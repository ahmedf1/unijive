// Define the `phonecatApp` module
var classesApp = angular.module('classesApp', []);

// Define the `PhoneListController` controller on the `phonecatApp` module
classesApp.controller('ClassListController', function ClassListController($scope) {
                       $scope.classes = [
                                        {
                                        name: 'Calculus II, Jacobvits',
                                        snippet: 'Did anyone get the answer to 3 on the hw?',
                                        src: 'icons_/unopened_muted_chat_icon.PNG',
                                        chat_status: 'unopened',
                                        button_text:'Unmute'
                                        }, {
                                        name: 'Physics III, Mugglin',
                                        snippet: 'Wtf is going on in class',
                                        src: 'icons_/opened_chat_icon.PNG',
                                        chat_status: 'opened',
                                        button_text:'Mute'
                                        }, {
                                        name: 'Chemistry, Santos',
                                        snippet: "Can someone send the notes for today's class. I cudnt make it",
                                        src: 'icons_/unopened_chat_icon.PNG',
                                        chat_status: 'unopened',
                                        button_text:'Mute'
                                        
                                        }
                                        ];
                       });

/*
phonecatApp.controller('PhoneListController', function PhoneListController($scope, $http){
                       $http.get("testingsomephp.php").then(function(response){
                                        $scope.phones = response.data.records;
                                                            });
                       });
*/
