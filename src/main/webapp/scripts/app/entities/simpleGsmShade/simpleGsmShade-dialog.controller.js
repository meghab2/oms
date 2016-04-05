'use strict';

angular.module('omsApp').controller('SimpleGsmShadeDialogController',
    ['$scope', '$stateParams', '$uibModalInstance', 'entity', 'SimpleGsmShade', 'Mill', 'Price',
        function($scope, $stateParams, $uibModalInstance, entity, SimpleGsmShade, Mill, Price) {

        $scope.simpleGsmShade = entity;
        $scope.findMill = function() {
            Mill.query(function(result) {
                $scope.mills = result;
                var mill;
                for(mill in $scope.mills) {
                    if($scope.mills[mill].id == $stateParams['id']) {
                        $scope.simpleGsmShade.mill = $scope.mills[mill];
                    }
                }
            });
        }
        $scope.findMill();
        
        $scope.mills = Mill.query();
        $scope.prices = Price.query();
        $scope.load = function(id) {
            SimpleGsmShade.get({id : id}, function(result) {
                $scope.simpleGsmShade = result;
            });
        };

        var onSaveSuccess = function (result) {
            $scope.$emit('omsApp:simpleGsmShadeUpdate', result);
            $uibModalInstance.close(result);
            $scope.isSaving = false;
        };

        var onSaveError = function (result) {
            $scope.isSaving = false;
        };

        $scope.save = function () {
            $scope.isSaving = true;
            if ($scope.simpleGsmShade.id != null) {
                SimpleGsmShade.update($scope.simpleGsmShade, onSaveSuccess, onSaveError);
            } else {
                SimpleGsmShade.save($scope.simpleGsmShade, onSaveSuccess, onSaveError);
            }
        };

        $scope.clear = function() {
            $uibModalInstance.dismiss('cancel');
        };
}]);
