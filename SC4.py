
#Name:Adrian silver
#Class: 5th Hour
#Assignment: SC4

#You have been transferred to a new team working on a mobile game that allows you to dress up a
#model and rate other models in a "Project Runway" style competition.

#They want to start prototyping the rating system and are asking you to make it.
#This prototype needs to allow the user to input the number of players, let each player rate
#a single model from 1 to 5, and then give the average score of all of the ratings.

num_players = int(input("Enter the number of players: "))

total = 0

for player in range(1, num_players + 1):
    rating = int(input("Player " + str(player) + ", enter a rating (1-5): "))

    while rating < 1 or rating > 5:
        print("Invalid rating. Please enter a number from 1 to 5.")
        rating = int(input("Enter your rating: "))

    total += rating

average = total / num_players
print("Total score:", total)
