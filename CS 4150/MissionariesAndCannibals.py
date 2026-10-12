def is_safe(missionaries, cannibals):
    return missionaries == 0 or missionaries >= cannibals


def is_valid_move(available_m, available_c, move_m, move_c):
    passengers = move_m + move_c

    return (
        1 <= passengers <= 2
        and 0 <= move_m <= available_m
        and 0 <= move_c <= available_c
    )


def get_move(available_m, available_c, direction):
    valid_move = False
    move_m = 0
    move_c = 0

    while not valid_move:
        print(f"\n{direction}")

        try:
            move_m = int(input("Enter number of Missionaries travel => "))
            move_c = int(input("Enter number of Cannibals travel => "))

            valid_move = is_valid_move(
                available_m,
                available_c,
                move_m,
                move_c
            )

            if not valid_move:
                print("Invalid move. The boat can carry 1 or 2 people.")
                print("You cannot move more people than are on this side.")

        except ValueError:
            print("Please enter whole numbers.")

    return move_m, move_c


def display_state(left_m, left_c, right_m, right_c, boat):
    left_side = " ".join(["M"] * left_m + ["C"] * left_c)
    right_side = " ".join(["M"] * right_m + ["C"] * right_c)

    print(f"\n{left_side:<12} | {boat} | {right_side}")


def play_game():
    left_m = 3
    left_c = 3
    right_m = 0
    right_c = 0
    attempts = 0

    display_state(left_m, left_c, right_m, right_c, "-->")

    game_over = False

    while not game_over:
        move_m, move_c = get_move(
            left_m,
            left_c,
            "Left side -> Right side"
        )

        left_m -= move_m
        left_c -= move_c
        right_m += move_m
        right_c += move_c
        attempts += 1

        display_state(left_m, left_c, right_m, right_c, "-->")

        if right_m == 3 and right_c == 3:
            print("\nYou won the game!")
            print(f"Total attempts: {attempts}")
            game_over = True
            continue

        if not is_safe(left_m, left_c) or not is_safe(right_m, right_c):
            print("\nCannibals eat missionaries!")
            print("You lost the game.")
            game_over = True
            continue

        move_m, move_c = get_move(
            right_m,
            right_c,
            "Right side -> Left side"
        )

        right_m -= move_m
        right_c -= move_c
        left_m += move_m
        left_c += move_c
        attempts += 1

        display_state(left_m, left_c, right_m, right_c, "<--")

        if not is_safe(left_m, left_c) or not is_safe(right_m, right_c):
            print("\nCannibals eat missionaries!")
            print("You lost the game.")
            game_over = True


def main():
    print("Move all missionaries and cannibals to the right side.\n")
    print("Rules:")
    print("1. The boat can carry at most two people.")
    print("2. Cannibals cannot outnumber missionaries.")
    print("3. The boat cannot cross with no people on board.")

    play_again = "y"

    while play_again == "y":
        play_game()

        play_again = input("\nWould you like to play again? (y/n): ").lower()

        while play_again not in ("y", "n"):
            print("Please enter y or n.")
            play_again = input("Would you like to play again? (y/n): ").lower()

    print("\nThanks for playing!")


if __name__ == "__main__":
    try:
        main()
    except EOFError:
        print("\nInput ended.")