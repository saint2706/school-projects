import customtkinter
import random
import configparser
import os
import tkinter
from typing import List, Tuple

class MinesweeperGame:
    """
    Encapsulates the core logic of the Minesweeper game.
    """
    def __init__(self, rows: int, cols: int, mines: int):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.field: List[List[int]] = []
        self.is_game_over = False
        self.is_win = False
        self.prepare_game()

    def prepare_game(self) -> None:
        """Initializes the game field and places the mines."""
        self.field = [[0] * self.cols for _ in range(self.rows)]
        mine_positions = random.sample(range(self.rows * self.cols), self.mines)

        for pos in mine_positions:
            r, c = divmod(pos, self.cols)
            self.field[r][c] = -1
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= r + i < self.rows and 0 <= c + j < self.cols and self.field[r + i][c + j] != -1:
                        self.field[r + i][c + j] += 1

    def click(self, r: int, c: int) -> List[Tuple[int, int]]:
        """
        Handles a click on a cell, revealing it.
        Returns a list of cells to be revealed.
        """
        if self.field[r][c] == -1:
            self.is_game_over = True
            return []

        revealed = []
        if self.field[r][c] == 0:
            self.reveal_empty_cells(r, c, revealed)
        else:
            revealed.append((r, c))

        self.check_win()
        return revealed

    def reveal_empty_cells(self, r: int, c: int, revealed: List[Tuple[int, int]]) -> None:
        """Recursively reveals empty cells and their neighbors."""
        if (r, c) in revealed:
            return
        revealed.append((r,c))

        if self.field[r][c] == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= r + i < self.rows and 0 <= c + j < self.cols:
                        self.reveal_empty_cells(r + i, c + j, revealed)

    def check_win(self) -> None:
        """Checks if the player has won the game."""
        # This logic needs to be handled in the UI class based on revealed cells
        pass

class MinesweeperUI(customtkinter.CTk):
    """
    Handles the user interface for the Minesweeper game.
    """
    def __init__(self):
        super().__init__()
        self.title("Minesweeper")
        self.rows = 10
        self.cols = 10
        self.mines = 10
        self.buttons: List[List[customtkinter.CTkButton]] = []
        self.revealed_cells = set()

        self.colors = {
            "System": {
                1: "#2b75f3", 2: "#2fa236", 3: "#d32f2f", 4: "#7b1fa2",
                5: "#ff8f00", 6: "#00838f", 7: "#d32f2f", 8: "#7b1fa2"
            }
        }

        if os.path.exists("config.ini"):
            self.load_config()

        self.game = MinesweeperGame(self.rows, self.cols, self.mines)
        self.create_widgets()

    def create_widgets(self):
        """Creates and places all widgets in the window."""
        self.main_frame = customtkinter.CTkFrame(self)
        self.main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.menu_frame = customtkinter.CTkFrame(self.main_frame)
        self.menu_frame.pack(pady=5, fill="x")

        customtkinter.CTkButton(self.menu_frame, text="Size", command=self.show_size_options).pack(side="left", padx=5)
        customtkinter.CTkButton(self.menu_frame, text="Restart", command=self.restart_game).pack(side="left", padx=5)
        customtkinter.CTkButton(self.menu_frame, text="Exit", command=self.destroy).pack(side="left", padx=5)

        self.game_frame = customtkinter.CTkFrame(self.main_frame)
        self.game_frame.pack(pady=5, fill="both", expand=True)

        self.buttons = []
        self.revealed_cells = set()
        for r in range(self.rows):
            self.buttons.append([])
            for c in range(self.cols):
                button = customtkinter.CTkButton(self.game_frame, text=" ", width=30, height=30, command=lambda r=r, c=c: self.on_left_click(r, c))
                button.bind("<Button-3>", lambda e, r=r, c=c: self.on_right_click(r, c))
                button.grid(row=r, column=c, padx=1, pady=1)
                self.buttons[r].append(button)

    def on_left_click(self, r: int, c: int):
        """Handles a left click on a cell."""
        if self.game.is_game_over or (r,c) in self.revealed_cells:
            return

        if self.game.field[r][c] == -1:
            self.game.is_game_over = True
            self.reveal_all_mines()
            self._show_message("Game Over", "You have lost.")
            return

        to_reveal = self.game.click(r, c)
        for row, col in to_reveal:
            self.reveal_cell(row, col)

        self.check_win()

    def reveal_cell(self, r: int, c: int):
        """Reveals a single cell on the board."""
        if (r,c) in self.revealed_cells:
            return

        self.revealed_cells.add((r,c))
        button = self.buttons[r][c]
        value = self.game.field[r][c]

        button.configure(state="disabled", fg_color="gray")
        if value > 0:
            theme = customtkinter.get_appearance_mode()
            color = self.colors.get(theme, self.colors["System"]).get(value, "white")
            button.configure(text=str(value), text_color=color)
        else:
            button.configure(text=" ")

    def reveal_all_mines(self):
        """Reveals all mines when the game is over."""
        for r in range(self.rows):
            for c in range(self.cols):
                if self.game.field[r][c] == -1:
                    self.buttons[r][c].configure(text="🚩", fg_color="red")

    def on_right_click(self, r: int, c: int):
        """Handles a right click on a cell to flag it."""
        if self.game.is_game_over or (r,c) in self.revealed_cells:
            return

        button = self.buttons[r][c]
        if button.cget("text") == "🚩":
            button.configure(text=" ", state="normal")
        elif button.cget("text") == " ":
            button.configure(text="🚩", state="disabled")

    def check_win(self):
        """Checks if the player has won."""
        if not self.game.is_win and len(self.revealed_cells) == self.rows * self.cols - self.mines:
            self.game.is_game_over = True
            self.game.is_win = True
            self.reveal_all_mines()
            self._show_message("Congratulations!", "You have won!")

    def _show_message(self, title: str, message: str):
        """Displays a message in a custom dialog."""
        dialog = customtkinter.CTkToplevel(self)
        dialog.title(title)
        dialog.geometry("280x150")

        dialog.grid_columnconfigure(0, weight=1)
        dialog.grid_rowconfigure(0, weight=1)

        label = customtkinter.CTkLabel(dialog, text=message, font=customtkinter.CTkFont(size=16))
        label.pack(pady=20, padx=20, expand=True, fill="both")

        ok_button = customtkinter.CTkButton(dialog, text="OK", command=dialog.destroy)
        ok_button.pack(pady=10, padx=20)

        dialog.transient(self)
        dialog.grab_set()
        self.wait_window(dialog)

    def show_size_options(self):
        """Shows a dialog to select the game size."""
        size_window = customtkinter.CTkToplevel(self)
        size_window.title("Select Size")

        def set_size(r, c, m):
            self.rows, self.cols, self.mines = r, c, m
            self.save_config()
            self.restart_game()
            size_window.destroy()

        customtkinter.CTkButton(size_window, text="Small (10x10, 10 mines)", command=lambda: set_size(10, 10, 10)).pack(pady=5, padx=10)
        customtkinter.CTkButton(size_window, text="Medium (16x16, 40 mines)", command=lambda: set_size(16, 16, 40)).pack(pady=5, padx=10)
        customtkinter.CTkButton(size_window, text="Large (30x16, 99 mines)", command=lambda: set_size(30, 16, 99)).pack(pady=5, padx=10)

    def restart_game(self):
        """Restarts the game with the current settings."""
        for widget in self.main_frame.winfo_children():
            widget.destroy()
        self.game = MinesweeperGame(self.rows, self.cols, self.mines)
        self.create_widgets()

    def save_config(self):
        """Saves the current game configuration."""
        config = configparser.ConfigParser()
        config["game"] = {
            "rows": str(self.rows),
            "cols": str(self.cols),
            "mines": str(self.mines)
        }
        with open("config.ini", "w") as configfile:
            config.write(configfile)

    def load_config(self):
        """Loads game configuration from config.ini."""
        config = configparser.ConfigParser()
        config.read("config.ini")
        if "game" in config:
            self.rows = int(config["game"].get("rows", 10))
            self.cols = int(config["game"].get("cols", 10))
            self.mines = int(config["game"].get("mines", 10))

if __name__ == "__main__":
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")
    app = MinesweeperUI()
    app.mainloop()