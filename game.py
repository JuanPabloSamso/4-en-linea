class InLine:
    def __init__(self):
        self.board = [[' ' for _ in range(7)]for _ in range(6)]
        self.player = 1
        self.player1 = 'X'
        self.player2 = 'Y'
        self.winner = ' '

    def available(self, col):
        for row in range(5,-1,-1):
            if self.board [row][col] == ' ':
                return row

    def turn(self):
            if self.player == 1:
                self.player +=1
            else:
                self.player -= 1

    def throw_coin(self,col):
        if self.player == 1: 
            self.board[self.available(col)][col] = self.player1    
            self.turn()
        else:
            self.board[self.available(col)][col] = self.player2    
            self.turn()

    def check_col(self):
        for c in range(7):
            for r in range(3):
                if self.board[r][c] == self.player1 and self.board[r+1][c] == self.player1 and self.board[r+2][c] == self.player1 and self.board[r+3][c] == self.player1:
                    self.winner = 'Jugador 1'
                    return True
                elif self.board[r][c] == self.player2 and self.board[r+1][c] == self.player2 and self.board[r+2][c] == self.player2 and self.board[r+3][c] == self.player2:
                    self.winner = 'Jugador 2'
                    return True 
         

    def check_row(self):
        for r in range(6):
            for c in range(4):
                if self.board[r][c] == self.player1 and self.board[r][c+1] == self.player1 and self.board[r][c+2] == self.player1 and self.board[r][c+3] == self.player1:
                    self.winner = 'Jugador 1'
                    return True
                elif self.board[r][c] == self.player2 and self.board[r][c+1] == self.player2 and self.board[r][c+2] == self.player2 and self.board[r][c+3] == self.player2:
                    self.winner = 'Jugador 2'
                    return True
         
    def check_diag_down(self):
        for r in range(3):
            for c in range(4):
                if self.board[r][c] == self.player1 and self.board[r+1][c+1] == self.player1 and self.board[r+2][c+2] == self.player1 and self.board[r+3][c+3] == self.player1:
                    self.winner = 'Jugador 1'
                    return True
                elif self.board[r][c] == self.player2 and self.board[r+1][c+1] == self.player2 and self.board[r+2][c+2] == self.player2 and self.board[r+3][c+3] == self.player2:
                    self.winner = 'Jugador 2'
                    return True 

    def check_diag_up(self):
        for r in range(6):
            for c in range(4):
                if self.board[r][c] == self.player1 and self.board[r-1][c+1] == self.player1 and self.board[r-2][c+2] == self.player1 and self.board[r-3][c+3] == self.player1:
                    self.winner = 'Jugador 1'
                    return True
                elif self.board[r][c] == self.player2 and self.board[r-1][c+1] == self.player2 and self.board[r-2][c+2] == self.player2 and self.board[r-3][c+3] == self.player2:
                    self.winner = 'Jugador 2'
                    return True 

    def check_winner(self):
        if self.check_col() or self.check_row() or self.check_diag_down() or self.check_diag_up() == True:
            return True