# tic_tac_toe.py

from heuristic import evaluate_board

class TicTacToe:
    """
    <summary>
    Inizializza una nuova board vuota di 9 posizioni.
    </summary>
    <returns>None</returns>
    """
    def __init__(self):
        self.board = [' ' for _ in range(9)]

    """
    <summary>
    Stampa la board attuale su console.
    </summary>
    <returns>None</returns>
    """
    def print_board(self):
        for i in range(3):
            print(" | ".join(self.board[i*3:(i+1)*3]))
            if i < 2:
                print("---------")
    """
    <summary>
    Tenta di piazzare il simbolo del giocatore in una posizione.
    </summary>
    <param name="position">Indice (0-8) della casella</param>
    <param name="player">'X' o 'O'</param>
    <returns>True se la mossa è valida e applicata, False altrimenti</returns>
    """
    def make_move(self, position, player):
        if  position <= len(self.board) and self.board[position] == ' ':
            self.board[position] = player
            return True
        return False

    """
    <summary>
    Verifica se il giocatore indicato ha una combinazione vincente.
    </summary>
    <param name="player">'X' o 'O'</param>
    <returns>True se il giocatore ha vinto, False altrimenti</returns>
    """
    def is_winner(self, player):
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]
        ]
        return any(all(self.board[pos] == player for pos in combo) for combo in winning_combinations)

    """
    <summary>
    Algoritmo Minimax con profondità limitata per calcolare il valore della board.
    </summary>
    <param name="depth">Livello corrente di profondità della ricorsione</param>
    <param name="is_maximizing">True se è il turno del max, False per il min</param>
    <returns>Punteggio ottimale per la configurazione corrente</returns>
    """
    def minimax(self, depth, is_maximizing):
        if self.is_winner('X'):
            return 100
        elif self.is_winner('O'):
            return -100
        elif ' ' not in self.board or depth == 2:
            return evaluate_board(self.board)

        best_score = float('-inf') if is_maximizing else float('inf')
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'X' if is_maximizing else 'O'
                score = self.minimax(depth + 1, not is_maximizing)
                self.board[i] = ' '
                best_score = max(best_score, score) if is_maximizing else min(best_score, score)
        return best_score

    """
    <summary>
    Determina la migliore mossa per 'X' usando Minimax.
    </summary>
    <returns>Indice (0-8) della cella migliore</returns>
    """
    def best_move(self):
        best_score = float('-inf')
        move = None
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'X'
                score = self.minimax(1, False)
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    move = i
        return move
