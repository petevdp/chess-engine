import pyglet
from pyglet import gl
import assets
import board

window = None
history = []
background_batch = None
piece_sprites = {}
pieces_batch = None

def main(width=800, height=800):
    global window, history, background_batch, pieces_batch
    window = pyglet.window.Window(width=width, height=height)
    pieces_batch = pyglet.graphics.Batch()
    background_batch = pyglet.graphics.Batch()

    asset_map = assets.load_assets(pyglet)

    board_sprite = pyglet.sprite.Sprite(asset_map.board, batch=background_batch)
    for piece, image in asset_map.pieces.items():
        piece_sprite = pyglet.sprite.Sprite(image, batch=pieces_batch)
        piece_sprites[piece] = piece_sprite

    starting_board = board.create_board()

    for coords, piece in starting_board.items():
        image = asset_map.pieces[piece]
        x,y = coords
        cell_size = 480 / 8
        pyglet.sprite.Sprite(image, batch=pieces_batch)

    @window.event
    def on_draw(self):
        self.clear()
        self.background_batch.draw()
        self.pieces_batch.draw()
    
    pyglet.app.run()

if __name__ == "__main__":
    main()