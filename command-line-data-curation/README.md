# Favorite Players CLI

This script is a simple command-line interface (CLI) application that allows users to view and add their favorite football players. It uses the `rich` library to print styled text to the console.

## Prerequisites

- Python 3.x
- `rich` library

## Installation

1. Clone the repository or download the script.
2. Install the `rich` library using pip:

    ```sh
    pip install rich
    ```

## Code Explanation/Usage

1. Run the script using Python:

    ```sh
    python cli_data_entry.py
    ```

2. The script will first display a list of predefined favorite players.
3. It will then prompt the user to share their favorite players by responding with 'Y' or 'N'. Theres a bit of a surprise with this one haha!!!
4. If selected `Y` (Yes), the script will ask for the details of the user's favorite player. You will be given attributes to fill out, like the `Name`, `Team`, `Age`, and `Salary` of the favorite player. You will be able to Google the salaries of your favorite player if you do not know it. I used [https://www.spotrac.com](https://www.spotrac.com) as my website to track the salaries. You can even add yourself as your favorite player!!!
5. After step 4, you are allowed to add more, view all the players that are currently in the list, or exit from the script.

### Main Functions

- `print_players()`: Prints the list of predefined favorite players.
- `addPlayer()`: Prompts the user to input the name of their favorite player.