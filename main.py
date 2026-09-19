# Did not use AI or other resources to write code, but did use the AI accompanying VS Code to check work, but did not make any changes

import random

# Set function for dealing a card
def deal_card():
    card_number = random.randint(1,13)
    # Set card_number to include Jack, Queen, and King but set the amount to 10
    if card_number > 10:
        card_number = 10
    return card_number

# Set function to deal two cards for the player
def get_player_score():
    player_card_1 = deal_card()
    player_card_2 = deal_card()

    # Add the cards together and print total
    player_score = player_card_1 + player_card_2

    # Check if player busts if the sum of the two cards is over 21 and loses
    if player_score > 21:
        return player_score
    # If player doesn't bust, print the score
    else:
        print("Your hand of two cards has a total value of ", player_score, ".", sep="")

        # Prompt player if they want to draw another card
        player_response = input("Would you like to take another card? (y/n) ")

        # Validation check for if the playet types anything other than y or n
        if (player_response != 'y') and (player_response != 'n'):

            # Print error
            print("Error. Please enter 'y' or 'n'.")

            # Prompt question again
            player_response = input("Would you like to take another card? (y/n) ")

        # If yes, deal another card, while loop    
        while player_response == 'y':

            # Draw another card, loop
            new_player_card = deal_card()

            # New sum
            player_score += new_player_card

            # Print new sum
            print(" Your hand is now now has a total value of ", player_score, ".", sep="")

            # If player busts, return function
            if player_score > 21:
                return player_score
            else:

                # Ask if the player wants to draw another card
                player_response = input("Would you like to take another card? (y/n) ")
        return player_score

# Set function for calculating the dealer score
def get_dealer_score():

    # Deal two cards
    dealer_card_1 = deal_card()
    dealer_card_2 = deal_card()

    # Get dealer sum
    dealer_score = dealer_card_1 + dealer_card_2

    # Make sure the dealer only deals above 16, draw another card with a while loop until value is over 16
    while dealer_score < 16:
        another_dealer_card = deal_card()
        dealer_score += another_dealer_card
    return dealer_score


# Set main function
def main():
    # Get dealer score
    dealer_score = get_dealer_score()

    # Get player score
    player_score =  get_player_score()
    print("You have stopped taking more cards with a hand value of ", player_score, ".", sep="")

    if player_score > 21:

        # Player busts with a sum over 21, dealer wins
        print("You BUSTED with a total value of ", player_score, ".", sep="")
        print('\n')   
        print("** You lose. **")


    elif dealer_score > 21:

        # Dealer busts with a sum over 21, player wins
        print("The Dealer BUSTED with a value of ", dealer_score, ".", sep="")
        print('\n')   
        print("** You win! **")

    else:

        # Dealer wins with higher score than player but does not bust
        print("The dealer was dealt a hand with a value of ", dealer_score, ".", sep="")
        if dealer_score >= player_score:
            print('\n')   
            print("** You lose! **")

        # Player wins if above dealer score but does not bust
        elif dealer_score < player_score:
            print('\n')   
            print("** You win! **")

    # Ask if the player wants to play again
    player_response_to_playing_again = input("Would you like to play again? (y/n) ")

    # If yes, call main function again
    if player_response_to_playing_again == 'y':
        main()

    # If no, end program!
   
# Call main function     
main()