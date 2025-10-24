import random
import matplotlib.pyplot as plt
from colorama import Fore, Style

# Game constants
BOARD_SIZE = 100
MIN_PLAYERS = 2
MAX_PLAYERS = 7
DICE_SIDES = 6
WINNING_SCORE = 100

class Player:
    """
    Represents a player in the game.
    """
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.position = 0
        self.turns_played = 0
        self.snakes_encountered = 0
        self.ladders_climbed = 0

    def move(self, steps):
        """Move the player by the given number of steps."""
        self.position += steps
        self.turns_played += 1

    def __repr__(self):
        return f"Player(name={self.name}, position={self.position})"

class Board:
    """
    Represents the Snakes and Ladders board.
    """
    def __init__(self):
        # Ladders: start -> end (climbing up)
        self.ladders = {
            2: 38, 7: 14, 8: 31, 15: 26, 21: 42, 28: 84, 36: 44,
            51: 67, 71: 91, 78: 98, 87: 94
        }
        
        # Snakes: start -> end (sliding down)
        self.snakes = {
            16: 6, 46: 25, 49: 11, 62: 19, 64: 60, 74: 53,
            89: 68, 92: 88, 95: 75, 99: 80
        }
        
        # Combined dictionary for easy lookup
        self.special_positions = {**self.ladders, **self.snakes}

    def _get_coordinates(self, position):
        """Convert board position to x, y coordinates."""
        if position % 10 == 0:
            return 90, (position // 10 - 1) * 10
        return (position % 10 - 1) * 10, (position // 10) * 10

    def is_ladder(self, position):
        """Check if position has a ladder."""
        return position in self.ladders

    def is_snake(self, position):
        """Check if position has a snake."""
        return position in self.snakes

    def get_new_position(self, position):
        """Get the new position after landing on a snake or ladder."""
        return self.special_positions.get(position, position)

    def get_text_board(self, players):
        """
        Generate a text-based representation of the board.
        
        Args:
            players: List of Player objects
            
        Returns:
            str: Text representation of the board
        """
        # Create player position map
        player_positions = {}
        for player in players:
            if player.position > 0:  # Only show players who have started
                pos = player.position
                if pos not in player_positions:
                    player_positions[pos] = []
                player_positions[pos].append(player.name[0].upper())  # First letter of name
        
        board_lines = []
        board_lines.append("\n" + "="*60)
        board_lines.append("📊 Current Board State")
        board_lines.append("="*60)
        
        # Display board from top to bottom (100 to 1)
        for row in range(9, -1, -1):
            line = ""
            for col in range(10):
                pos = row * 10 + col + 1
                
                # Format cell
                cell_content = f"{pos:2d}"
                
                # Add special markers
                if pos in self.ladders:
                    cell_content += "🪜"
                elif pos in self.snakes:
                    cell_content += "🐍"
                else:
                    cell_content += "  "
                
                # Add players at this position
                if pos in player_positions:
                    players_here = ''.join(player_positions[pos][:2])  # Max 2 initials
                    cell_content += f"[{players_here}]"
                else:
                    cell_content += "    "
                
                line += cell_content + " "
            
            board_lines.append(line)
        
        board_lines.append("="*60)
        return '\n'.join(board_lines)

    def _draw_grid_lines(self):
        """Draw the grid lines for the board."""
        grid_size = 10
        num_lines = 11
        
        for j in range(num_lines):
            # Vertical lines
            x = [(j * grid_size) - 5 for _ in range(num_lines)]
            y = [grid_size * i - 5 for i in range(num_lines)]
            plt.plot(x, y, c='k', linewidth=0.5)
            
            # Horizontal lines
            x1 = [i * grid_size - 5 for i in range(num_lines)]
            y1 = [(j * grid_size) - 5 for _ in range(num_lines)]
            plt.plot(x1, y1, c='k', linewidth=0.5)

    def show_grid(self, players):
        """Displays the game board with players."""
        plt.figure(figsize=(10, 10))
        
        # Draw ladders in green
        for start, end in self.ladders.items():
            x_start, y_start = self._get_coordinates(start)
            x_end, y_end = self._get_coordinates(end)
            plt.plot([x_start, x_end], [y_start, y_end], c='g', linewidth=2, label='Ladder' if start == 2 else '')
        
        # Draw snakes in magenta
        for start, end in self.snakes.items():
            x_start, y_start = self._get_coordinates(start)
            x_end, y_end = self._get_coordinates(end)
            plt.plot([x_start, x_end], [y_start, y_end], c='m', linewidth=2, label='Snake' if start == 16 else '')

        # Draw grid lines
        self._draw_grid_lines()

        # Set axis labels and ticks
        plt.yticks([10 * i for i in range(10)], [10 * (i) for i in range(1, 11)]) # type: ignore
        plt.xticks([10 * i for i in range(10)], [i for i in range(1, 11)]) # type: ignore

        # Plot players
        colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
        for i, player in enumerate(players):
            if player.position > 0:  # Only show players who have started
                xc, yc = self._get_coordinates(player.position)
                plt.scatter(xc, yc, c=colors[i], s=100, label=player.name, edgecolors='black', linewidths=1)

        plt.title('(っ◔◡◔)っ ♥ Snakes and Ladders ♥', fontsize=16, fontweight='bold')
        plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
        plt.tight_layout()
        plt.show(block=False)
        plt.pause(0.1)  # Brief pause to ensure window updates

class Game:
    """
    Manages the Snakes and Ladders game flow.
    """
    # Player colors for visualization
    PLAYER_COLORS = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'black']
    
    def __init__(self, show_board=True, text_board=True):
        """
        Initialize the game.
        
        Args:
            show_board: Whether to display the matplotlib board after each turn (default: True)
            text_board: Whether to show text-based board in console (default: True)
        """
        self.board = Board()
        self.players = []
        self.game_over = False
        self.show_board = show_board
        self.text_board = text_board
        self.total_turns = 0
        self.game_history = []  # Track all moves for replay

    def setup_players(self):
        """Gets the number of players and their names."""
        num_players = self._get_valid_player_count()
        
        print("\n" + "="*50)
        for i in range(num_players):
            name = self._get_player_name(i + 1)
            player = Player(name, self.PLAYER_COLORS[i])
            self.players.append(player)
            print(f"✓ Player {i+1}: {name} (Color: {self.PLAYER_COLORS[i]}, Initial: {name[0].upper()})")
        print("="*50)

    def _get_valid_player_count(self):
        """Prompt user for a valid number of players."""
        while True:
            try:
                num_players = int(input(f'Enter number of players (minimum {MIN_PLAYERS} and maximum {MAX_PLAYERS}): '))
                if MIN_PLAYERS <= num_players <= MAX_PLAYERS:
                    return num_players
                else:
                    print(f'Invalid number of players. Please enter a number between {MIN_PLAYERS} and {MAX_PLAYERS}.')
            except ValueError:
                print('Invalid input. Please enter a number.')

    def _get_player_name(self, player_number):
        """Get a player's name with validation."""
        while True:
            name = input(f'Enter name of player {player_number}: ').strip()
            if name:
                return name
            else:
                print('Name cannot be empty. Please enter a valid name.')

    def roll_dice(self):
        """Roll a single die and return the result."""
        return random.randint(1, DICE_SIDES)

    def handle_turn(self, player):
        """
        Handle a single player's turn, including extra rolls for sixes.
        
        Args:
            player: The Player object taking their turn
            
        Returns:
            tuple: (total_roll, list of individual rolls)
        """
        max_consecutive_sixes = 3  # Prevent infinite rolling
        total_roll = 0
        rolls = []
        consecutive_sixes = 0
        
        # Keep rolling while player gets 6s
        while consecutive_sixes < max_consecutive_sixes:
            roll = self.roll_dice()
            rolls.append(roll)
            total_roll += roll
            
            if roll == DICE_SIDES:  # Rolled a 6
                consecutive_sixes += 1
                print(Fore.GREEN + f"{player.name} rolled a {DICE_SIDES}! Rolling again..." + Style.RESET_ALL)
                if consecutive_sixes >= max_consecutive_sixes:
                    print(Fore.YELLOW + f"Maximum consecutive {DICE_SIDES}s reached!" + Style.RESET_ALL)
            else:
                break
        
        return total_roll, rolls

    def _process_move(self, player, total_roll):
        """
        Process a player's move and check for special positions.
        
        Args:
            player: The Player object
            total_roll: Total dice roll value
            
        Returns:
            bool: True if player won, False otherwise
        """
        old_position = player.position
        new_position = old_position + total_roll

        # Check if move exceeds winning position
        if new_position > WINNING_SCORE:
            needed = WINNING_SCORE - old_position
            print(Fore.RED + f"❌ Can't move! You need exactly {needed} to win, but rolled {total_roll}." + Style.RESET_ALL)
            print(Fore.YELLOW + f"💡 Tip: You need to roll {needed} or less to reach position {WINNING_SCORE}!" + Style.RESET_ALL)
            return False

        # Move player
        player.move(total_roll)
        
        # Record move in history
        self.game_history.append({
            'player': player.name,
            'turn': player.turns_played,
            'roll': total_roll,
            'from': old_position,
            'to': player.position
        })

        print(f"➡️  {player.name} moves from {old_position} to {player.position}")

        # Check for win
        if player.position == WINNING_SCORE:
            self._announce_winner(player)
            return True

        # Check for snake or ladder
        self._check_special_position(player)
        
        print(f"📍 {player.name} is now at position {player.position}")
        return False

    def _check_special_position(self, player):
        """Check if player landed on a snake or ladder and update position."""
        if self.board.is_ladder(player.position):
            old_pos = player.position
            player.position = self.board.get_new_position(player.position)
            print(Fore.GREEN + f"🪜 Ladder! You climb from {old_pos} to {player.position}!" + Style.RESET_ALL)
            player.ladders_climbed += 1
        elif self.board.is_snake(player.position):
            old_pos = player.position
            player.position = self.board.get_new_position(player.position)
            print(Fore.MAGENTA + f"🐍 Snake! You slide from {old_pos} down to {player.position}!" + Style.RESET_ALL)
            player.snakes_encountered += 1

    def _announce_winner(self, player):
        """Announce the winner and display their statistics."""
        print(Fore.GREEN + f"\n🎉🎉🎉 {player.name} has won the game! 🎉🎉🎉" + Style.RESET_ALL)
        print(f"\n📊 Game Statistics for {player.name}:")
        print(f"   Total turns: {player.turns_played}")
        print(f"   Ladders climbed: {player.ladders_climbed}")
        print(f"   Snakes encountered: {player.snakes_encountered}")

    def _display_board(self):
        """Display the game board if visualization is enabled."""
        # Show text board if enabled
        if self.text_board:
            print(self.board.get_text_board(self.players))
        
        # Show graphical board if enabled
        if self.show_board:
            try:
                self.board.show_grid(self.players)
            except Exception as e:
                print(f"⚠️  Could not display graphical board: {e}")
                print("Continuing with text-only mode...")
                self.show_board = False  # Disable further attempts

    def _show_current_standings(self):
        """Display current standings during the game."""
        print("\n" + "-"*50)
        print("📊 Current Standings:")
        sorted_players = sorted(self.players, key=lambda p: p.position, reverse=True)
        for i, player in enumerate(sorted_players, 1):
            status = "🏆 WINNING!" if player.position == max(p.position for p in self.players) and player.position > 0 else ""
            print(f"  {i}. {player.name}: Position {player.position} {status}")
        print("-"*50)

    def _print_welcome_message(self):
        """Display welcome message and game rules."""
        print("\n" + "="*60)
        print(" " * 15 + "🎲 SNAKES AND LADDERS 🎲")
        print("="*60)
        print("\n📖 GAME RULES:")
        print("  🎲 Roll the dice to move forward on the board")
        print(f"  🎉 Roll a {DICE_SIDES} to get an extra turn (bonus roll!)")
        print("  🪜 Land on a ladder (🪜) to climb up")
        print("  🐍 Land on a snake (🐍) to slide down")
        print(f"  🏆 First to reach exactly position {WINNING_SCORE} wins!")
        print(f"  ⚠️  You must roll the exact number to land on {WINNING_SCORE}")
        print("\n💡 TIPS:")
        print("  • Player initials show on the text board")
        print("  • Watch out for snakes near the end!")
        print("  • Press 'q' at any time to quit")
        print("\n" + "="*60)
        
        # Ask about display preferences
        if self.show_board:
            response = input("\n🖼️  Show graphical board after each turn? (Y/n): ").strip().lower()
            if response == 'n':
                self.show_board = False
                print("✓ Graphical display disabled. Text board will still show.")
        
        print("\n🎮 Let's begin!\n")

    def _print_final_standings(self):
        """Display final standings when game ends."""
        print("\n" + "="*60)
        print(" " * 20 + "🏁 GAME OVER 🏁")
        print("="*60)
        print("\n📊 FINAL STANDINGS:")
        print("-"*60)
        sorted_players = sorted(self.players, key=lambda p: p.position, reverse=True)
        for i, player in enumerate(sorted_players, 1):
            medal = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
            print(f"{medal} {player.name:15s} | Pos: {player.position:3d} | "
                  f"Turns: {player.turns_played:2d} | Ladders: {player.ladders_climbed} | "
                  f"Snakes: {player.snakes_encountered}")
        
        print("-"*60)
        print(f"\n📈 GAME STATISTICS:")
        print(f"  Total turns played: {self.total_turns}")
        print(f"  Total moves recorded: {len(self.game_history)}")
        if self.players:
            winner = max(self.players, key=lambda p: p.position)
            if winner.position == WINNING_SCORE:
                print(f"  � Winner: {winner.name} in {winner.turns_played} turns!")
        
        print("\n" + "="*60)
        print(" " * 15 + "👋 Thanks for playing! 👋")
        print("="*60)

    def play(self):
        """Main function to play the game."""
        self.setup_players()
        self._print_welcome_message()

        while not self.game_over:
            for player in self.players:
                self.total_turns += 1
                
                print(f"\n{'='*50}")
                print(f"� {player.name}'s turn (Currently at position {player.position})")
                print(f"{'='*50}")
                
                action = input('Press Enter to roll the dice or "q" to quit: ')
                if action.lower() == 'q':
                    self.game_over = True
                    print("\n👋 Thanks for playing!")
                    break

                # Roll the dice (with potential extra rolls for 6s)
                total_roll, rolls = self.handle_turn(player)
                
                # Display roll results
                if len(rolls) == 1:
                    print(f"🎲 {player.name} rolled a {rolls[0]}")
                else:
                    print(f"🎲 {player.name} rolled: {' + '.join(map(str, rolls))} = {total_roll}")

                # Process the move and check for win
                won = self._process_move(player, total_roll)
                if won:
                    self.game_over = True
                    break

                # Display the board
                self._display_board()

                if self.game_over:
                    break

        # Show final standings
        self._print_final_standings()

def main():
    """Main entry point for the game."""
    import sys
    
    # Check for command-line arguments
    show_board = True
    text_board = True
    
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if arg == '--no-graphics':
                show_board = False
            elif arg == '--no-text':
                text_board = False
            elif arg == '--help':
                print("Snakes and Ladders Game")
                print("\nUsage: python snakes_and_ladders.py [options]")
                print("\nOptions:")
                print("  --no-graphics    Disable matplotlib graphical board")
                print("  --no-text        Disable text-based board display")
                print("  --help           Show this help message")
                print("\nControls during game:")
                print("  Enter            Roll the dice")
                print("  s                Show current standings")
                print("  q                Quit the game")
                sys.exit(0)
    
    try:
        game = Game(show_board=show_board, text_board=text_board)
        game.play()
    except KeyboardInterrupt:
        print("\n\n⚠️  Game interrupted by user (Ctrl+C)")
        print("👋 Thanks for playing!")
    except Exception as e:
        print(f"\n❌ An error occurred: {e}")
        print("Please report this issue if it persists.")

if __name__ == "__main__":
    main()
