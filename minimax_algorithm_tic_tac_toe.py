import tkinter as tk

human = "X"
ai = "O"
emp = " "

root = tk.Tk()
root.title("AI-TTT")

buttons = [[None, None, None], [None, None, None], [None, None, None]]

def winner_chk(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):
            return True
    for j in range(3):
        if all(board[i][j] == player for i in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def draw_chk(board):
    return all(board[i][j] != emp for i in range(3) for j in range(3))

def ai_mov():
    best_score = -float("inf")
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == emp:
                board[i][j] = ai
                score = minimax(board, 0, False)
                board[i][j] = emp
                if score > best_score:
                    best_score = score
                    move = (i, j)
    if move:
        i, j = move
        buttons[i][j].config(text=ai, state=tk.DISABLED,foreground="black")
        board[i][j] = ai
        if winner_chk(board, ai):
            result_label.config(text="AI WINS!")
        elif draw_chk(board):
            result_label.config(text="DRAW!")

def minimax(board, depth, is_maximizing):
    winner = human if is_maximizing else ai

    if winner_chk(board, human):
        return -1
    elif winner_chk(board, ai):
        return 1
    elif draw_chk(board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == emp:
                    board[i][j] = ai
                    score = minimax(board, depth + 1, False)
                    board[i][j] = emp
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == emp:
                    board[i][j] = human
                    score = minimax(board, depth + 1, True)
                    board[i][j] = emp
                    best_score = min(score, best_score)
        return best_score

def click_hdl(row, col):
    if board[row][col] == emp:
        buttons[row][col].config(text=human, state=tk.DISABLED,foreground="black")
        board[row][col] = human
        if winner_chk(board, human):
            result_label.config(text="YOU WIN!")
        elif not draw_chk(board):
            ai_mov()
        elif draw_chk(board):
            result_label.config(text="DRAW!")

for row in range(3):
    for col in range(3):
        buttons[row][col] = tk.Button(root, text=emp, width=10, height=4, command=lambda row=row, col=col: click_hdl(row, col),bg="black")
        buttons[row][col].grid(row=row, column=col)

result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.grid(row=3, columnspan=3)

board = [[emp for _ in range(3)] for _ in range(3)]

root.mainloop()
