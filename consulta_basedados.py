# Baixando as ferramentas necessarias
from flask import Flask, request, render_template, jsonify
from flaskext.mysql import MySQL
import config


# Acionando ferramenta de contato com o banco de dados
mysql = MySQL()


# Ferramenta que vai permitir acionar o servidor 
app = Flask(__name__)


# Script para conexao com o banco de dados
app.config['MYSQL_DATABASE_DB'] = config.DB
app.config['MYSQL_DATABASE_USER'] = config.USER
app.config['MYSQL_DATABASE_PASSWORD'] = config.PASS
app.config['MYSQL_DATABASE_HOST'] = config.DB_URL


# Iniciando a conexao com o banco de dados
mysql.init_app(app)


# Retorna todos os nomes armazenados em banco de dados
def ver_autores2():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select * from biblioteca.autores')
    autores = cursor.fetchall()
    conn.commit()
    return jsonify(autores)
    cursor.close()
    conn.close()


# Retorna todos os nomes armazenados em banco de dados
def ver_livros2():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select id, nome from biblioteca.livros')
    nomes = cursor.fetchall()
    conn.commit()
    return jsonify(nomes)
    cursor.close()
    conn.close()


# Retorna todos os nomes armazenados em banco de dados
def ver_autores_livros2():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('select a.nome nome_autor, l.nome nome_livro from biblioteca.autores as a inner join biblioteca.livros as l on l.id_autores = a.id;')
    nomes = cursor.fetchall()
    conn.commit()
    return jsonify(nomes)
    cursor.close()
    conn.close()