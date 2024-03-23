import random
#from art import logo
#from replit import clear

#print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def game():
    global user_card  # Using global variable
    global dealer_card  # Using global variable
    print("Hello man, here are your cards")
    # Reinitialize the card lists for a new game
    user_card = random.choices(cards, k=2)
    dealer_card = random.choices(cards, k=2)
    user_score = sum(user_card)
    dealer_score = sum(dealer_card)
    print(f"Your cards: {user_card}, current score: {user_score}")
    print(f"Computer first card is: {dealer_card[0]}")

    should_continue = True
    while should_continue:
        next_move = input("Please decide your next action: one more 'card', 'pass', or 'q': \n").lower()
        #clear()
        #print(logo)
        if next_move == 'card':
            user_card.append(random.choice(cards))
            user_score = sum(user_card)
            print(f"Your cards: {user_card}, current score: {user_score}")
            if user_score > 21:
                print(f"Your final score: {user_score}")
                print(f"Dealer final score: {dealer_score}")
                print("You went over. You lose!")
                return
        elif next_move == 'pass':
            # Make the dealer draw cards until its score is 17 or greater
            while dealer_score < 17:
                dealer_card.append(random.choice(cards))
                dealer_score = sum(dealer_card)

            print(f"Your cards: {user_card}, current score: {user_score}")
            print(f"Dealer cards: {dealer_card}, current score: {dealer_score}")
            # Game outcome conditions
            if dealer_score > 21:
                print("Dealer went over. You win!")
            elif user_score > dealer_score:
                print("You win!")
            elif user_score == dealer_score:
                print("It's a draw!")
            else:
                print("You lose!")

            should_continue = False  # End the game loop

        elif next_move == 'q':  # Corrected the condition
            should_continue = False

while True:
    game()
    choice = input("Please make your next move: 'y' to play more or 'n' to quit: \n").lower()
    #clear()
    #print(logo)
    if choice == 'n':
        break