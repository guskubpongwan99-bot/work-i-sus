
import tkinter as tk #pip install tkinter
from tkinter import messagebox
 
class TicTacToe:
    def __init__(self):
 
        # Custom styling 
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.root.configure(bg="#2C2F33")  
 
        self.current_player = "X" #first to start is X
        self.board = [""] * 9
        self.buttons = []
 
        self.create_widgets()
        self.root.mainloop()
 
    def create_widgets(self):
        """Create the game grid and reset button."""
 
        # create the title 
        # the title is on one row and 3 columns 
        title = tk.Label(self.root, text="Tic-Tac-Toe",
                         font=("Arial", 18, "bold"), fg="white", bg="#2C2F33")
        title.grid(row=0, column=0, columnspan=3, pady=10)
 
        # create the 9 buttons for playing 
        # when u click on a button, it will call the function on_click
        for i in range(9):
            btn = tk.Button(self.root, text="", font=("Arial", 20, "bold"), width=6, height=2,
                            fg="#FFFFFF", bg="#23272A", activebackground="#99AAB5", 
                            relief="ridge", command=lambda i=i: self.on_click(i))
            btn.grid(row=(i // 3) + 1, column=i % 3, padx=5, pady=5)
            self.buttons.append(btn)
 
        self.reset_btn = tk.Button(self.root, text="Reset", font=("Arial", 14, "bold"), 
                                   fg="#FFFFFF", bg="#7289DA", activebackground="#99AAB5",
                                   command=self.reset_board)
        self.reset_btn.grid(row=4, column=0, columnspan=3, pady=10)
 
    def on_click(self, index):
        """Handles button clicks, updates board, and checks for a winner."""
        if self.board[index] == "" and not self.check_winner(): #if board is empty still, and if no one won yet
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player, state="disabled")
 
            winner = self.check_winner()
            if winner:
                self.show_winner(winner)
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
 
    def check_winner(self):
        """Checks if there's a winner or a draw."""
        win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                          (0, 3, 6), (1, 4, 7), (2, 5, 8),
                          (0, 4, 8), (2, 4, 6)] # win conditions here are hard coded 
        
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] and self.board[a] != "": #if the three of them are alike and not empty then someone won
                return self.board[a]
        
        return "Draw" if "" not in self.board else None #if its full, and no one won, its a draw, otherwise, game continue (return none) 
 
    def show_winner(self, winner):
        """Displays the winner and resets the game."""
        if winner == "Draw":
            messagebox.showinfo("Tic-Tac-Toe", "Draw!, woopsie daisie")
        else:
            messagebox.showinfo("Tic-Tac-Toe", f"{winner} wins!")
        self.reset_board()
 
    def reset_board(self):
        """Resets the game board for a new match."""
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="", state="normal")
 
if __name__ == "__main__":
    TicTacToe()