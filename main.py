from flask import Flask, render_template

app = Flask(__name__)


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


@app.route('/inicio')
def inicio():
    lista = [
        Jogo('Super Mario', 'Plataforma', 'SNES'),
        Jogo('Pokemon Gold', 'RPG', 'GameBoy'),
        Jogo('Mortal Kombat', 'Luta', 'SNES'),
    ]

    return render_template('lista.html', titulo="Jogos", header="Jogoteca", jogos=lista)


app.run(host='0.0.0.0', port=8080)
