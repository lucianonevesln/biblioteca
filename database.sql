-- Criando um banco de dados
create database biblioteca;

-- Colocando o banco de dados em uso
use biblioteca;

-- Criando tabelas
create table if not exists autores (
	id int not null auto_increment,
    nome varchar(50),
    key(id)
);

create table if not exists livros (
	id int not null auto_increment,
    id_autores int not null,
    nome varchar(100),
    key(id),
    foreign key (id_autores) references autores(id)
);

-- inserindo valores nas tabelas para teste
insert into autores (nome) values ('Fiodor Dostoievski');
insert into autores (nome) values ('Paulo Coelho');

insert into livros (nome, id_autores) values ('Crime e Castigo', 1);
insert into livros (nome, id_autores) values ('Diario de um Mago', 2);
insert into livros (nome, id_autores) values ('Guerra e Paz', 1);
insert into livros (nome, id_autores) values ('O Alquimista', 2);

-- consultando valores na tabela
select * from autores;
select * from livros;

select
	a.nome nome_autor,
    l.nome nome_livro
from
	autores as a
inner join livros as l on l.id_autores = a.id;

-- Excluir registro da tabela
delete from livros where id = 9;
delete from livros where id = 10;
delete from autores where id = 7;

-- Excluir tabelas criadas
drop table livros;
drop table autores;