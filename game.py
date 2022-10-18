import arcade


# Global 

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Board game zone"

# game class

class BoardGames(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        
        arcade.set_background_color(arcade.color.AMAZON)
    def setup(self):
        """ Set up the game variables. Call to re-start the game. """
        # Create your sprites and sprite lists here
        pass

    def on_draw(self):
        """
        Render the screen.
        """

        # This command should happen before we start drawing. It will clear
        # the screen to the background color, and erase what we drew last frame.
        self.clear()

        # Call draw() on all your sprite lists below

def main():
    """ Main function """
    game = BoardGames(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()


if __name__ == "__main__":
    main()