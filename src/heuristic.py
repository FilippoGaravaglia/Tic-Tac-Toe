# heuristic.py

"""
<summary>
Valuta lo stato corrente della board di Tic-Tac-Toe restituendo un punteggio numerico.
</summary>
<param name="board">
  Lista di 9 elementi ('X', 'O' o ' ') che rappresentano la board.
</param>
<returns>
  Intero: punteggio calcolato (positivo favorisce X, negativo favorisce O).
</returns>
"""
def evaluate_board(board):
    score = 0
    lines = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Righe
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colonne
        [0, 4, 8], [2, 4, 6]              # Diagonali
    ]

    for line in lines:
        x_count = sum(1 for pos in line if board[pos] == 'X')
        o_count = sum(1 for pos in line if board[pos] == 'O')

        # Applica i punteggi secondo i criteri dati
        if x_count == 3:
            score += 100
        elif x_count == 2 and o_count == 0:
            score += 10
        elif x_count == 1 and o_count == 0:
            score += 1
        elif o_count == 3:
            score -= 100
        elif o_count == 2 and x_count == 0:
            score -= 10
        elif o_count == 1 and x_count == 0:
            score -= 1

    return score
