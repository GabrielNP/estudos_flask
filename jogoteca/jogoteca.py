from flask import Flask, render_template


app = Flask(__name__)

class Jogo:

    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


@app.route('/inicio')
def ola():
    # lista = ['Tetris', 'Super Mario', 'Pokemon Gold']
    jogo1 = Jogo('Super Mario', 'Ação', 'SNES')
    jogo2 = Jogo('Pokemon Gold', 'RPG', 'Gameboy')
    jogo3 = Jogo('Tetris', 'Lógica', 'Celular')
    lista = [jogo1, jogo2, jogo3]
    return render_template('lista.html', titulo='Jogos', jogos=lista)

@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')
app.run(host='0.0.0.0', port=8080)

