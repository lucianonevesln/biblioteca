# Baixando as ferramentas necessarias
from flask import Flask, request, render_template, jsonify
from consulta_basedados import *
from cadastro_basedados import *


# Ferramenta que vai permitir acionar o servidor 
app = Flask(__name__)


# Rota para renderizar o front-end
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


# Rota para renderizar pagina de cadastro de autor
@app.route('/cadastra_autor', methods=['GET'])
def cad_autor1():
    return render_template('cadastra_autor.html')


# Rota que insere autor em banco de dados
@app.route('/cadastrar_autor', methods=['POST'])
def cad_autor2():
    autor = request.form['id_autor']
    return cad_autor3(autor)


# Rota para renderizar pagina de cadastro de livro
@app.route('/cadastra_livro', methods=['GET'])
def cad_livro1():
    return render_template('cadastra_livro.html')


# Rota que insere livro em banco de dados
@app.route('/cadastrar_livro', methods=['POST'])
def cad_livro2():
    livro = request.form['id_livro']
    id_autor_livro = int(request.form['id_autor_livro'])
    return cad_livro3(livro, id_autor_livro)


# Rota que retorna todos os autores armazenados em banco de dados
@app.route('/autores', methods=['GET'])
def ver_autores1():
    return ver_autores2()


# Rota que retorna todos os livros armazenados em banco de dados
@app.route('/livros', methods=['GET'])
def ver_livros1():
    return ver_livros2()


# Rot que retorna todos os autores e livros armazenados em banco de dados
@app.route('/autores-livros', methods=['GET'])
def ver_autores_livros1():
    return ver_autores_livros2()


# Scrip que define a localidade e executa o servidor
if __name__ == '__main__':
    app.run(host = 'localhost', port = 5002, debug = True)