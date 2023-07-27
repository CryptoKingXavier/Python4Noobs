# Rock, Paper, Scissors Game in Python
from random import randint

# Model 1: Person-2-Person
ROCK_STATE: list = ['r', 'R', 'rock', 'Rock', 'ROCK']
PAPER_STATE: list = ['p', 'P', 'paper', 'Paper', 'PAPER']
SCISSORS_STATE: list = ['s', 'S', 'scissors', 'Scissors', 'SCISSORS']

def Welcome_Msg() -> None: print('Welcome To My RPS-Game! \tEnter R/P/S')

def Rules(p1Name: str, p1Choice: str, p2Name: str, p2Choice: str) -> str:
    if (p1Choice in ROCK_STATE or p1Choice in PAPER_STATE or p1Choice in SCISSORS_STATE) \
    and (p2Choice in ROCK_STATE or p2Choice in PAPER_STATE or p2Choice in SCISSORS_STATE) \
    and (p1Choice == p2Choice): return f'{p1Name} and {p2Name} Tied!'
    elif (p1Choice in ROCK_STATE and p2Choice in PAPER_STATE): return f'{p2Name} Wins!'
    elif (p1Choice in ROCK_STATE and p2Choice in SCISSORS_STATE): return f'{p1Name} Wins!'
    elif (p1Choice in PAPER_STATE and p2Choice in ROCK_STATE): return f'{p1Name} Wins!'
    elif (p1Choice in PAPER_STATE and p2Choice in SCISSORS_STATE): return f'{p2Name} Wins!'
    elif (p1Choice in SCISSORS_STATE and p2Choice in ROCK_STATE): return f'{p2Name} Wins!'
    elif (p1Choice in SCISSORS_STATE and p2Choice in PAPER_STATE): return f'{p1Name} Wins!'
    else: return f'{p1Name}/{p2Name} State Not Found!'

def RPS_PvP():   # Player Vs Player
    Welcome_Msg()

    # Getting player names
    player1_Name: str = input('Player-1 Name: ')
    player2_Name: str = input('Player-2 Name: ')

    print()   # new line

    # Getting player choices
    player1_Choice: str = input(f'{player1_Name}-Choice: ')
    player2_Choice: str = input(f'{player2_Name}-Choice: ')

    # Getting winner
    print(
        Rules(
            p1Name=player1_Name,
            p2Name=player2_Name,
            p1Choice=player1_Choice,
            p2Choice=player2_Choice
        )
    )

# Model 2: Person-2-Computer
def RPS_CvP():   # Computer Vs Player
    Welcome_Msg()

    # Getting player name
    player1_Name: str = input('Enter Name: ')
    player2_Name: str = 'AI'

    print()   # new line

    # Getting player choice
    player1_Choice: str = input(f'{player1_Name}-Choice: ')
    
    # Getting AI choice
    AI_STATES: list = ['R', 'P', 'S']
    # randint(a, b): this is a method of the random module that generates a randint (random integer) between a (inclusive) and b (inclusive)
    player2_Choice: str = AI_STATES[randint(0, 2)]

    # Getting winner
    print(
        Rules(
            p1Name=player1_Name,
            p2Name=player2_Name,
            p1Choice=player1_Choice,
            p2Choice=player2_Choice
        )
    )

def GameState(state: str) -> None: RPS_PvP() if state == '1' else RPS_CvP()

def GamePlay() -> None:

    # To clear system terminal
    try:
        from os import system
        system('cls')
    except Exception:
        print('Command Not Found!')
    finally:
        state: str = input('Pick a number: 1. Person-vs-Person | 2. Person-vs-Computer: ')
        GameState(state)

# Launch Game
GamePlay()
