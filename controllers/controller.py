from crypt import methods
from operator import methodcaller
from unittest import result
from app import app
from flask import render_template, request, redirect
from models.game_func import play_game
from models.game import Game
from models.player import Player

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/rock/scissors')
def rock_wins():
    return "Player One wins! Rock beats scissors!"

@app.route('/rock/paper')
def rock_loses():
    return "Player Two wins! Paper beats rock!"

@app.route('/rock/rock')
def rock_draw():
    return "It's a draw!"

@app.route('/scissors/paper')
def scissors_win():
    return "Player One wins! Scissors beats paper!"

@app.route('/scissors/rock')
def scissors_lose():
    return "Player Two wins! Rock beats scissors!"

@app.route('/scissors/scissors')
def scissors_draw():
    return "It's a draw!"

@app.route('/paper/rock')
def paper_wins():
    return "Player One wins! Paper beats rock!"

@app.route('/paper/scissors')
def paper_loses():
    return "Player Two wins! Scissors beats paper!"

@app.route('/paper/paper')
def paper_draws():
    return "It's a draw!"

@app.route('/', methods=['POST'])
def play_round():
    p1_choice = request.form['player1-choice']
    p2_choice = request.form['player2-choice']
    return render_template('base.html', play_round=play_game(p1_choice, p2_choice))

@app.route('/rules')
def index1():
    return render_template('index.html')
