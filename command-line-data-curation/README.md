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

## Usage

1. Run the script using Python:

    ```sh
    python cli_data_entry.py
    ```

2. The script will first display a list of predefined favorite players.
3. It will then prompt the user to share their favorite players by responding with 'Y' or 'N'.
4. If the user responds with 'N', the script will repeatedly prompt until the user responds with 'Y'.
5. Once the user responds with 'Y', they will be asked to input the name of their favorite player.

## Code Explanation

- The script starts by printing a list of predefined favorite players using the `rich` library for styled output.
- It then prompts the user to share their favorite players.
- If the user responds with 'N', the script will keep prompting until the user responds with 'Y'.
- Once the user responds with 'Y', the script will ask for the name of the user's favorite player.

### Main Functions

- `print_players()`: Prints the list of predefined favorite players.
- `addPlayer()`: Prompts the user to input the name of their favorite player.