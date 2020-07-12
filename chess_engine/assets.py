import os
from collections import namedtuple
import board

CHESS_SET_NAME = "chess_green"

ASSET_ROOT = os.path.abspath(os.path.join(
    os.getcwd(), "../assets/Pixel_Art_Chess_DevilsWorkshop_V03", CHESS_SET_NAME))

BOARD = os.path.join(ASSET_ROOT, "board.png")


Sprites = namedtuple('Sprites', 'board pieces')

def piece_asset_name(piece):
    return piece.type.name

PieceAssetPair = namedtuple('PieceAssets', 'piece dark light')

def load_assets(pyglet):
    pyglet.resource.path = [ASSET_ROOT]
    pieces = {}
    for piece in board.all_pieces():
        name = f'{piece.colour.name.lower()}_{piece.type.name.lower()}.png'
        image = pyglet.resource.image(name)
        pieces[piece] = image

    board_image = pyglet.resource.image('board.png')

    return Sprites(board_image, pieces)
