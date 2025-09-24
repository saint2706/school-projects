from .team import Team
from .player import Player
from .pitch import Pitch
import time
import random

class Game:
    """
    Represents a game of FIFA.
    """
    def __init__(self):
        self.team1 = self._create_team("Barcelona")
        self.team2 = self._create_team("PSG")
        self.pitch = Pitch()
        self.ball_position = [50, 25]
        self.possession = random.choice([self.team1, self.team2])
        self.game_time = 0

    def _create_team(self, name):
        """Creates a team with players."""
        players = []
        if name == "Barcelona":
            players.append(Player("Ter Stegen", [5, 25]))
            players.append(Player("Pique", [20, 15]))
            players.append(Player("Umtiti", [20, 35]))
            players.append(Player("Rakitic", [40, 10]))
            players.append(Player("Busquets", [40, 25]))
            players.append(Player("Arthur", [40, 40]))
            players.append(Player("Coutinho", [60, 5]))
            players.append(Player("Messi", [60, 25]))
            players.append(Player("Dembele", [60, 45]))
            players.append(Player("Suarez", [80, 25]))
        else: # PSG
            players.append(Player("Buffon", [95, 25]))
            players.append(Player("Thiago Silva", [80, 15]))
            players.append(Player("Kimpembe", [80, 35]))
            players.append(Player("Verrati", [60, 10]))
            players.append(Player("Marquinhos", [60, 25]))
            players.append(Player("Rabiot", [60, 40]))
            players.append(Player("Dani Alves", [40, 5]))
            players.append(Player("Neymar", [40, 25]))
            players.append(Player("Mbappe", [40, 45]))
            players.append(Player("Cavani", [20, 25]))

        return Team(name, players)

    def play(self):
        """Main function to play the game."""
        print("--- Welcome to FIFA 2019 ---")
        print(f"{self.team1.name} vs {self.team2.name}")
        print(f"{self.possession.name} starts with the ball.")

        while self.game_time < 90:
            self.pitch.draw_pitch(self.team1, self.team2)
            print(f"--- Minute {self.game_time} ---")
            print(f"{self.possession.name} has the ball.")

            self._player_turn()

            self.game_time += random.randint(1, 5)
            time.sleep(1)

        print("--- Full Time ---")
        print(f"Final Score: {self.team1.name} {self.team1.score} - {self.team2.score} {self.team2.name}")

    def _player_turn(self):
        """Manages a single player's turn."""
        player_with_ball = self._get_player_with_ball()
        print(f"{player_with_ball.name} has the ball.")

        action = input("Choose an action (pass, shoot, skill): ").lower()

        if action == "pass":
            self._pass_ball(player_with_ball)
        elif action == "shoot":
            self._shoot(player_with_ball)
        elif action == "skill":
            self._skill_move(player_with_ball)
        else:
            print("Invalid action. Turnover!")
            self._turnover()

    def _get_player_with_ball(self):
        """Finds the player closest to the ball."""
        closest_player = None
        min_dist = float('inf')
        for player in self.possession.players:
            dist = ((player.position[0] - self.ball_position[0])**2 +
                    (player.position[1] - self.ball_position[1])**2)**0.5
            if dist < min_dist:
                min_dist = dist
                closest_player = player
        return closest_player

    def _pass_ball(self, player):
        """Handles a pass action."""
        target_player = random.choice(self.possession.players)
        print(f"{player.name} passes to {target_player.name}.")

        # Simple pass logic
        if random.random() > 0.2: # 80% pass success rate
            self.ball_position = target_player.position
            print("Pass successful!")
        else:
            print("Pass intercepted!")
            self._turnover()

    def _shoot(self, player):
        """Handles a shoot action."""
        print(f"{player.name} shoots!")

        # Simple shoot logic
        distance_to_goal = self.ball_position[0] if self.possession == self.team2 else 100 - self.ball_position[0]
        shot_accuracy = 1 - (distance_to_goal / 100) # Higher accuracy closer to goal

        if random.random() < shot_accuracy:
            print("GOOOOAL!")
            self.possession.score += 1
            self._turnover()
        else:
            print("Shot missed!")
            self._turnover()

    def _skill_move(self, player):
        """Handles a skill move action."""
        print(f"{player.name} tries a skill move!")

        if random.random() > 0.5: # 50% skill move success rate
            print("Skill move successful!")
            # Move the player and ball forward
            direction = 1 if self.possession == self.team1 else -1
            player.position[0] += direction * 10
            self.ball_position = player.position
        else:
            print("Skill move failed! Turnover!")
            self._turnover()

    def _turnover(self):
        """Changes possession of the ball."""
        if self.possession == self.team1:
            self.possession = self.team2
        else:
            self.possession = self.team1
        print(f"{self.possession.name} now has the ball.")
