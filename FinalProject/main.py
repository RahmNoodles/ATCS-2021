# Zain Rahman's Pong Game
# Teacher: Ms. Namasivayam
# Due Date: May 10, 2022
#
# Source[s] used: https://realpython.com/arcade-python-game-framework/

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
SCALING = .5
PITCH_SCALING = 2.78
BALL_SCALING = 0.25
BALL_SPEED = 15
PLAYER_SPEED = 5
INITIAL_BALL_SPEED_ADJUSTER = 3
CORNER_TO_GOAL_RATIO_ON_PITCH = 4.67
DEFUALT_FONT_SIZE = 10
SCORE_TO_WIN = 10

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

        # Instance variables
        self.AIDeadband = 75
        self.difficulty = "Easy"
        self.state = 0

        self.setup()

    def setup(self):
        """Get the game ready to play
        """
        # Set up the empty sprite lists
        self.players_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()
        self.ball_list = arcade.SpriteList()
        self.all_sprites = arcade.SpriteList()
        self.p1Score = 0
        self.p2Score = 0
        self.AIUp = False
        self.AIDown = False
        self.twoPlayer = False

        # Set up field
        self.field = arcade.Sprite("data/Pitch.png", PITCH_SCALING)
        self.field.center_y = self.height / 2
        self.field.left = 0
        self.all_sprites.append(self.field)
        # Set up the players
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
        self.ball.change_y = 0
        self.ball.change_x = BALL_SPEED/INITIAL_BALL_SPEED_ADJUSTER
        self.all_sprites.append(self.ball)

        ball_angle = 0

    def on_key_press(self, symbol, modifiers):
        """Handle user keyboard input
        Q: Quit the game
        R: Resets the game
        W/S: Player 1 moves up, Player 1 moves down
        Arrows: Player 2 moves up, Player 2 moves down (Only if twoPlayer)

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()

        # Adds movement to paddles
        if self.state == 1:
            if symbol == arcade.key.W:
                self.player.change_y = PLAYER_SPEED

            if symbol == arcade.key.S:
                self.player.change_y = -PLAYER_SPEED
            # Checks PvP before allowing controls
            if self.twoPlayer:
                if symbol == arcade.key.UP:
                    self.player2.change_y = PLAYER_SPEED

                if symbol == arcade.key.DOWN:
                    self.player2.change_y = -PLAYER_SPEED

        if self.state == 0:
            # Easy difficulty setup
            if symbol == arcade.key.KEY_1:
                self.AIDeadband = 75
                self.difficulty = "Easy"
                self.state = 1
                self.setup()
            # Medium difficulty setup
            if symbol == arcade.key.KEY_2:
                self.AIDeadband = 10
                self.difficulty = "Medium"
                self.state = 1
                self.setup()
            # Hard difficulty setup
            if symbol == arcade.key.KEY_3:
                self.AIDeadband = 0
                self.difficulty = "Hard"
                self.state = 1
                self.setup()
            # PvP game-mode setup
            if symbol == arcade.key.KEY_4:
                self.setup()
                self.twoPlayer = True
                self.difficulty = "PvP"
                self.state = 1
        # Resets game
        if symbol == arcade.key.R:
            self.state = 0

    def on_key_release(self, symbol: int, modifiers: int):
        """Undo movement vectors when movement keys are released

        Arguments:
            symbol {int} -- Which key was pressed
            modifiers {int} -- Which modifiers were pressed
        """
        if self.state == 1:
            if (
                    symbol == arcade.key.W
                    or symbol == arcade.key.S
            ):
                self.player.change_y = 0
            if self.twoPlayer:
                if symbol == arcade.key.UP or symbol == arcade.key.DOWN:
                    self.player2.change_y = 0


    def AI_input_update(self):
        # If the ball is above or below the player, move player in the correct direction (towards the ball)
        if self.AIUp:
            self.player2.change_y = PLAYER_SPEED

        if self.AIDown:
            self.player2.change_y = -PLAYER_SPEED

        if not self.AIUp and not self.AIDown:
            self.player2.change_y = 0

    def AI_position_update(self):
        # Check where the player is in correlation to ball and set values for AI.Up and AI.Down (whether ai player must go up or down)
        change_in_y = self.player2.center_y - self.ball.center_y
        if change_in_y > self.AIDeadband:
            self.AIDown = True
            self.AIUp = False
        elif change_in_y < - self.AIDeadband:
            self.AIUp = True
            self.AIDown = False

        else:
            self.AIUp = False
            self.AIDown = False


    def on_collide_with_player(self, player, speed):
        #Algorithm for when the ball collides with player 1
        relativeIntersectY = (player.center_y) - self.ball.center_y
        normalizedRelativeIntersectionY = (relativeIntersectY / (player.height / 2))
        bounceAngle = normalizedRelativeIntersectionY * BALL_SPEED * math.pi/12
        self.ball.change_x = speed * math.cos(bounceAngle)
        self.ball.change_y = speed * math.sin(bounceAngle)

    def on_collide_with_player2(self, player, speed):
        #Algorithm for when the ball collides with player 2
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

        # Draw text corresponding to each state as well as draw all sprites in state 1 and draw background to every state but 1
        # State 0 text and background
        if self.state == 0:
            arcade.set_background_color(arcade.color.BLACK)
            arcade.draw_text("CHOOSE DIFFICULTY:", self.width/2, self.height/2, arcade.color.WHITE, DEFUALT_FONT_SIZE*4, 'center', anchor_x="center", anchor_y="center")
            arcade.draw_text("EASY (PRESS 1) MEDIUM (PRESS 2) HARD (PRESS 3) 2-PLAYER (PRESS 4)", self.width / 2,
                             self.height / 2 - DEFUALT_FONT_SIZE*4, arcade.color.WHITE, DEFUALT_FONT_SIZE * 2, 'center', anchor_x="center",
                             anchor_y="center")
        # State 1 text and sprite drawing
        if self.state == 1:
            self.all_sprites.draw()
            # Difficulty tracker
            arcade.draw_text("Difficulty: " + str(self.difficulty), 0, SCREEN_HEIGHT, arcade.color.BLACK, DEFUALT_FONT_SIZE, align="left", anchor_y= "top")
            # Drawing scoreboard
            arcade.draw_text(str(self.p1Score) + " : " + str(self.p2Score), SCREEN_WIDTH/2 - SCOREBOARD_WIDTH + SCOREBOARD_SIZE/2 + CROP_X_PITCH_ADJUSTER, SCREEN_HEIGHT/2 - SCOREBOARD_SIZE/2 + CROP_Y_PITCH_ADJUSTER, arcade.color.BLACK, SCOREBOARD_SIZE, SCOREBOARD_WIDTH, 'left')
        # State 2 text and background
        if self.state == 2:
            arcade.set_background_color(arcade.color.BLACK)
            # Checks PvP
            if self.twoPlayer:
                arcade.draw_text("Player 1 Wins!", self.width / 2, self.height / 2, arcade.color.WHITE,
                                 DEFUALT_FONT_SIZE * 4, 'center', anchor_x="center", anchor_y="center")
            else:
                arcade.draw_text("You Win!", self.width / 2, self.height / 2, arcade.color.WHITE,
                                 DEFUALT_FONT_SIZE * 4, 'center', anchor_x="center", anchor_y="center")
        # State 3 text and background
        if self.state == 3:
            arcade.set_background_color(arcade.color.BLACK)
            # Checks PvP
            if self.twoPlayer:
                arcade.draw_text("Player 2 Wins!", self.width / 2, self.height / 2, arcade.color.WHITE,
                                 DEFUALT_FONT_SIZE * 4, 'center', anchor_x="center", anchor_y="center")
            else:
                arcade.draw_text("You Lose!", self.width / 2, self.height / 2, arcade.color.WHITE,
                                 DEFUALT_FONT_SIZE * 4, 'center', anchor_x="center", anchor_y="center")
    def on_update(self, delta_time: float):
        """Update the positions and statuses of all game objects

        Arguments:
            delta_time {float} -- Time since the last update
        """
        # Check win
        if self.state == 1:
            if self.p1Score >= SCORE_TO_WIN:
                self.state = 2
            if self.p2Score >= SCORE_TO_WIN:
                self.state = 3

            # Update everything
            self.all_sprites.update()
            #AI
            if not self.twoPlayer:
                self.AI_position_update()
                self.AI_input_update()
            # Collide with player (Also checks to make sure ball isn't stuck)
            if self.player.collides_with_sprite(self.ball):
                self.on_collide_with_player(self.player, BALL_SPEED)
                if self.ball.bottom <= self.player.top and self.ball.top >= self.player.bottom and self.ball.right < self.player.right:
                    self.ball.left = self.player.width + 10
                    if self.ball.bottom <= 0:
                        self.ball.bottom = 10
                    if self.ball.top >= self.height:
                        self.ball.top = self.height - 10
                    self.ball.change_x = BALL_SPEED * 2 /3
            if self.player2.collides_with_sprite(self.ball):
                self.on_collide_with_player2(self.player2, -BALL_SPEED)
                if self.ball.bottom <= self.player2.top and self.ball.top >= self.player2.bottom and self.ball.left > self.player2.left:
                    if self.ball.bottom <= 0:
                        self.ball.bottom = 10
                    if self.ball.top >= self.height:
                        self.ball.top = self.height - 10
                    self.ball.right = self.width - self.player2.width - 10
                    self.ball.change_x = -BALL_SPEED * 2 /3
            # Bounce of top or bottom wall
            if self.ball.top >= self.height or self.ball.bottom <= 0:
                self.ball.change_y = - self.ball.change_y
            # Check if ball is in Player 2's goal
            if self.ball.right >= self.width and self.ball.bottom >= SCREEN_HEIGHT/CORNER_TO_GOAL_RATIO_ON_PITCH and self.ball.top <= SCREEN_HEIGHT - SCREEN_HEIGHT/CORNER_TO_GOAL_RATIO_ON_PITCH:
                self.ball.center_x = self.width/2
                self.ball.center_y = self.height / 2
                self.ball.change_x = BALL_SPEED/CORNER_TO_GOAL_RATIO_ON_PITCH
                self.ball.change_y = 0
                #Player 1 score tally increased
                self.p1Score += 1
            else:
                # Ball bounces off right wall
                if self.ball.right >= self.width:
                    self.ball.change_x = -BALL_SPEED * 2 /3
            # Check if ball is in Player 1's goal
            if self.ball.left <= 0 and self.ball.bottom >= SCREEN_HEIGHT/CORNER_TO_GOAL_RATIO_ON_PITCH and self.ball.top <= SCREEN_HEIGHT - SCREEN_HEIGHT/CORNER_TO_GOAL_RATIO_ON_PITCH:
                self.ball.center_x = self.width/2
                self.ball.center_y = self.height / 2
                self.ball.change_x = -BALL_SPEED/3
                self.ball.change_y = 0
                #Player 2 score tally increased
                self.p2Score += 1
            else:
                # Ball bounces off left wall
                if self.ball.left <= 0:
                    self.ball.change_x = BALL_SPEED * 2 /3

            # When ball is stuck moving vertically, reset ball
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
