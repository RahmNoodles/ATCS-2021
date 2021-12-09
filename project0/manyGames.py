games = ["Rainbow Six Siege", "Dead by Daylight", "Valorant", "Clash Royale"]
print("I like to play " + str(games[0]) + " " + str(games[1]) + " " + str(games[2]) + " " + str(games[3]))

new_game = input("What is your favorite game: ")

games.append(new_game)

# Start a loop that will run until the user enters 'quit'.
while new_game != 'quit':
    # Ask the user for a name.
    new_game = input("What is your favorite game: , or enter 'quit': ")

    # Add the new name to our list.
    if new_game != 'quit':
        games.append(new_game)

games.append(new_game)
print("We like to play ")
for i in games:
    print(i)

