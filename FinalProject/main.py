#imports
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Pong"
RADIUS = 10
SCALING = 2.0
PITCH_SCALING = 2.78

class Pong(arcade.Window):
    """Space Shooter side scroller game
    Player starts on the left, enemies appear on the right
    Player can move anywhere, but not off screen
    Enemies fly to the left at variable speed
    Collisions end the game
    """

    def __init__(self, width, height, title):
        """Initialize the game
        """
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLUE)

        # Set up the empty sprite lists
        self.players_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()

        self.setup()

    def setup(self):
        """Get the game ready to play
        """

        # Set the background color
        #self.player = arcade.Sprite("data/Pitch.png", SCALING)
        #arcade.set_background_color(self.player)

        # Set up the player
        self.player = arcade.Sprite("data/Neymar.tiff", SCALING)
        self.player.center_y = self.height / 2
        self.player.left = 0
        self.all_sprites.append(self.player)

        self.player = arcade.Sprite("data/Messi.tiff", SCALING)
        self.player.center_y = self.height / 2
        self.player.left = SCREEN_WIDTH - 217
        self.all_sprites.append(self.player)

    def on_draw(self):
        """Called whenever you need to draw your window
        """

        # Clear the screen and start drawing
        arcade.start_render()
        #Draw sprites
        self.all_sprites.draw()
        # Draw a blue circle
        arcade.draw_circle_filled(
            SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, RADIUS, arcade.color.BLUE
        )

if __name__ == '__main__':
    game = Pong(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
