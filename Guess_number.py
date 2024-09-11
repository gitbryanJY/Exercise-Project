import sys
import random


def gn(name='PlayerOne'):
    game_count = 0
    player_wins = 0

    def play_gn():
        nonlocal name
        nonlocal player_wins

        playerchoice = input(
            f"\n{name}, guess what number i'm thinking of... 1, 2, or 3.\n\n")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1, 2, or 3.")
            return play_gn()

        player = int(playerchoice)

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\n{name}, you chose {
              str(player)}.")
        print(
            f"I was thinking about the number {str(computer)}.\n")

        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            if player == computer:
                player_wins += 1
                return f"{name}, you win!"
            else:
                return f"\nSorry, {name}. Better luck next time."

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {
              format(((player_wins/game_count)*100), '.2f')}%")

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input("\nY for Yes or \nQ to Quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_gn()
        else:
            print("\n🎉🎉🎉🎉")
            print("Thank you for playing!\n")
            sys.exit(f"Bye {name}! 👋")

    return play_gn


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game."
    )

    args = parser.parse_args()

    guessnumber = gn(args.name)
    guessnumber()
