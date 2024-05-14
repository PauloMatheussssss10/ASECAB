from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('arquivo.html')

@app.route('/cadastro', methods=['POST'])
def cadastrar():
    nome = request.form['nome']
    endereco = request.form['endereco']
    telefone = request.form['telefone']
    email = request.form['email']
    login = request.form['login']
    senha = request.form['senha']

    # Salvar os dados em um arquivo CSV
    # Obtenha o caminho absoluto para o arquivo cadastros.csv
    caminho_csv = os.path.join(os.path.dirname(__file__), 'cadastros.csv')

    # Salvar os dados em um arquivo CSV
    with open(caminho_csv, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nome, endereco, telefone, email, login, senha])
        return 'Cadastro realizado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
