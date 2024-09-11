import tkinter as tk
from tkinter import messagebox
import random

# List of words for the game
WORDS = ["PYTHON", "DEVELOPER", "COMPUTER", "PROGRAMMING", "HANGMAN"]

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        
        self.word = random.choice(WORDS)
        self.word_to_guess = list("_" * len(self.word))
        self.guesses = set()
        self.max_attempts = 6
        self.attempts_left = self.max_attempts
        
        self.create_widgets()
        
    def create_widgets(self):
        # Frame for word display
        self.word_frame = tk.Frame(self.master)
        self.word_frame.pack(pady=20)
        
        self.word_label = tk.Label(self.word_frame, text=" ".join(self.word_to_guess), font=("Helvetica", 24))
        self.word_label.pack()
        
        # Frame for guess input
        self.guess_frame = tk.Frame(self.master)
        self.guess_frame.pack(pady=20)
        
        self.guess_entry = tk.Entry(self.guess_frame, font=("Helvetica", 24), width=3)
        self.guess_entry.pack(side=tk.LEFT)
        
        self.guess_button = tk.Button(self.guess_frame, text="Guess", command=self.make_guess, font=("Helvetica", 24))
        self.guess_button.pack(side=tk.LEFT, padx=10)
        
        # Frame for attempts
        self.attempts_frame = tk.Frame(self.master)
        self.attempts_frame.pack(pady=20)
        
        self.attempts_label = tk.Label(self.attempts_frame, text=f"Attempts Left: {self.attempts_left}", font=("Helvetica", 24))
        self.attempts_label.pack()
        
    def make_guess(self):
        guess = self.guess_entry.get().upper()
        
        if not guess or len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Invalid Input", "Please enter a single letter.")
            return
        
        if guess in self.guesses:
            messagebox.showinfo("Already Guessed", "You have already guessed that letter.")
            return
        
        self.guesses.add(guess)
        
        if guess in self.word:
            for index, letter in enumerate(self.word):
                if letter == guess:
                    self.word_to_guess[index] = guess
            self.word_label.config(text=" ".join(self.word_to_guess))
            
            if "_" not in self.word_to_guess:
                self.game_over("Congratulations! You won!")
        else:
            self.attempts_left -= 1
            self.attempts_label.config(text=f"Attempts Left: {self.attempts_left}")
            
            if self.attempts_left == 0:
                self.game_over(f"Game Over! The word was '{self.word}'")
        
        self.guess_entry.delete(0, tk.END)
        
    def game_over(self, message):
        messagebox.showinfo("Game Over", message)
        self.master.quit()

def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
