from flask import Flask, render_template, request, redirect

app = Flask(__name__)


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


lista = [
        Jogo('Super Mario', 'Plataforma', 'SNES'),
        Jogo('Pokemon Gold', 'RPG', 'GameBoy'),
        Jogo('Mortal Kombat', 'Luta', 'SNES'),
    ]


@app.route('/')
def index():
    return render_template('lista.html', titulo="Jogos", header="Jogoteca", jogos=lista)


@app.route('/novo')
def novo():
    return render_template('novo.html', titulo="Jogos", header="Novo Jovo")


@app.route('/criar', methods=['POST', ])
def criar():
    lista.append(Jogo(request.form['nome'], request.form['categoria'], request.form['console']))
    return redirect('/')


app.run(host='0.0.0.0', port=8080, debug=True)
