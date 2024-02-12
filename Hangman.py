import tkinter as tk
import random

class HangmanApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Hangman Game")
        self.master.configure(bg="#008080")  # Set background color to teal

        self.word_list = []
        self.word = ""
        self.guessed_letters = []
        self.attempts = 6

        self.word_display = tk.StringVar()
        self.word_display.set(self.display_word())

        self.create_widgets()

    def choose_word(self):
        return random.choice(self.word_list)

    def display_word(self):
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        return display

    def check_guess(self):
        guess = self.guess_entry.get().lower()
        self.guess_entry.delete(0, tk.END)

        if guess in self.guessed_letters:
            self.message_var.set("You already guessed that letter.")
        elif guess in self.word:
            self.guessed_letters.append(guess)
            self.word_display.set(self.display_word())
        else:
            self.attempts -= 1
            self.message_var.set(f"Incorrect guess! You have {self.attempts} attempts left.")
            if self.attempts == 0:
                self.message_var.set("You've run out of attempts! Game over.")
                self.word_display.set(f"The word was: {self.word}")
                self.guess_button.config(state=tk.DISABLED)

        if "_" not in self.display_word():
            self.message_var.set("Congratulations! You've guessed the word.")
            self.guess_button.config(state=tk.DISABLED)

    def reset_game(self):
        self.word_list = []
        self.word = ""
        self.guessed_letters = []
        self.attempts = 6
        self.word_display.set("")
        self.word_entry.config(state=tk.NORMAL)
        self.word_submit_button.config(state=tk.NORMAL)
        self.guess_entry.config(state=tk.NORMAL)
        self.guess_button.config(state=tk.NORMAL)
        self.message_var.set("")

    def create_widgets(self):
        # Word Input
        self.word_input_label = tk.Label(self.master, text="Enter your word list (separated by spaces):", font=("Arial", 28, "bold"), fg="#000000", bg="#008080")  # Solid bright black
        self.word_input_label.grid(row=0, column=0, columnspan=3, sticky="n", padx=10, pady=(50, 10))

        self.word_entry = tk.Entry(self.master, font=("Arial", 28, "bold"), width=50, bg="#FFFFFF", fg="#000000")  # Bright white, Solid bright black
        self.word_entry.grid(row=1, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        self.word_submit_button = tk.Button(self.master, text="Submit", command=self.submit_word_list, font=("Arial", 28, "bold"), bg="#FFFFFF", fg="#000000", relief="raised", width=1, height=1)  # Bright white, Solid bright black
        self.word_submit_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Hangman Word Display
        self.word_label = tk.Label(self.master, textvariable=self.word_display, font=("Arial", 40, "bold"), fg="#000000", bg="#008080")  # Solid bright black
        self.word_label.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

        # Guess Input
        self.guess_label = tk.Label(self.master, text="Enter a letter:", font=("Arial", 28, "bold"), fg="#000000", bg="#008080")  # Solid bright black
        self.guess_label.grid(row=4, column=0, sticky="n", padx=10, pady=10)

        self.guess_entry = tk.Entry(self.master, bg="#FFFFFF", fg="#000000", font=("Arial", 28, "bold"), width=10)  # Bright white, Solid bright black
        self.guess_entry.grid(row=4, column=1, sticky="nsew", padx=10, pady=10)

        self.guess_button = tk.Button(self.master, text="Guess", command=self.check_guess, font=("Arial", 28, "bold"), bg="#FFFFFF", fg="#000000", relief="raised", width=1, height=1)  # Bright white, Solid bright black
        self.guess_button.grid(row=4, column=2, sticky="nsew", padx=10, pady=10)

        # Reset Button
        self.reset_button = tk.Button(self.master, text="Reset", command=self.reset_game, font=("Arial", 24, "bold"), bg="#FFFFFF", fg="#000000", relief="raised", width=1, height=1)  # Bright white, Solid bright black
        self.reset_button.grid(row=5, column=0, columnspan=3, padx=10, pady=10, sticky="nsew")

        # Message Label
        self.message_var = tk.StringVar()
        self.message_label = tk.Label(self.master, textvariable=self.message_var, font=("Arial", 28, "bold"), fg="#000000", bg="#008080")  # Solid bright black
        self.message_label.grid(row=6, column=0, columnspan=3, padx=10, pady=10)

        # Configure grid weights to allow resizing
        for i in range(7):
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(3):
            self.master.grid_columnconfigure(i, weight=1)
        # Adjust column weights to center the buttons
        self.master.grid_columnconfigure(0, weight=1)
        self.master.grid_columnconfigure(2, weight=1)

    def submit_word_list(self):
        self.word_list = self.word_entry.get().split()
        if not self.word_list:
            self.message_var.set("Please enter at least one word.")
        else:
            self.word_entry.config(state=tk.DISABLED)
            self.word_submit_button.config(state=tk.DISABLED)
            self.word = self.choose_word()
            self.word_display.set(self.display_word())

def main():
    root = tk.Tk()
    root.title("Hangman Game")
    root.configure(bg="#008080")  # Set background color to teal
    app = HangmanApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
