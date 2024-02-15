from operator import itemgetter
from random import shuffle
from time import sleep


def check_players_validation(player_num):
    return int(player_num) if player_num.isdigit() else None


def choose_a_winner(players):
    valid_players = {name:score for name, score in players if score < 22}
    sorted_players = sorted(valid_players.items(), key=itemgetter(1), reverse=True)
    winners = []
    max_score = 0
    for name, score in sorted_players:
        if score >= max_score:
            winners.append(name)
        else:
            break
    return winners



def main():
    while True:
        N = check_players_validation(input("Number of Players: "))
        if N: break

    # Create deck
    deck = [2, 3, 4, 6, 7, 8, 9, 10, 11] * 4
    shuffle(deck)

    # Dict with all players
    players = {}

    # Fill the players dict with players
    for i in range(N):
        name = input(f"Please, enter a name for Player #{i + 1}: ")
        players[name] = 0

    # GAME
    for player in players:
        
        # Take 2 cards at start
        players[player] += sum(card1 := deck.pop(), card2 := deck.pop())
        print(f"{player}, you took two cards {card1} and {card2}")
        if card1 == 11 and card2 == 11:
            print("You have 2 aces! You won! Game over and the winner is {player}!!! Congratulations!")
        sleep(2)


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
                    print("You're busted! Try next time!")
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
