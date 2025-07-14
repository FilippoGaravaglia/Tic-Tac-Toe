# main.py

from src.tic_tac_toe import TicTacToe

"""
<summary>
Gestisce il ciclo di gioco del Tic-Tac-Toe:
  - mostra il tabellone;
  - legge e valida la mossa dell'utente;
  - verifica vittoria o pareggio;
  - esegue la mossa del computer.
</summary>
<returns></returns>
"""
def play_game():
    game = TicTacToe()
    while True:
        game.print_board()

        # Mossa del giocatore
        user_move = int(input("Inserisci la posizione (1-9): ")) - 1
        if not game.make_move(user_move, 'O'):
            print("Posizione non valida. Riprova.")
            continue

        if game.is_winner('O'):
            game.print_board()
            print("Hai vinto!")
            break

        if ' ' not in game.board:
            game.print_board()
            print("Pareggio!")
            break

        # Mossa del computer
        computer_move = game.best_move()
        game.make_move(computer_move, 'X')

        if game.is_winner('X'):
            game.print_board()
            print("Il computer ha vinto!")
            break

        if ' ' not in game.board:
            game.print_board()
            print("Pareggio!")
            break

if __name__ == "__main__":
    play_game()
