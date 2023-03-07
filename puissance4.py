# Initialisation du plateau de jeu
ROWS = 6
COLS = 7
board = [[' ' for j in range(COLS)] for i in range(ROWS)]

# Affichage du plateau de jeu
def print_board():
    print('  '.join(str(i) for i in range(COLS)))
    for i in range(ROWS):
        print('| ' + ' | '.join(board[i]) + ' |')

# Vérification si une colonne est pleine
def is_column_full(col):
    return board[0][col] != ' '

# Ajout d'un jeton dans une colonne
def drop_token(col, token):
    for i in range(ROWS-1, -1, -1):
        if board[i][col] == ' ':
            board[i][col] = token
            return True
    return False

# Vérification si une colonne contient une combinaison gagnante
def is_winning_column(col, token):
    for i in range(ROWS-3):
        if board[i][col] == token and board[i+1][col] == token and board[i+2][col] == token and board[i+3][col] == token:
            return True
    return False

# Vérification si une ligne contient une combinaison gagnante
def is_winning_row(row, token):
    for j in range(COLS-3):
        if board[row][j] == token and board[row][j+1] == token and board[row][j+2] == token and board[row][j+3] == token:
            return True
    return False

# Vérification si une diagonale contient une combinaison gagnante
def is_winning_diagonal(token):
    # Vérification des diagonales de la forme '\'
    for i in range(ROWS-3):
        for j in range(COLS-3):
            if board[i][j] == token and board[i+1][j+1] == token and board[i+2][j+2] == token and board[i+3][j+3] == token:
                return True
    # Vérification des diagonales de la forme '/'
    for i in range(3, ROWS):
        for j in range(COLS-3):
            if board[i][j] == token and board[i-1][j+1] == token and board[i-2][j+2] == token and board[i-3][j+3] == token:
                return True
    return False

# Vérification si le jeu
