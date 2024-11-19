from rich.console import Console
from rich.table import Table
import json

""" All information about the players and are from the following sources: (https://www.spotrac.com) """

# Create a Console instance to print formatted text
console = Console()

favorite_players = [
    {
        "Player": 'Messi',
        "Team": "Inter Miami FC",
        "Age": 37,
        "Salary": 20446667
    },
    {
        "Player": 'Rashford',
        "Team": "Manchester United F.C.",
        "Age": 26,
        "Salary": 15600000
    },
    {
        "Player": "Haaland",
        "Team": "Manchester City F.C.",
        "Age": 24,
        "Salary": 19500000
    },
    {
        "Player": 'Salah',
        "Team": 'Liveerpool F.C.',
        "Age": 32,
        "Salary": 18200000
    }
]

console.print("What's up! I am making favorite soccer player list. Here are mine:", style="bright_green")

def print_players():
    console.print("\n[bright_green]My favorite players:[/bright_green]")
    for player in favorite_players:
        console.print("\n")
        for field, value in player.items():
            console.print(f"[bright_green]{field}[/bright_green]: {value}")

def save_players_to_file(filename):
    with open(filename, 'w') as file:
        json.dump(favorite_players, file, indent=4)

def add_player():
    while True:
        console.print("What is the name of your favorite player?", style="bright_green")
        player = input("Player: ")
        console.print("What team does the player play for?", style="bright_green")
        team = input("Team: ")
        console.print("What is the player's age?", style="bright_green")
        age = int(input("Age: "))
        console.print("What is the player's salary?", style="bright_green")
        salary = int(input("Salary: "))

        favorite_players.append({
            "Player": player,
            "Team": team,
            "Age": age,
            "Salary": salary
        })

        console.print(f"[bright_green]{player} has been added to your favorite players list.[/bright_green]")

        console.print("Do you want to add another player? (yes/no)", style="bright_green")
        if input().lower() != 'yes':
            break

# Print players
print_players()

# Save players to a local file
save_players_to_file('favorite_players.json')

# Add new players
add_player()

# Save updated players to a local file
save_players_to_file('favorite_players.json')