import matplotlib.pyplot as plt
from matplotlib import collections as mc
import numpy as np

class Pitch:
    """
    Represents the soccer pitch and handles visualization.
    """
    def __init__(self, length=100, width=50):
        self.length = length
        self.width = width

    def draw_pitch(self, team1, team2):
        """Draws the pitch with the players."""
        fig, ax = plt.subplots(figsize=(self.length / 10, self.width / 10))
        ax.set_facecolor('green')

        # Draw pitch markings
        lines = [
            [(0, 0), (self.length, 0)],
            [(0, self.width), (self.length, self.width)],
            [(0, 0), (0, self.width)],
            [(self.length, 0), (self.length, self.width)],
            [(self.length / 2, 0), (self.length / 2, self.width)]
        ]
        lc = mc.LineCollection(lines, colors='white', linewidths=2)
        ax.add_collection(lc)

        # Draw players
        for player in team1.players:
            plt.scatter(player.position[0], player.position[1], c='red', s=100, label=team1.name)
        for player in team2.players:
            plt.scatter(player.position[0], player.position[1], c='blue', s=100, label=team2.name)

        plt.xlim(0, self.length)
        plt.ylim(0, self.width)
        plt.title("FIFA 2019")
        plt.legend()
        plt.show()
