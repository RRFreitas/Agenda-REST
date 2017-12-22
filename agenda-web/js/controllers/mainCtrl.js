app.controller("mainCtrl", function ($scope, contatoService, operadoraService) {

    $scope.contatos = []
    $scope.operadoras = []

    var carregarOperadoras = function() {
        operadoraService.getOperadoras().then(function(data) {
            $scope.operadoras = data.data;
        })
    }

    var carregarContatos = function() {
        contatoService.getContatos().then(function(data) {
            $scope.contatos = data.data;
        });
    };

    $scope.addContato = function(contato) {
        var auxContato = {'nome' : contato.nome, 'telefone' : contato.telefone, 'operadora_id' : contato.operadora_id};
        contatoService.addContato(auxContato).then(function(data) {
            delete $scope.contato;
            carregarContatos();
        });
    };

    carregarOperadoras();
    carregarContatos();

    $scope.apagarContatos = function (contatos) {
        var selecionados = contatos.filter(function (contato) {
            if (contato.selecionado) return contato;
        });
        
        for(selecionado of selecionados) {
            contatoService.delContato(selecionado.id).then(function(data) {
                carregarContatos();
            });
        };
    };

    $scope.isContatoSelecionado = function (contatos) {
        return contatos.some(function (contato) {
            return contato.selecionado;
        });
    }
});