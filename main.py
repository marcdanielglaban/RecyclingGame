import random
import tkinter as tk
from tkinter import messagebox

class Trash:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def __str__(self):
        return f"{self.name} ({self.category})"

class Bin:
    def __init__(self, category):
        self.category = category
        self.stuff = []

    def accept(self, trash):
        self.stuff.append(trash)

    def display_contents(self):
        return f"{self.category} Bin: {', '.join(str(item) for item in self.stuff)}"

    def __str__(self):
        return self.display_contents()

class RecyclingGame:
    DIFFICULTY_SETTINGS = {
        "easy": {"duration": 20},
        "medium": {"duration": 15},
        "hard": {"duration": 10},
    }

    def __init__(self, master):
        self.master = master
        master.title("Recycling Game")
        master.configure(bg="#D2B48C")  # Set background color to light brown

        self.score = 0  # Initialize the score attribute

        self.trash_list = [
            Trash("Homework", "Paper"),
            Trash("Soda Can", "Metal"),
            Trash("Plastic Bag", "Plastic"),
            Trash("Newspaper", "Paper"),
            Trash("Aluminum Foil", "Metal"),
            Trash("Water Bottle", "Plastic"),
            Trash("Glass Bottle", "Glass"),
            Trash("Cardboard Box", "Paper"),
            Trash("Tin Can", "Metal"),
            Trash("Styrofoam Cup", "Plastic"),
        ]

        # Initialize bins_list
        self.bins_list = [
            Bin("Paper"),
            Bin("Metal"),
            Bin("Plastic"),
            Bin("Glass"),
        ]

        self.total_unique_items = len(set(item.name for item in self.trash_list))
        self.timer_duration = 10
        self.remaining_time = self.timer_duration
        self.game_active = False
        self.result_window_shown = False

        self.difficulty_var = tk.StringVar(master, "easy")  # Default difficulty is set to easy

        self.difficulty_menu = tk.OptionMenu(master, self.difficulty_var, *self.DIFFICULTY_SETTINGS.keys())
        self.difficulty_menu.pack(pady=10)

        self.start_button = tk.Button(master, text="Start Game", command=self.play_game, font=("Arial", 14))
        self.start_button.pack()

        self.label = tk.Label(master, text="Welcome to the Recycling Game!", font=("Arial", 16), bg="#D2B48C")
        self.label.pack()

        self.score_label = tk.Label(master, text="Score: 0", font=("Arial", 14), bg="#D2B48C")
        self.score_label.pack()

        self.timer_label = tk.Label(master, text="Time left: ", font=("Arial", 14), bg="#D2B48C")
        self.timer_label.pack()

        self.button_frame = tk.Frame(master, bg="#D2B48C")
        self.button_frame.pack()

        self.create_bin_buttons()

    def create_bin_buttons(self):
        self.bin_buttons = []
        for bin in self.bins_list:
            bin_button = tk.Button(
                self.button_frame,
                text=bin.category,
                command=lambda b=bin.category: self.select_bin(b),
                width=8,
                height=3,
                font=("Arial", 12),
                bg="lightgray",
                relief=tk.GROOVE,
            )
            bin_button.pack(side=tk.LEFT, padx=10, pady=10)
            self.bin_buttons.append(bin_button)

    def select_bin(self, chosen_bin):
        if self.game_active:
            matching_bin = next((bin for bin in self.bins_list if bin.category == chosen_bin), None)

            if matching_bin and matching_bin.category == self.current_item.category:
                matching_bin.accept(self.current_item)
                self.update_score(1)
            else:
                self.update_score(-1)

            self.next_item()

    def play_game(self):
        selected_difficulty = self.difficulty_var.get()
        self.timer_duration = self.DIFFICULTY_SETTINGS[selected_difficulty]["duration"]

        random.shuffle(self.trash_list)

        self.start_button.config(state=tk.DISABLED)
        self.game_active = True
        self.remaining_time = self.timer_duration
        self.update_timer()
        self.next_item()

    def next_item(self):
        if self.trash_list:
            self.current_item = self.trash_list.pop(0)
            self.label.config(text=f"\nItem to sort: {self.current_item.name}")
        else:
            self.show_results()

    def update_timer(self):
        if self.remaining_time > 0 and self.game_active:
            self.timer_label.config(text=f"Time left: {self.remaining_time}")
            self.remaining_time -= 1
            self.master.after(1000, self.update_timer)
        else:
            if self.game_active:
                self.timer_label.config(text="Time's up!")
                self.show_results()

    def update_score(self, points):
        self.score += points
        if self.score < 0:
            self.score = 0
        self.score_label.config(text=f"Score: {self.score}")

    def show_results(self):
        if not self.result_window_shown:
            self.result_window_shown = True
            self.game_active = False

            accuracy = self.calculate_accuracy()
            grade = self.calculate_grade(accuracy)

            messagebox.showinfo(
                "Game Over",
                f"Accuracy: {accuracy:.2f}%! Your grade: {grade}.\nKeep rocking that recycling game!"
            )

            self.display_bin_contents()

            if not self.game_active:
                self.master.destroy()

    def calculate_accuracy(self):
        correctly_sorted_items = set()
        for bin in self.bins_list:
            correctly_sorted_items.update(item for item in bin.stuff if item.category == bin.category)
        return (len(correctly_sorted_items) / self.total_unique_items) * 100 if self.total_unique_items > 0 else 0

    def calculate_grade(self, accuracy):
        if accuracy >= 90:
            return "Gold"
        elif accuracy >= 75:
            return "Silver"
        elif accuracy >= 50:
            return "Bronze"
        else:
            return "No Grade"

    def display_bin_contents(self):
        bin_contents = "\nBin Contents:"
        for bin in self.bins_list:
            bin_contents += "\n" + str(bin)
        messagebox.showinfo("Bin Contents", bin_contents)


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("600x300")  
    game = RecyclingGame(root)
    root.mainloop()
