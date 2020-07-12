from enum import Enum
from collections import namedtuple


class PieceType(Enum):
    PAWN = 0
    KNIGHT = 1
    BISHOP = 2
    ROOK = 3
    QUEEN = 4
    KING = 5


class Colour(Enum):
    WHITE = 0
    BLACK = 1


Piece = namedtuple('Piece', 'type colour')


def all_pieces():
    pieces = []
    for piece_type in list(PieceType):
        for colour in list(Colour):
            pieces.append(Piece(piece_type, colour))
    return pieces


def create_board():
    white_pieces = {
        **{(i, 1): PieceType.PAWN for i in range(8)},
        (0, 0): PieceType.ROOK,
        (1, 0): PieceType.KNIGHT,
        (2, 0): PieceType.BISHOP,
        (3, 0): PieceType.QUEEN,
        (4, 0): PieceType.KING,
        (5, 0): PieceType.BISHOP,
        (6, 0): PieceType.KNIGHT,
        (7, 0): PieceType.ROOK,
    }

    black_pieces = {(c[0], mirror(c[1])): v for c, v in white_pieces.items()}

    return {
        **{k: Piece(t, Colour.WHITE) for k, t in white_pieces.items()},
        **{k: Piece(t, Colour.BLACK) for k, t in black_pieces.items()}
    }


def mirror(num, size=8):
    middle = size // 2

    if num > middle:
        m_num = middle - (num - middle) - 1
    else:
        m_num = middle + (middle - num) - 1
    return m_num

class BoardHistory:
    def __init__(self):
        self.history = [create_board()]

    def make_move(self):
        pass

    def curr_board(self):
        return self.history[-1]