import random

class Player:
    def __init__(self, symbol):
        self.symbol = symbol
        self.name = self.generate_random_name()

    def generate_random_name(self):
        names = ["Ania", "Tomek", "Piotrek", "Zosia", "Marcin", "Kasia"]
        surnames = ["Kowalska", "Nowak", "Zdun", "Majewska", "Wiśniewski", "Lis"]
        return f"{random.choice(names)} {random.choice(surnames)}"
    
player_X = Player('X')
player_O = Player('O')


# Funkcja do wyświetlania planszy
def print_board(board):
    for i in range(0, 9, 3):
        print("|".join(board[i:i + 3]))
        if i < 6:
            print("-----")

# Funkcja do sprawdzania warunków wygranej
def check_winner(board, player):
    win_conditions = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Poziomo
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Pionowo
        [0, 4, 8], [2, 4, 6]              # Skos
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Funkcja do ruchu gracza
def player_move(board, current_player):
    while True:
        try:
            move = int(input(f"{current_player.name}, wybierz pole (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                return move
            else:
                print("To pole jest już zajęte lub wybierz liczbę z zakresu 1-9.")
        except ValueError:
            print("Wprowadź liczbę.")

def player_move2(board):
    while True:
        try:
            move = int(input(f"{current_player.name}, wybierz pole (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                return move
            else:
                print("To pole jest już zajęte lub wybierz liczbę z zakresu 1-9.")
        except ValueError:
            print("Wprowadź liczbę.")

# Funkcja do ruchu komputera
def computer_move(board):
    available_moves = [i for i, val in enumerate(board) if val == ' ']
    return random.choice(available_moves)

# Funkcja do zmiany gracza
def switch_player(current_player):
    return player_O if current_player == player_X else player_X

# Funkcja do inicjalizacji gry
def initialize_game():
    global board
    global current_player
    board = [' '] * 9
    current_player = 'X'

# Funkcja główna gry
def play_game1():
    initialize_game()
    current_player = player_X
    
    while True:
        print_board(board)

        if current_player == player_X:
            move = player_move(board, current_player)
        else:
            move = computer_move(board)

        board[move] = current_player.symbol

        if check_winner(board, current_player.symbol):
            print_board(board)
            print(f"{current_player.name} wygrał!")
            break

        if ' ' not in board:
            print_board(board)
            print("Remis!")
            break

        current_player = switch_player(current_player)

def play_game2():
    initialize_game()
    current_player = player_X
    
    while True:
        print_board(board)

        move = player_move(board, current_player)
        board[move] = current_player.symbol

        if check_winner(board, current_player.symbol):
            print_board(board)
            print(f"{current_player.name} wygrał!")
            break

        if ' ' not in board:
            print_board(board)
            print("Remis!")
            break

        current_player = switch_player(current_player)

# Funkcja do obsługi menu
def main_menu():
    while True:
        print("====Menu====")
        print("1. Gra z innym człowiekiem")
        print("2. Gra z komputerem")
        print("3. Wyjście")
        
        choice = input("Wybierz opcję: ")

        match choice:
            case '1':
                play_game1()
            case '2':
                play_game2()
            case '3':
                print("Do widzenia!")
                break
            case _:
                print("Nieprawidłowy wybór. Wybierz ponownie.")

if __name__ == "__main__":
    main_menu()

