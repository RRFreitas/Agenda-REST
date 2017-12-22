angular.module("app").factory("contatoService", function($http, config) {

    var _path = config.baseUrl() + "/contatos";

    var _getContatos = function() {
        return $http.get(_path);
    }

    var _addContato = function(contato) {
        return $http.post(_path, contato)
    }

    var _delContato = function(contato) {
        return $http.delete(_path + "/" + contato)
    }

    return {
        getContatos : _getContatos,
        addContato : _addContato,
        delContato : _delContato
    }
});