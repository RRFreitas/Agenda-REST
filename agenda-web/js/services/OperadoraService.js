angular.module("app").factory("operadoraService", function($http, config) {

    var _path = config.baseUrl() + "/operadoras";

    var _getOperadoras = function() {
        return $http.get(_path);
    }

    return {
        getOperadoras : _getOperadoras
    }
});