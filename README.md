# YahtzeeGame
A command-line implementation of the popular Yahtzee dice game in Python. This project allows multiple players to play the game, keeping track of scores and providing a scorecard at the end of the game.

## Features

- Simulates a 5-dice roll with up to three rolls per turn.
- Supports multiple players.
- Implements various Yahtzee scoring rules, including full house, straights, and of a kind.
- Displays a scorecard for each player after their turn.
- Declares the winner at the end of the game.

## Prerequisites

Ensure you have Python installed on your system. This game has been tested with Python 3.6+.

## How to Run Locally

1. **Clone the Repository**
   
   First, clone the repository from GitHub to your local machine:
   ```bash
   git clone https://github.com/jake00o/YahtzeeGame
   ```

2. **Navigate to the Project Directory**

   Change to the project directory:
   ```bash
   cd yahtzee-game
   ```

3. **Run the Game**

   Execute the script to start the game:
   ```bash
   python yahtzee.py
   ```

## How to Play

1. **Start the Game**

   Upon running the script, you will be prompted to enter the number of players. Enter the number of players and their names.

2. **Roll Dice**

   Players take turns to roll the dice. Each player can roll the dice up to three times per turn, choosing which dice to keep and which to re-roll.

3. **Choose Points**

   After rolling the dice, players will be presented with various scoring options based on their roll. Players can choose the best option to maximize their score.

4. **End of Game**

   The game continues for 13 rounds. After all rounds are completed, the final scores are displayed, and the player with the highest score is declared the winner.

## Code Structure

- **Player Class**: Manages player-specific details like name, score, moves, etc.
- **Roll Function**: Handles the dice rolling logic.
- **Scoring Functions**: Calculate scores for different combinations like full house, straights, and of a kind.
- **Main Loop**: The main game loop where players take turns, roll dice, choose points, and display the scorecard.

## Screenshots

Welcome Screen:

```
██╗░░░██╗░█████╗░██╗░░██╗████████╗███████╗███████╗███████╗
╚██╗░██╔╝██╔══██╗██║░░██║╚══██╔══╝╚════██║██╔════╝██╔════╝
░╚████╔╝░███████║███████║░░░██║░░░░░███╔═╝█████╗░░█████╗░░
░░╚██╔╝░░██╔══██║██╔══██║░░░██║░░░██╔══╝░░██╔══╝░░██╔══╝░░
░░░██║░░░██║░░██║██║░░██║░░░██║░░░███████╗███████╗███████╗
░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚══════╝╚══════╝

░██████╗░░█████╗░███╗░░░███╗███████╗
██╔════╝░██╔══██╗████╗░████║██╔════╝
██║░░██╗░███████║██╔████╔██║█████╗░░
██║░░╚██╗██╔══██║██║╚██╔╝██║██╔══╝░░
╚██████╔╝██║░░██║██║░╚═╝░██║███████╗
░╚═════╝░╚═╝░░╚═╝╚═╝░░░░░╚═╝╚══════╝

```

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Please ensure your changes are well-tested and follow the project's coding standards.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

If you have any questions or need further assistance, please contact me in issues

Enjoy playing Yahtzee! 🎲
