from rich.console import Console
from rich.table import Table

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

print_players()


console.print("\nWould you care to share your favorite players? Please respond Y/N (To simply put it; YOU ARE FORCED TO ADD A PLAYER HAHAHAHAHAH :D )", style="bright_green")
y_n = input("Y/N: ")

while y_n != "Y":
    console.print("What did I tell you!", style="bright_green")
    y_n = input("Y/N: ")

def addPlayer():
    console.print("What is the name of your favorite player?", style="bright_green")
    player = input("Player: ")

    console.print("What team does your favorite player play for?", style="bright_green")
    team = input("Team: ")

    console.print("What is the age of your favorite player?", style="bright_green")
    age = input("Age: ")

    console.print("What is the salary of your favorite player? (you can look this up on the Internet)", style="bright_green")
    salary = input("Salary: ")

    favorite_player = {"Player": player, "Team": team, "Age": age, "Salary": salary}
    console.print("Your favorite player has been added: ", style="bright_green")

    for field, value in favorite_player.items():
        console.print(f"[bright_green]{field}[/bright_green]: {value}")
    favorite_players.append(favorite_player)

addPlayer()

  
def prompt():
    console.print("Would you like to add another player? Please respond with Yes/No/View", style="bright_green")
    next = input("Yes/No/View: ")
    
    while next != 'Yes' and next != 'No' and next != 'View':
        console.print("You chose nothing! Make sure you choose Yes, No, or View", style="bright_green")
        next = input("Yes/No/View: ")

    if next == 'Yes':
        addPlayer()
        prompt()
    
    elif next == 'No':
        console.print('Thanks for participating in my favorite soccer player fun!', style="bright_green")
    
    elif next == 'View':
        print_players()
        prompt()
    
prompt()