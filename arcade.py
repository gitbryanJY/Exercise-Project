import sys
from guess_number import guessnumber
from rps_final import rock_paper_scissors


def play_acd(name='PlayerOne'):
    print(f"\n{name}, welcome to the Arcade! 🤖\n")

    def play_choice():
        nonlocal name
        playerchoice = input(
            f'\nPlease choose a game:\n1 = Rock Paper Scissors\n2 = Guess My Number\n\nOr press "x" to exit the Arcade\n\n')

        if playerchoice not in ["1", "2", "x", "X"]:
            print(f"{name}, please enter 1, 2, or x.")
            return play_choice()

        if playerchoice == "1":
            rock_paper_scissors(name, standalone=False)()
        elif playerchoice == "2":
            guessnumber(name, standalone=False)()
        else:
            print("\nSee you next time!\n")
            sys.exit(f"Bye {name}! 👋")

        print(f"\n{name}, welcome back to the Arcade menu.")
        return play_choice()

    return play_choice


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

    arcade = play_acd(args.name)
    arcade()
