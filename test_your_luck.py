"""Probability game by Aqsa Shoaib (original project: January 12, 2025)."""

import random


def flip_coin():
    """Return Heads or Tails with equal probability."""
    return random.choice(("Heads", "Tails"))


def roll_die(times):
    """Roll a die once or twice, keeping the highest roll."""
    return max(random.randint(1, 6) for _ in range(times))


def spin_spinner():
    """Choose an equally likely spinner outcome."""
    return random.choice(("LOCKED", "ROLL", "NOTHING"))


def check_win(number):
    """Determine whether the final die number wins."""
    return number >= 4


def play_round():
    """Simulate a coin flip, initial roll, spinner, and result."""
    coin = flip_coin()
    number = roll_die(1 if coin == "Heads" else 2)
    spinner = spin_spinner()
    if spinner == "ROLL":
        number = roll_die(1)
    elif spinner == "NOTHING":
        number = 1
    return check_win(number)


def get_round_count():
    """Read a valid positive number of simulation rounds."""
    while True:
        try:
            rounds = int(input("How many rounds would you like to simulate? "))
            if rounds > 0:
                return rounds
        except ValueError:
            pass
        print("Please enter a whole number greater than zero.")


def main():
    """Simulate rounds and show the observed winning percentage."""
    print("TEST YOUR LUCK")
    print("Heads: roll once. Tails: roll twice and keep the higher result.")
    print("The spinner then LOCKS your result, ROLLS again, or sets it to 1.")
    print("A final roll of 4, 5, or 6 is a win.\n")
    rounds = get_round_count()
    wins = sum(play_round() for _ in range(rounds))
    print(f"\nTotal rounds: {rounds}")
    print(f"Total wins: {wins}")
    print(f"Total losses: {rounds - wins}")
    print(f"Observed win rate: {wins / rounds:.2%}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGame closed.")
