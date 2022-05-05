#imports
import arcade
import math

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
SCREEN_TITLE = "Pong"
SCOREBOARD_SIZE = 50
SCOREBOARD_WIDTH = 100
CROP_X_PITCH_ADJUSTER = 8
CROP_Y_PITCH_ADJUSTER = 3
RADIUS = 10
SCALING = 1
PITCH_SCALING = 2.78
BALL_SCALING = 0.25
BALL_SPEED = 15
INITIAL_BALL_SPEED_ADJUSTER = 3
CORNER_TO_GOAL_RATIO_ON_PITCH = 4.67

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


        # Set up the empty sprite lists
        self.players_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.p1Score = 0
        self.p2Score = 0

        self.setup()

    def setup(self):
        """Get the game ready to play
        """

        # Set the background color
        #self.player = arcade.Sprite("data/Pitch.png", SCALING)
        #arcade.set_background_color(self.player)

        # Set up field
        self.field = arcade.Sprite("data/Pitch.png", PITCH_SCALING)
        self.field.center_y = self.height / 2
        self.field.left = 0
        self.all_sprites.append(self.field)
        # Set up the player
        self.player = arcade.Sprite("data/Neymar.tiff", SCALING)
        self.player.center_y = self.height / 2
        self.player.left = 0
        self.all_sprites.append(self.player)

        self.player2 = arcade.Sprite("data/Messi.tiff", SCALING)
        self.player2.center_y = self.height / 2
        self.player2.right = SCREEN_WIDTH
        self.all_sprites.append(self.player2)
        # Set up a the ball
        self.ball = arcade.Sprite("data/Ball.png", BALL_SCALING)
        self.ball.center_y = self.height / 2
        self.ball.left = SCREEN_WIDTH/2
        self.ball.change_x = BALL_SPEED/INITIAL_BALL_SPEED_ADJUSTER
        self.all_sprites.append(self.ball)

        ball_angle = 0

    def on_key_press(self, symbol, modifiers):
        """Handle user keyboard input
        Q: Quit the game
        P: Pause/Unpause the game
        I/J/K/L: Move Up, Left, Down, Right
        Arrows: Move Up, Left, Down, Right

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()


        if symbol == arcade.key.W:
            self.player.change_y = 5

        if symbol == arcade.key.UP:
            self.player2.change_y = 5

        if symbol == arcade.key.S:
            self.player.change_y = -5

        if symbol == arcade.key.DOWN:
            self.player2.change_y = -5

    def on_key_release(self, symbol: int, modifiers: int):
        """Undo movement vectors when movement keys are released

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if (
                symbol == arcade.key.W
                or symbol == arcade.key.S
        ):
            self.player.change_y = 0
        if (
                symbol == arcade.key.UP
                or symbol == arcade.key.DOWN
        ):
            self.player2.change_y = 0

    def on_collide_with_player(self, player, speed):
        relativeIntersectY = (player.center_y) - self.ball.center_y
        normalizedRelativeIntersectionY = (relativeIntersectY / (player.height / 2))
        bounceAngle = normalizedRelativeIntersectionY * BALL_SPEED * math.pi/12
        self.ball.change_x = speed * math.cos(bounceAngle)
        self.ball.change_y = speed * math.sin(bounceAngle)

    def on_collide_with_player2(self, player, speed):
        relativeIntersectY = (player.center_y) - self.ball.center_y
        normalizedRelativeIntersectionY = (relativeIntersectY / (player.height / 2))
        bounceAngle = normalizedRelativeIntersectionY * BALL_SPEED * math.pi / 12
        self.ball.change_x = speed * math.cos(bounceAngle)
        self.ball.change_y = speed * -math.sin(bounceAngle)

    def on_draw(self):
        """Called whenever you need to draw your window
        """

        # Clear the screen and start drawing
        arcade.start_render()
        #Draw sprites
        self.all_sprites.draw()
        arcade.draw_text(str(self.p1Score) + " : " + str(self.p2Score), SCREEN_WIDTH/2 - SCOREBOARD_WIDTH + SCOREBOARD_SIZE/2 + CROP_X_PITCH_ADJUSTER, SCREEN_HEIGHT/2 - SCOREBOARD_SIZE/2 + CROP_Y_PITCH_ADJUSTER, arcade.color.BLACK, SCOREBOARD_SIZE, SCOREBOARD_WIDTH, 'left')

    def on_update(self, delta_time: float):
        """Update the positions and statuses of all game objects
        If paused, do nothing

        Arguments:
            delta_time {float} -- Time since the last update
        """

        # If paused, don't update anything
        #if self.paused:
            #return

        # Update everything
        self.all_sprites.update()

        # Collide with player
        if self.player.collides_with_sprite(self.ball):
            print("Collide 1")
            self.on_collide_with_player(self.player, BALL_SPEED)
        if self.player2.collides_with_sprite(self.ball):
            print("Collide 2")
            self.on_collide_with_player2(self.player2, -BALL_SPEED)
        if self.ball.top >= self.height or self.ball.bottom <= 0:
            self.ball.change_y = - self.ball.change_y
        if self.ball.right >= self.width and self.ball.bottom >= SCREEN_HEIGHT/CORNER_TO_GOAL_RATIO_ON_PITCH and self.ball.top <= SCREEN_HEIGHT - SCREEN_HEIGHT/CORNER_TO_GOAL_RATIO_ON_PITCH:
            self.ball.center_x = self.width/2
            self.ball.center_y = self.height / 2
            self.ball.change_x = BALL_SPEED/CORNER_TO_GOAL_RATIO_ON_PITCH
            self.ball.change_y = 0
            print("Player 1 scores!")
            self.p1Score += 1
        else:
            if self.ball.right >= self.width:
                self.ball.change_x = - self.ball.change_x
        if self.ball.left <= 0 and self.ball.bottom >= SCREEN_HEIGHT/CORNER_TO_GOAL_RATIO_ON_PITCH and self.ball.top <= SCREEN_HEIGHT - SCREEN_HEIGHT/CORNER_TO_GOAL_RATIO_ON_PITCH:
            self.ball.center_x = self.width/2
            self.ball.center_y = self.height / 2
            self.ball.change_x = -BALL_SPEED/3
            self.ball.change_y = 0
            print("Player 2 scores!")
            self.p2Score += 1
        else:
            if self.ball.left <= 0:
                self.ball.change_x = - self.ball.change_x


        if self.ball.change_x == 0:
            self.ball.change_x = BALL_SPEED
            self.ball.change_y = 0
        # Keep the player on screen

        for sprite in self.all_sprites:
            if sprite.top > self.height:
                sprite.top = self.height
            if sprite.bottom < 0:
                sprite.bottom = 0
            sprite.center_x = int(
                sprite.center_x + sprite.change_x * delta_time
            )
            sprite.center_y = int(
                sprite.center_y + sprite.change_y * delta_time
            )

if __name__ == '__main__':
    game = Pong(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
