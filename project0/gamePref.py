games = ["Rainbow Six Siege", "Dead by Daylight", "Valorant", "Clash Royale"]
print("I like to play " + str(games[0]) + " " + str(games[1]) + " " + str(games[2]) + " " + str(games[3]))

new_game = input("What is your favorite game: ")

games.append(new_game)
print("We like to play " + str(games[0]) + " " + str(games[1]) + " " + str(games[2]) + " " + str(games[3]) + " " + str(new_game))
