from operator import itemgetter
from random import shuffle
from time import sleep


def check_players_validation(player_num):
    try:
        player_num = int(player_num)
    except ValueError:
        player_num = 0
    return player_num if 7 > player_num > 1 else None


def choose_a_winner(players):
    valid_players = {player:score for player, score in players.items() if score < 22}
    sorted_players = sorted(valid_players.items(), key=itemgetter(1), reverse=True)
    winners = []
    max_score = 0
    for name, score in sorted_players:
        if score >= max_score:
            max_score = score
            winners.append(name)
    return winners


def get_players():
    players_dict = {}
    print("Please enter the number of players in game. Note that number must be between 2 and 6 inclusively!")
    
    while True:
        player_num = check_players_validation(input("Number of Players: "))
        if player_num: break
    
    # Fill the players dict with players
    for i in range(player_num):
        while True:
            name = input(f"Please, enter a name for Player #{i + 1}: ")
            if name in players_dict:
                print("This player is playing already. Please choose another name!")
            else:
                break
        players_dict[name] = 0
    
    return players_dict


def main():
    # Create deck
    deck = [2, 3, 4, 6, 7, 8, 9, 10, 11] * 4
    shuffle(deck)

    # Gather all players
    players = get_players()

    # GAME
    for player in players:
        
        # Take 2 cards at start
        players[player] += sum((card1 := deck.pop(), card2 := deck.pop()))
        print(f"{player}, you took two cards {card1} and {card2}")
        if card1 == 11 and card2 == 11:
            print(f"You have 2 aces! You won! Game over and the winner is {player}!!! Congratulations!")
            exit()
        sleep(1.5)


    for player in players:

        score = players[player]

        while True:
            choice = input(f"{player}, do you want to take 1 more? y/n ")
            if choice == 'y':
                new_card = deck.pop()
                score += new_card
                print(f"You took card with rank {new_card}")
                sleep(0.5)
                print(f"Your new score is {score}")
                if score > 21:
                    print("You're busted! See you!")
                    sleep(1)
                    break
                elif score == 21:
                    print("You have 21 points!")
                    print("Next player...")
                    sleep(1)
                    break
            elif choice == 'n':
                print(f'You have {score} points! Next player...')
                sleep(1)
                break
            else:
                print('Please enter y or n')
                sleep(0.5)

        players[player] = score

    winners = choose_a_winner(players)

    # Name the winners
    print(f"And the winner{'s are' if len(winners) > 1 else ' is'}:", end=" ")
    print(" ".join(winners))


if __name__ == "__main__":
    main()
