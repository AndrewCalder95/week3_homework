from flask import render_template, request, redirect
from app import app
from models.player import Player
from models.game import Game
import random


@app.route('/<player1>/<player2>/')
def game(player1, player2):
    player1 = Player("Player 1", player1)
    player2 = Player("Player 2", player2)
    game = Game()
    
    winner = game.play_game(player1, player2)
    

    return render_template("index.html", player_1=player1, player_2=player2, winner=winner)

@app.route('/rules')
def rules():
    return render_template("welcome.html")

@app.route('/')
def home():
    return render_template("homepage.html")

@app.route('/visualgame', methods=['POST', 'GET'])
def game_version2():
    if request.method == 'POST':
        first_player = request.form["player1"]
        second_player = request.form["player2"]
        player1 = Player("Player 1", first_player)
        player2 = Player("Player 2", second_player)

        game = Game()
        
        winner = game.play_game(player1, player2)

        return render_template('index.html', player_1=player1, player_2=player2, winner=winner)
    else:
        return render_template('home.html')


@app.route('/play', methods=['POST', 'GET'])
def computer_game():
    if request.method == 'POST':
        player_name = request.form["player_check"]
        player_choice = request.form["move_check"]
        player = Player(player_name, player_choice)
        bot = Player('Bot', random.choice(["rock", "paper", "scissors"]))
        game = Game()
        winner = game.play_game(player, bot)

        return render_template("index.html", player_1=player, player_2 = bot , winner=winner)
    else:
        return render_template('play.html')