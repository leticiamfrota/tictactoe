import tkinter as tk
from tkinter import messagebox

class ticTacToe:
    def __init__(self):
        # Configuração da Janela Principal
        self.window = tk.Tk()
        self.window.title("Jogo da Velha Com Alg. Minimax")
        
        # Atributos de lógica
        self.board = [[" "," "," "], [" "," "," "], [" "," "," "]]
        self.done = ""
        self.mode = None  # "IA" ou "Multiplayer"
        self.current_player = "X" # X começa sempre
        
        # Matriz para guardar os objetos dos botões
        self.buttons = [[None for _ in range(3)] for _ in range(3)]

        # Escolher um jogador ou dois
        self.show_menu()

    def show_menu(self):
        # Criamos um "Frame" (um contentor) para o menu
        self.menu_frame = tk.Frame(self.window)
        self.menu_frame.pack(pady=20)
        
        tk.Label(self.menu_frame, text="Escolha o Modo de Jogo:", font=("Arial", 14)).pack(pady=10)
        
        tk.Button(self.menu_frame, text="Contra a IA", width=20, 
                command=lambda: self.start_game("IA")).pack(pady=5)
        
        tk.Button(self.menu_frame, text="Dois Jogadores", width=20, 
                command=lambda: self.start_game("Multiplayer")).pack(pady=5)

    def start_game(self, chosen_mode):
        self.mode = chosen_mode
        self.menu_frame.destroy() # Remove o menu da tela
        self.create_widgets()     # Desenha o tabuleiro
    
    def create_widgets(self):
        # Criar os 9 botões usando um loop aninhado
        for i in range(3):
            for j in range(3):
                # O parâmetro 'command' usa lambda para passar a posição exata do clique
                self.buttons[i][j] = tk.Button(
                    self.window, 
                    text=" ", 
                    font=('Arial', 20, 'bold'), 
                    width=5, 
                    height=2,
                    command=lambda r=i, c=j: self.on_click(r, c)
                )
                # O grid organiza os botões em linhas e colunas
                self.buttons[i][j].grid(row=i, column=j)
        
        reset_btn = tk.Button(
        self.window, 
        text="Reiniciar Jogo", 
        font=('Arial', 12),
        command=self.reset_game
        )   
        reset_btn.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def check_win_gui(self):
        res = self.simulate(self.board)
        
        if res == 10:
            self.done = "O"
            if self.mode == "IA":
                messagebox.showinfo("Fim de Jogo", "A IA venceu!")
            else:
                messagebox.showinfo("Fim de Jogo", "Player 2 venceu!")
            self.reset_game()
        elif res == -10:
            self.done = "X"
            if self.mode == "IA":
                messagebox.showinfo("Fim de Jogo", "Você venceu!")
            else:
                messagebox.showinfo("Fim de Jogo", "Player 1 venceu!")
            self.reset_game()
        elif res == 0:
            self.done = "D"
            messagebox.showinfo("Fim de Jogo", "Empate!")
            self.reset_game()
        
        
    
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
        
        if best_move:
            r, c = best_move
            self.board[r][c] = "O"
            self.buttons[r][c].config(text="O", state="disabled")
            
            # Após a IA jogar, verifica se ela ganhou
            self.check_win_gui()
    
    def on_click(self, row, col):
        if self.board[row][col] != " " or self.done != "":
            return
        # Marca a jogada do jogador atual (pode ser X ou O no multiplayer)
        self.board[row][col] = self.current_player
        self.buttons[row][col].config(text=self.current_player)
        
        # Verifica se houve vitória
        self.check_win_gui()
        
        if self.done == "":
            if self.mode == "IA":
                # Modo IA: O humano é sempre X, a IA é sempre O
                self.make_move()
            else:
                # Modo Multiplayer: Troca o símbolo para a próxima jogada
                self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.done = ""
        self.current_player = "X"
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text=" ", state="normal")

    def back_to_menu(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].destroy()
        
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.done = ""
        self.show_menu()
    
if __name__ == "__main__":
    game = ticTacToe()
    game.window.mainloop() 