import customtkinter
import random
import configparser
import os
import tkinter.messagebox
import tkinter.simpledialog

class Minesweeper:
    """
    A class to represent the Minesweeper game.
    """
    def __init__(self, master):
        self.master = master
        self.rows = 10
        self.cols = 10
        self.mines = 10
        self.field = []
        self.buttons = []
        self.gameover = False
        self.customsizes = []
        self.colors = ['#FFFFFF', '#0000FF', '#008200', '#FF0000', '#000084', '#840000', '#008284', '#840084', '#000000']

        self.master.title("Minesweeper")

        if os.path.exists("config.ini"):
            self.load_config()
        else:
            self.save_config()

        self.create_menu()
        self.prepare_window()
        self.prepare_game()

    def create_menu(self):
        """
        Creates the menu for the game.
        """
        self.menu_frame = customtkinter.CTkFrame(self.master)
        self.menu_frame.grid(row=0, column=0, columnspan=self.cols, sticky="ew")

        size_button = customtkinter.CTkButton(self.menu_frame, text="Size", command=self.show_size_options)
        size_button.pack(side="left", padx=5, pady=5)

        restart_button = customtkinter.CTkButton(self.menu_frame, text="Restart", command=self.restart_game)
        restart_button.pack(side="left", padx=5, pady=5)

        exit_button = customtkinter.CTkButton(self.menu_frame, text="Exit", command=self.master.destroy)
        exit_button.pack(side="left", padx=5, pady=5)

    def show_size_options(self):
        """
        Shows the size options in a new window.
        """
        size_window = customtkinter.CTkToplevel(self.master)
        size_window.title("Select Size")

        customtkinter.CTkButton(size_window, text="Small (10x10, 10 mines)", command=lambda: self.set_size(10, 10, 10, size_window)).pack(pady=5)
        customtkinter.CTkButton(size_window, text="Medium (20x20, 40 mines)", command=lambda: self.set_size(20, 20, 40, size_window)).pack(pady=5)
        customtkinter.CTkButton(size_window, text="Big (35x35, 120 mines)", command=lambda: self.set_size(35, 35, 120, size_window)).pack(pady=5)
        customtkinter.CTkButton(size_window, text="Custom", command=lambda: self.set_custom_size(size_window)).pack(pady=5)

    def set_size(self, r, c, m, window_to_destroy):
        """
        Sets the size of the game board.
        """
        self.rows = r
        self.cols = c
        self.mines = m
        self.save_config()
        self.restart_game()
        window_to_destroy.destroy()

    def set_custom_size(self, parent_window):
        """
        Sets a custom size for the game board.
        """
        r = tkinter.simpledialog.askinteger("Custom size", "Enter amount of rows", parent=parent_window)
        c = tkinter.simpledialog.askinteger("Custom size", "Enter amount of columns", parent=parent_window)
        m = tkinter.simpledialog.askinteger("Custom size", "Enter amount of mines", parent=parent_window)
        if r and c and m:
            while m > r * c:
                m = tkinter.simpledialog.askinteger("Custom size", f"Maximum mines for this dimension is: {r * c}\nEnter amount of mines", parent=parent_window)
            self.customsizes.insert(0, (r, c, m))
            self.customsizes = self.customsizes[0:5]
            self.set_size(r, c, m, parent_window)

    def save_config(self):
        """
        Saves the current game configuration.
        """
        config = configparser.ConfigParser()
        config.add_section("game")
        config.set("game", "rows", str(self.rows))
        config.set("game", "cols", str(self.cols))
        config.set("game", "mines", str(self.mines))
        config.add_section("sizes")
        config.set("sizes", "amount", str(min(5, len(self.customsizes))))
        for x in range(min(5, len(self.customsizes))):
            config.set("sizes", f"row{x}", str(self.customsizes[x][0]))
            config.set("sizes", f"cols{x}", str(self.customsizes[x][1]))
            config.set("sizes", f"mines{x}", str(self.customsizes[x][2]))

        with open("config.ini", "w") as file:
            config.write(file)

    def load_config(self):
        """
        Loads the game configuration.
        """
        config = configparser.ConfigParser()
        config.read("config.ini")
        self.rows = config.getint("game", "rows")
        self.cols = config.getint("game", "cols")
        self.mines = config.getint("game", "mines")
        amountofsizes = config.getint("sizes", "amount")
        for x in range(amountofsizes):
            self.customsizes.append(
                (
                    config.getint("sizes", f"row{x}"),
                    config.getint("sizes", f"cols{x}"),
                    config.getint("sizes", f"mines{x}"),
                )
            )

    def prepare_game(self):
        """
        Prepares the game field and mines.
        """
        self.field = []
        for x in range(self.rows):
            self.field.append([])
            for y in range(self.cols):
                self.field[x].append(0)

        for _ in range(self.mines):
            x = random.randint(0, self.rows - 1)
            y = random.randint(0, self.cols - 1)
            while self.field[x][y] == -1:
                x = random.randint(0, self.rows - 1)
                y = random.randint(0, self.cols - 1)
            self.field[x][y] = -1

            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= x + i < self.rows and 0 <= y + j < self.cols and self.field[x + i][y + j] != -1:
                        self.field[x + i][y + j] += 1

    def prepare_window(self):
        """
        Prepares the game window with buttons.
        """
        self.game_frame = customtkinter.CTkFrame(self.master)
        self.game_frame.grid(row=1, column=0, columnspan=self.cols)
        self.buttons = []
        for x in range(self.rows):
            self.buttons.append([])
            for y in range(self.cols):
                b = customtkinter.CTkButton(self.game_frame, text=" ", width=40, height=40, command=lambda x=x, y=y: self.click_on(x, y))
                b.bind("<Button-3>", lambda e, x=x, y=y: self.on_right_click(x, y))
                b.grid(row=x, column=y)
                self.buttons[x].append(b)

    def restart_game(self):
        """
        Restarts the game.
        """
        self.gameover = False
        for widget in self.master.winfo_children():
            widget.destroy()
        self.create_menu()
        self.prepare_window()
        self.prepare_game()

    def click_on(self, x, y):
        """
        Handles a left click on a button.
        """
        if self.gameover:
            return

        self.buttons[x][y].configure(text=str(self.field[x][y]))

        if self.field[x][y] == -1:
            self.buttons[x][y].configure(text="*", fg_color="red")
            self.gameover = True
            tkinter.messagebox.showinfo("Game Over", "You have lost.")
            for _x in range(self.rows):
                for _y in range(self.cols):
                    if self.field[_x][_y] == -1:
                        self.buttons[_x][_y].configure(text="*", fg_color="red")
        else:
            self.buttons[x][y].configure(fg_color=self.colors[field[x][y]])

        if self.field[x][y] == 0:
            self.buttons[x][y].configure(text=" ")
            self.auto_click_on(x, y)

        self.buttons[x][y].configure(state="disabled")
        self.check_win()

    def auto_click_on(self, x, y):
        """
        Automatically clicks on surrounding buttons if the clicked button is a 0.
        """
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < self.rows and 0 <= y + j < self.cols:
                    if self.buttons[x+i][y+j].cget("state") == "normal":
                        self.click_on(x+i, y+j)

    def on_right_click(self, x, y):
        """
        Handles a right click on a button.
        """
        if self.gameover:
            return

        if self.buttons[x][y].cget("text") == "?":
            self.buttons[x][y].configure(text=" ", state="normal")
        elif self.buttons[x][y].cget("text") == " " and self.buttons[x][y].cget("state") == "normal":
            self.buttons[x][y].configure(text="?", state="disabled")

    def check_win(self):
        """
        Checks if the player has won the game.
        """
        win = True
        for x in range(self.rows):
            for y in range(self.cols):
                if self.field[x][y] != -1 and self.buttons[x][y].cget("state") == "normal":
                    win = False
        if win:
            tkinter.messagebox.showinfo("Game Over", "You have won.")
            self.gameover = True

if __name__ == "__main__":
    customtkinter.set_appearance_mode("System")
    customtkinter.set_default_color_theme("blue")

    app = customtkinter.CTk()
    game = Minesweeper(app)
    app.mainloop()
