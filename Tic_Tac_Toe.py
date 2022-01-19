def display_board(game_list):
    """Displays the game board"""
    print()
    print(f" {game_list[1]} | {game_list[2]} | {game_list[3]} ")
    print("-----------")
    print(f" {game_list[4]} | {game_list[5]} | {game_list[6]} ")
    print("-----------")
    print(f" {game_list[7]} | {game_list[8]} | {game_list[9]} ")
    print()


def take_position(game_list):
    while True:
        position = input("Enter the position (1-9): ")

        if position.isdigit():
            position = int(position)

            if position in list(range(1, 10)):
                if game_list[position] == " ":
                    return position
                else:
                    print("Sorry! the position is already filled up.")

            else:
                print("Please enter a valid position!")

        else:
            print("Please enter a number!")


def place_symbol(game_list, position, symbol):
    game_list[position] = symbol


def is_winner(game_list, symbol):
    if game_list[1] == game_list[2] == game_list[3] == symbol:
        return True
    elif game_list[4] == game_list[5] == game_list[6] == symbol:
        return True
    elif game_list[7] == game_list[8] == game_list[9] == symbol:
        return True
    elif game_list[1] == game_list[4] == game_list[7] == symbol:
        return True
    elif game_list[2] == game_list[5] == game_list[8] == symbol:
        return True
    elif game_list[3] == game_list[6] == game_list[9] == symbol:
        return True
    elif game_list[1] == game_list[5] == game_list[9] == symbol:
        return True
    elif game_list[3] == game_list[5] == game_list[7] == symbol:
        return True
    return False


def is_drawn(game_list):
    if " " in game_list:
        return False
    return True


def show_welcome_message():
    print("\nWELCOME TO TIC TAC TOE ULTRA PRO MAX 65\n")
    print("Please follow the board below to place your symbol in correct position")
    game_board = list(range(10))
    display_board(game_board)
    print()


def take_symbol():

    while True:
        user = input("What do you want to be? 'X' or 'O': ").lower()
        if user == "x" or user == "o":
            return user.upper()
        else:
            print("Select a valid symbol!")


def replay():
    users = input(
        "If you want to play again press 'Y' otherwise 'N': ").lower()
    return users == 'y'


if __name__ == "__main__":
    while True:

        show_welcome_message()
        game_list = [' ']*10

        first_player_symbol = take_symbol()
        if first_player_symbol == "O":
            second_player_symbol = "X"
        else:
            second_player_symbol = "O"
        print(f"{first_player_symbol} will go first\n")

        display_board(game_list)

        game_on = True
        while game_on:
            if is_drawn(game_list):
                game_on = False
                break
            elif is_winner(game_list, first_player_symbol):
                print(f"{first_player_symbol} win the game")
                game_on = False
                break
            elif is_winner(game_list, second_player_symbol):
                print(f"{second_player_symbol} win the game")
                game_on = False
                break

            print(f"{first_player_symbol}'s Turn")
            first_player_position = take_position(game_list)
            place_symbol(game_list, first_player_position, first_player_symbol)
            display_board(game_list)

            if is_drawn(game_list):
                game_on = False
                break
            elif is_winner(game_list, first_player_symbol):
                print(f"{first_player_symbol} win the game")
                game_on = False
                break
            elif is_winner(game_list, second_player_symbol):
                print(f"{second_player_symbol} win the game")
                game_on = False
                break

            print(f"{second_player_symbol}'s Turn")
            second_player_position = take_position(game_list)
            place_symbol(game_list, second_player_position,
                         second_player_symbol)
            display_board(game_list)

        if not replay():
            break
