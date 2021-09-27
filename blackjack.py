"""This is the main Blackjack file for the Blackgame."""
# Use randint to generate random cards.
# DO NOT CHANGE OR REMOVE THIS COMMENT, and do not change this import otherwise all tests will fail.
from random import randint
from deck import card_name, card_value, end_turn_status, end_game_status

def main():
    """This is the code that runs the Blackgame and evaluates the winner of the game."""
    print("-----------\n" + "YOUR TURN\n" + "-----------")
    # Write all of your code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
    user_hand = 0
    drawn_count = 0
    hit = True
    while hit:
        card_rank = randint(1, 13)

        print('Drew a ' + card_name(card_rank))
        user_hand += card_value(card_rank)
        drawn_count = drawn_count + 1

        if user_hand >= 21:
            hit = False
        elif drawn_count >= 2:
            hit = input('You have ' + str(user_hand) + '. Hit (y/n)? ') == 'y'

    print('Final hand: ' + str(user_hand) + '.')
    print(end_turn_status(user_hand))

    print("-----------\n" + "DEALER TURN\n" + "-----------")

    # Write all of your code below this comment. DO NOT CHANGE OR REMOVE THIS COMMENT.
    dealer_hand = 0
    drawn_count = 0

    while dealer_hand <= 17:
        if drawn_count >= 2:
            print('Dealer has ' + str(dealer_hand) + '.')

        card_rank = randint(1, 13)

        print('Drew a ' + card_name(card_rank))
        dealer_hand += card_value(card_rank)
        drawn_count += 1

    print('Final hand: ' + str(dealer_hand) + '.')
    print(end_turn_status(dealer_hand))

    print("-----------\n" + "GAME RESULT\n" + "-----------")
    # Code to determine the winner of the game
    print(end_game_status(user_hand, dealer_hand))

if __name__ == "__main__":
    main()
