# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, other_player, make_move, check_move, get_winner, isfull
from logic import show_board
from game import Game
import pandas as pd
#import numpy as np
filename="TicTacToe.csv" #record game's data
player_file="player_record.csv" #record palyer's data
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
#player_data=pd.read_csv(player_file,names=col_p,header=None)
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

type=0

if __name__ == '__main__':
    ans=input("Do you want to play against the bot?(y or n): ").lower()
    winner_name=None
    if ans=='y':
        type=1
        game=Game()
        #player1_name=input("Please enter your name:")
        game.run()
        player1_name=game.get_winner_name()
        if game.get_winner()=="X":
            add_game(len(game_data),player1_name,"Bot",player1_name,type)
            games.to_csv(filename,mode='a',header=False)
            if player1_name not in player_data["Name"].tolist():
                add_player(player1_name,0)
            players.to_csv(player_file,mode='a',index=False,header=False)
            player_data=pd.read_csv(player_file)
            update_score(player1_name)
        else:
            add_game(len(game_data),player1_name,"Bot",game.get_winner_name(),type)
            games.to_csv(filename,mode='a',header=False)
        
        player_data['Rank']=player_data.Score.rank(method='dense',ascending=False)
        player_data.to_csv(player_file,index=False)
        print(games)
        print("---------------------------------------")
        print("Global rank: ")
        print(player_data.sort_values('Rank',ascending=True))
        
    else:
        type=2
        board = make_empty_board()
        winner = None
        turn=0 
        now=1 #Represents the current player that should be operating
        show_board(board)
        player1_name=input("Player 1, please enter your name:")
        player2_name=input("Player 2, please enter your name:")
        player1=input("Player 1 choose which one you want to be, X or O?").upper()
        while (player1 !="X" and player1!="O"):
            player1=input(("Please choose X or O")).upper()
        player2=other_player(player1)
        print("So player 2 you are letter "+player2)
        print("Player 1, you go first")
        row=int(input("pick a row: "))
        while (row<0 or row>2):
            row=int(input("out of boundary, please pick a numer(0<= x <3): "))

        col=int(input("pick a col: "))
        while (col<0 or col>2):
            col=int(input("out of boundary, please pick a numer(0<= y <3): "))
        board=make_move(board,player1,player2,now,row,col)
        turn+=1
        show_board(board)

        while winner == None: #make a turn
            if turn%2==0:
                now=1
            else:
                now=2
            print("TODO: take a turn!")
            # TODO: Input a move from the player.
            if now==1:
                print("Player 1 is your turn!")
            else:
                print("Player 2 is your turn!")

            row=int(input("pick a row: "))
            while (row<0 or row>2):
                row=int(input("out of boundary, please pick a numer(0<= x <3): "))

            col=int(input("pick a col: "))
            while (col<0 or col>2):
                col=int(input("out of boundary, please pick a numer(0<= y <3): "))

            while check_move(board,row,col): #keep input until input move is vailed
                print("this position was taken, please choose a new one")
                row=int(input("pick a row: "))
                while (row<0 or row>2):
                    row=int(input("out of boundary, please pick a numer(0<= x <3): "))

                col=int(input("pick a col: "))
                while (col<0 or col>2):
                    col=int(input("out of boundary, please pick a numer(0<= y <3): "))
                

            board=make_move(board,player1,player2,now,row,col)

            show_board(board)

            winner=get_winner(board)
            
            if winner==player1:
                print("Congratulation! ", player1_name ," is winner!")
                winner_name=player1_name
            elif winner==player2:
                print("Congratulation! ",player2_name," is winner!")
                winner_name=player2_name
            else:
                if isfull(board):
                    print("The grid is full, draw!")
                    winner="Draw"
                    winner_name="draw"
                #break

            # TODO: Update who's turn it is.
            turn+=1
        
        add_game(len(game_data),player1_name,player2_name,winner_name,type)
        games.to_csv(filename,mode='a',header=False)

        if player1_name not in player_data["Name"].tolist():
            add_player(player1_name,0)
        if player2_name not in player_data["Name"].tolist():
            add_player(player2_name,0)
        players.to_csv(player_file,mode='a',index=False,header=False)
        player_data=pd.read_csv(player_file)
        update_score(winner_name)

        """if winner_name==player1_name:
            if winner_name in player_data["Name"]:
                update_score(winner_name)
            else:
                add_player(winner_name,1)

            if player2_name not in player_data["Name"]:
                add_player(player2_name,0)
        else:
            if winner_name in player_data["Name"]:
                update_score(winner_name)
            else:
                add_player(winner_name,1)

            if player1_name not in player_data["Name"]:
                add_player(player1_name,0)"""

        
        #rank_data=pd.read_csv(filename,names=col_names,header=None)
        #rank=rank_data["Winner"].value_counts()
        #rank_data['Rank']=rank_data.groupby('Winner').rank()
        #rank=pd.value_counts(rank_data["Winner"])
        player_data['Rank']=player_data.Score.rank(method='dense',ascending=False)
        player_data.to_csv(player_file,index=False)
        print(games)
        print("---------------------------------------")
        print("Global rank: ")
        print(player_data.sort_values('Rank',ascending=True))
        #player_data.to_csv(player_file,index=False)

        '''if player1_name in rank:
            print(player1_name,", your current global rank is ",rank[player1_name])
        #rank1=rank[player1_name]
        else:
            print("Sorry ",player1_name,", you haven't won one so far")
        
        if player2_name in rank:
            print(player2_name,", your current global rank is ",rank[player2_name])
        else:
            print("Sorry ",player2_name,", you haven't won one so far")'''
        
    



        
     