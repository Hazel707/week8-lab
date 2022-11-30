
import random
from logic import get_winner, check_move, isfull, make_empty_board, show_board
from typing import Tuple
import pandas as pd
import numpy as np
filename="TicTacToe.csv"
player_file="player_record.csv"

games=pd.DataFrame(columns=[
    "ID",
    "Player1",
    "Player2",
    "Winner",
    "Type",
])
players=pd.DataFrame(columns=[
    "ID",
    "Name",
    "Score",
    "Rank",
])

col_names=[
    "ID",
    "Player1",
    "Player2",
    "Winner",
    "Type", #Type: 1=human-bot, 2=human-human
]
col_p=[
    "ID",
    "Name",
    "Score",
    "Rank",
]
game_data=pd.read_csv(filename,names=col_names,header=None)
player_data=pd.read_csv(player_file)
def add_game(id,player1,player2,winner,type):
    games.loc[len(game_data)]={
        "ID":id,
        "Player1":player1,
        "Player2":player2,
        "Winner":winner,
        "Type":type,
    }
def add_player(name,score):
    players.loc[len(player_data)]={
        "ID":len(player_data)+1,
        "Name":name,
        "Score":score,
        "Rank":None
    }
def update_score(name):
    player_data.loc[player_data.Name==name,"Score"]+=1
type=1    

class Game:
    def __init__(self) :
        self.board=make_empty_board()
        self.winner=None #get_winner(self._board)
        self.user_turn=True
        self.winner_name=None
        
    def get_winner_name(self):
        return self.winner_name
    def get_winner(self):
        return self.winner


    def get_board(self):
        return self.board

    def set_move(self,x,y,value):
        self.board[x][y]=value

    
    def _get_empty_space(self):
        space = []

        for i in range(3):
            for j in range(3):
                if self.board[i][j] is None:
                    space.append((i, j))

        return space

    def bot_random_step(self) -> Tuple:
        _empty_space = self._get_empty_space()

        return _empty_space[random.randint(0, len(_empty_space) - 1)]


    def run(self):
        show_board(self.board)
        player1_name=input("Please enter your name:")
        
        while self.winner is None:
            if self.user_turn:
                
                print("It's your turn!")
                row=int(input("pick a row: "))
                while (row<0 or row>2):
                    row=int(input("out of boundary, please pick a numer(0<= x <3): "))
                col=int(input("pick a col: "))
                while (col<0 or col>2):
                    col=int(input("out of boundary, please pick a numer(0<= y <3): "))
                
                while check_move(self.board,row,col): #keep input until input move is vailed
                    print("this position was taken, please choose a new one")
                    row=int(input("pick a row: "))
                    while (row<0 or row>2):
                        row=int(input("out of boundary, please pick a numer(0<= x <3): "))

                    col=int(input("pick a col: "))
                    while (col<0 or col>2):
                        col=int(input("out of boundary, please pick a numer(0<= y <3): "))
                self.set_move(row,col,"X")

                
                
            else:
                print("It's bot's turn!")
                bot_step = self.bot_random_step()

                print("Bot takes " + str(bot_step))

                self.board[bot_step[0]][bot_step[1]] = "O"

                #make_move(self._board,current_player)

            show_board(self.board)
            self.winner=get_winner(self.board)
            
            if self.winner=="X":
                self.winner_name=player1_name
                print("Congratulation! Yor're winner!")
            elif self.winner=="O":
                self.winner_name="Bot"
                print("You failed")
            else:
                if isfull(self.board):
                    print("The grid is full, draw!")
                    self.winner="Draw"
                    self.winner_name="draw"

            self.user_turn=not self.user_turn
        

        

