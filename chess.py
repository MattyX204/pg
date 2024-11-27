from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
       
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):

        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_position):
        self.__position = new_position

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
      
        return []

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
     
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
     
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
      
        row, col = self.position
        moves = []
   
        for i in range(1, 8):
            new_pos = (row + i, col + i)
            if self.is_position_on_board(new_pos):
                moves.append(new_pos)
            else:
                break
      
        for i in range(1, 8):
            new_pos = (row + i, col - i)
            if self.is_position_on_board(new_pos):
                moves.append(new_pos)
            else:
                break
    
        for i in range(1, 8):
            new_pos = (row - i, col + i)
            if self.is_position_on_board(new_pos):
                moves.append(new_pos)
            else:
                break
       
        for i in range(1, 8):
            new_pos = (row - i, col - i)
            if self.is_position_on_board(new_pos):
                moves.append(new_pos)
            else:
                break
        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):

        row, col = self.position
        moves = []
        for i in range(col + 1, 9):
            moves.append((row, i))
        for i in range(1, col):
            moves.append((row, i))
        for i in range(row + 1, 9):
            moves.append((i, col))
        for i in range(1, row):
            moves.append((i, col))
        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        return Bishop.possible_moves(self) + Rook.possible_moves(self)

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                new_pos = (row + i, col + j)
                if self.is_position_on_board(new_pos):
                    moves.append(new_pos)
        return moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    piece = Knight("black", (1, 2))
    print(piece)
    print(piece.possible_moves())