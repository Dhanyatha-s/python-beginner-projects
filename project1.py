# PIG
# IS A GAME, WHEN WE ROLL A DICE AND HIT 2 WE GONNA ROLL TWO MORE TIMES, IF 5 5 MORE TIME..
# INCASE IF WE HIT 1 IN THE DICE ALL THE SCORE WE MADE BECOME ZERO
#  THERE WILL BE A WINNING NUMBER WHOEVER HIT 50 BY  ROLLING WILL BE THE WINNER

# LETS BREAK DOWN THE PROCESS

##################################   THINKING  ##################################
# ALLOW USER TO ROLL THE DICE ------RANDOM NUMBER GENERATOR 1 TO 6
# ASK USER TO CONTINUE OR STOP ------- IF THEY STOP THEIR TURN WE NEED TO ADD THEIR SCORE TO TOTAL SCORE
# NEED TO CONSTANTLY CHECK WEATHER THE PLAYER'S SCORE REACHED 50 OR NO IF SO DECLARE WINNER



# GENERATE RANDOM NUMBER
import random

def roll():
    min_value = 1
    max_value = 6
    roll_dice=random.randint(min_value, max_value)
    return roll_dice


# value = roll()
# print(value)

# NOW WE ARE GOING TO ASK THE PLAYERS HOW MANY WANTS TO PLAY
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players=int(players)
        if 2<= players <=4:
            break
        else:
            print("should be between 2-4 players")
    else:
        print("Invalid! Try again")

# print(players)

# NOW WE GONNA STORE THE VALUE AND PUT THE WINNING NUMBER
max_score = 50
players_score = [0 for _ in range(players)] #for every players that users set will be initialized with 0 at the beginning
# print(players_score)


# making them play
while max(players_score) < max_score:

    for player_idx in range(players):
        print("\nplayer number", player_idx +1, "Turn had just started\n")
        current_score =0

        while True:
            should_roll = input("Would you like to roll (y)?")
            if should_roll.lower() != "y":
                break
            value = roll()
            if value == 1:
                print("you rolled 1 turn is done:(")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a: ", value)

            print("Your score is ", current_score)

        players_score[player_idx] +=current_score
        print("your total score is: ",players_score[player_idx])

max_score = max(players_score)
winning_idx = players_score.index(max_score)
print("Player Number", winning_idx+1,"is the winner with score of:", max_score)