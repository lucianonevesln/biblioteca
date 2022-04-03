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


# Inicia a conexao com o banco de dados
mysql.init_app(app)


# funcao que cadastra autor em banco de dados
def cad_autor3(autor):
    if autor:
         conn = mysql.connect()
         cursor = conn.cursor()
         cursor.execute(
             'insert into autores (nome) values (%s);', 
             (autor)
             )
         conn.commit()
         cursor.close()
         conn.close()
         return render_template('cadastra_autor.html')


# funcao que cadastra nome do livro e associa a autor em banco de dados
def cad_livro3(livro, id_autor_livro):
    if livro:
         conn = mysql.connect()
         cursor = conn.cursor()
         cursor.execute(
             'insert into livros (nome, id_autores) values (%s, %s);', 
             (livro, id_autor_livro)
             )
         conn.commit()
         cursor.close()
         conn.close()
         return render_template('cadastra_livro.html')