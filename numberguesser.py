import random
import tkinter as tk

class NumberGuesser:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.num_guesses = 0

        self.root = tk.Tk()
        self.root.title("Number Guessing Game")

        self.label = tk.Label(self.root, text="Guess a number between 1 and 100")
        self.label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.grid(row=1, column=0, padx=10, pady=10)

        self.submit_button = tk.Button(self.root, text="Submit", command=self.check_guess)
        self.submit_button.grid(row=1, column=1, padx=10, pady=10)

        self.output = tk.Text(self.root, height=2, state="disabled")
        self.output.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        # Bind the Enter key to the check_guess function
        self.root.bind('<Return>', self.check_guess)

    def check_guess(self, event=None):
        guess = int(self.entry.get())
        self.num_guesses += 1

        if guess == self.secret_number:
            message = f"Congratulations! You guessed the number in {self.num_guesses} guesses."
            self.submit_button.config(state="disabled")
            self.entry.config(state="disabled")
        elif guess < self.secret_number:
            message = "Too low. Guess again."
        else:
            message = "Too high. Guess again."

        self.output.config(state="normal")
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, message)
        self.output.config(state="disabled")

    def run(self):
        self.root.mainloop()

game = NumberGuesser()
game.run()
