import random
import os
import time

class ticTacToe:
    def __init__(self, mode):
        self.reset()
        self.mode = mode

    def print_board(self):
        print("")
        print(" " + self.board[0][0] + " | " + self.board[0][1] + " | " +  self.board[0][2])
        print("-----------")
        print(" " + self.board[1][0] + " | " + self.board[1][1] + " | " +  self.board[1][2])
        print("-----------")
        print(" " + self.board[2][0] + " | " + self.board[2][1] + " | " +  self.board[2][2])
    
    def reset(self):
        self.board = [[" "," "," "], [" "," "," "], [" "," "," "]]
        self.done = ""

    def check_win_or_draw(self):
        dict_win = {}

        for i in ["X", "O"]:
            #Horizontais
            dict_win[i] = (self.board[0][0] == self.board[0][1] == self.board[0][2] == i)
            dict_win[i] = (self.board[1][0] == self.board[1][1] == self.board[1][2] == i) or dict_win[i]
            dict_win[i] = (self.board[2][0] == self.board[2][1] == self.board[2][2] == i) or dict_win[i]
            #Verticais
            dict_win[i] = (self.board[0][0] == self.board[1][0] == self.board[2][0] == i) or dict_win[i]
            dict_win[i] = (self.board[0][1] == self.board[1][1] == self.board[2][1] == i) or dict_win[i]
            dict_win[i] = (self.board[0][2] == self.board[1][2] == self.board[2][2] == i) or dict_win[i]
            # Diagonais
            dict_win[i] = (self.board[0][0] == self.board[1][1] == self.board[2][2] == i) or dict_win[i]
            dict_win[i] = (self.board[0][2] == self.board[1][1] == self.board[2][0] == i) or dict_win[i]
        
        if dict_win["X"]:
            self.done = "X"
            print("X wins")
            return
        elif dict_win["O"]:
            self.done = "O"
            print("O wins")
            return

        c = 0
        for i in range(3):
            for j in range(3): 
                if self.board[i][j] != " ":
                    c += 1

        if c == 9:
            self.done = "D"
            print("Draw")
            return


    def get_player_move(self, player):
        invalide_move = True

        while invalide_move:
            
            try:
                x = int(input(f"\nDigite a linha do seu próximo lance: "))
                y = int(input(f"\nDigite a coluna do seu próximo lance: "))
                
                if x < 0 or y < 0 or x > 2 or y > 2:
                    print("Coordenadas Inválidas") 
                    continue

                elif self.board[x][y] != " ":
                    print("Posição já preenchida")
                    continue
                
            except Exception as e:
                print(e)
                continue
        
            invalide_move = False
        if player == "X":
            self.board[x][y] = "X"
        else:
            self.board[x][y] = "O"

    board = [[" "," "," "], [" "," "," "], [" "," "," "]]
    def simulate(self, board):
        dict_win = {}

        for i in ["X", "O"]:
            #Horizontais
            dict_win[i] = (board[0][0] == board[0][1] == board[0][2] == i)
            dict_win[i] = (board[1][0] == board[1][1] == board[1][2] == i) or dict_win[i]
            dict_win[i] = (board[2][0] == board[2][1] == board[2][2] == i) or dict_win[i]
            #Verticais
            dict_win[i] = (board[0][0] == board[1][0] == board[2][0] == i) or dict_win[i]
            dict_win[i] = (board[0][1] == board[1][1] == board[2][1] == i) or dict_win[i]
            dict_win[i] = (board[0][2] == board[1][2] == board[2][2] == i) or dict_win[i]
            # Diagonais
            dict_win[i] = (board[0][0] == board[1][1] == board[2][2] == i) or dict_win[i]
            dict_win[i] = (board[0][2] == board[1][1] == board[2][0] == i) or dict_win[i]
        
        if dict_win["X"]:
            return -10
        elif dict_win["O"]:
            return 10

        c = 0
        for i in range(3):
            for j in range(3): 
                if board[i][j] != " ":
                    c += 1

        if c == 9:
            return 0
        
        else:
            return None

    def minimax(self, board, is_maximizing):
        # Verificar se o jogo já acabou
        score = self.simulate(board)
        if score is not None:
            return score
        # Jogada da Máquina
        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = "O"
                        score = self.minimax(board, False)
                        board[i][j] = " "
                        best_score = max(score, best_score)
            return best_score
        # Jogada Humana
        else:
            best_score = float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ' ':
                        board[i][j] = "X"
                        score = self.minimax(board, True)
                        board[i][j] = " "
                        best_score = min(score, best_score)
            return best_score
        
    def make_move(self):
        list_move = []
        best_val = -float('inf')
        best_move = None

        for i in range(3):
            for j in range(3):
                if self.board[i][j] == " ":
                    list_move.append((i,j))
        if len(list_move) > 0: 
            for i, j in list_move:
                self.board[i][j] = "O"
                move_val = self.minimax(self.board, False)
                if move_val > best_val:
                    best_val = move_val
                    best_move = (i, j)
                self.board[i][j] = " "
            i, j = best_move
            self.board[i][j] = "O"
            

mode = input("\n1: IA \n2: Multiplayer \nModo de Jogo:")
tic_tac_toe = ticTacToe(mode)
tic_tac_toe.print_board()
next = 0

while next == 0:
    os.system("clear")
    tic_tac_toe.print_board()
    while tic_tac_toe.done == "":
        tic_tac_toe.get_player_move("X")
        os.system("clear")
        tic_tac_toe.print_board()
        tic_tac_toe.check_win_or_draw()
        if tic_tac_toe.done != "":
            break
        if mode == "1":  # "IA" ou "Multiplayer"
            print("\nThinking")
            time.sleep(1.5)
            os.system("clear")
            tic_tac_toe.make_move()
            os.system("clear")
            tic_tac_toe.print_board()
            tic_tac_toe.check_win_or_draw()
        else:
            tic_tac_toe.get_player_move("O")
            os.system("clear")
            tic_tac_toe.print_board()
            tic_tac_toe.check_win_or_draw()

    answer = input("\nDigite 1 para sair do jogo ou qualquer tecla para continuar:")
    if answer == "1":
        next = 1
        print("\nBYEEEE!")
        break
    else:
        tic_tac_toe.reset()