import tkinter as tk
from tkinter import messagebox

def check_winner():
    """Verifica se há um vencedor ou empate."""
    for row in board:
        if row[0]['text'] == row[1]['text'] == row[2]['text'] != "":
            return row[0]['text']

    for col in range(3):
        if board[0][col]['text'] == board[1][col]['text'] == board[2][col]['text'] != "":
            return board[0][col]['text']

    if board[0][0]['text'] == board[1][1]['text'] == board[2][2]['text'] != "":
        return board[0][0]['text']

    if board[0][2]['text'] == board[1][1]['text'] == board[2][0]['text'] != "":
        return board[0][2]['text']

    if all(board[row][col]['text'] != "" for row in range(3) for col in range(3)):
        return "Empate"

    return None

def click(row, col):
    """Manipula o clique nos botões."""
    global current_player

    if board[row][col]['text'] == "":
        board[row][col]['text'] = current_player
        winner = check_winner()
        if winner:
            if winner == "Empate":
                messagebox.showinfo("Fim de Jogo", "O jogo terminou em empate!")
            else:
                messagebox.showinfo("Fim de Jogo", f"O jogador {winner} venceu!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"

        update_display()

def reset_game():
    """Reinicia o jogo."""
    global current_player
    current_player = "X"
    for row in range(3):
        for col in range(3):
            board[row][col]['text'] = ""
    update_display()

def update_display():
    """Atualiza a interface do usuário."""
    for row in range(3):
        for col in range(3):
            board[row][col].update()

def adjust_window(event):
    """Ajusta o tamanho dos botões com a janela."""
    width = root.winfo_width()
    height = root.winfo_height()

    button_size = min(width // 5, height // 5)
    for row in range(3):
        for col in range(3):
            board[row][col].config(width=button_size // 10, height=button_size // 30)

    reset_button.config(width=button_size // 10, height=button_size // 30)

# Configuração inicial do jogo
root = tk.Tk()
root.title("Jogo da Velha")
root.geometry("400x400")
root.bind("<Configure>", adjust_window)

current_player = "X"
board = [[None for _ in range(3)] for _ in range(3)]

# Criando o tabuleiro
for row in range(3):
    for col in range(3):
        button = tk.Button(root, text="", font=("Arial", 24), command=lambda r=row, c=col: click(r, c))
        button.grid(row=row, column=col, sticky="nsew")
        board[row][col] = button

# Botão de reinício
reset_button = tk.Button(root, text="Reiniciar", font=("Arial", 14), command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

# Configurando redimensionamento dinâmico
def configure_grid():
    for i in range(4):
        root.grid_rowconfigure(i, weight=1)
        root.grid_columnconfigure(i, weight=1)

configure_grid()
root.mainloop()
