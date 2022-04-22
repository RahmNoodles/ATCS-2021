#imports
import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Pong"
RADIUS = 10

# Open the window
arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

# Set the background color
arcade.set_background_color(arcade.color.BLACK)

# Clear the screen and start drawing
arcade.start_render()

# Draw a blue circle
arcade.draw_circle_filled(
    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, RADIUS, arcade.color.WHITE
)

# Finish drawing
arcade.finish_render()

# Display everything
arcade.run()