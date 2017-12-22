CREATE TABLE agenda.operadora(
	id int primary key auto_increment,
	nome varchar(15) not null,
    codigo int not null,
    categoria varchar(5)
);

CREATE TABLE agenda.contato(
	id int primary key auto_increment,
    nome varchar(30) not null,
    telefone varchar(15) not null,
    operadora_id int not null,
    foreign key(operadora_id) references agenda.operadora(id)
);