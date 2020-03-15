import random
import time

def create_deck_of_cards():
    list_of_suits = ["Red_Heart", "Red_Diamond", "Black_Spade", "Black_Clover"]
    list_of_card_types = ["Ace"] + [str(number) for number in range(2, 11)] + ["Jack", "Queen", "King"]
    list_of_all_cards = []
    for suit in range(0, len(list_of_suits)):
        for card_type in range(0, len(list_of_card_types)):
            list_of_all_cards.append(list_of_suits[suit] + " " + list_of_card_types[card_type])
    return(list_of_all_cards)

def assign_card_values_to_dict(list_of_all_cards):
    card_value_dict = {}
    for card in range(0, len(list_of_all_cards)):
        current_card = list_of_all_cards[card]
        if current_card[-1].isnumeric() is True and current_card[-1] != ("0" or "1"):
            card_value_dict.update({current_card : int(current_card[-1])})
        # Assign initial value of 1 to a 1 Card, but later on mechanic is it can be 1 or 11...
        elif current_card.endswith("Ace"):
            card_value_dict.update({current_card : 1})
        elif current_card.endswith(("10", "Jack", "Queen", "King")):
            card_value_dict.update({current_card : 10})
    return(card_value_dict)

def deal_initial_cards(list_of_all_cards):
    drawn_cards = random.sample(list_of_all_cards, 4)
    dealer_hand = drawn_cards[:2]
    player_hand = drawn_cards[2:]
    cards_left = [card for card in list_of_all_cards if card not in drawn_cards]
    return(dealer_hand, player_hand, cards_left)

def generate_possible_player_initial_totals(player_hand, assigned_card_values, list_of_possible_player_initial_totals):
    if assigned_card_values[player_hand[0]] == 1 and assigned_card_values[player_hand[1]] != 1:
        list_of_possible_player_initial_totals.append(1 + assigned_card_values[player_hand[1]])
        list_of_possible_player_initial_totals.append(11 + assigned_card_values[player_hand[1]])
        print("Your current possible totals are " + str(list_of_possible_player_initial_totals).strip("[]"))
    elif assigned_card_values[player_hand[0]] == 1 and assigned_card_values[player_hand[1]] == 1:
        list_of_possible_player_initial_totals.append(1 + 1)
        list_of_possible_player_initial_totals.append(11 + 1)
        list_of_possible_player_initial_totals.append(11 + 11)
        print("Your current possible totals are " + str(list_of_possible_player_initial_totals).strip("[]"))
    elif assigned_card_values[player_hand[0]] != 1 and assigned_card_values[player_hand[1]] == 1:
        list_of_possible_player_initial_totals.append(assigned_card_values[player_hand[0]] + 1)
        list_of_possible_player_initial_totals.append(assigned_card_values[player_hand[0]] + 11)
        print("Your current possible totals are " + str(list_of_possible_player_initial_totals).strip("[]"))
    elif assigned_card_values[player_hand[0]] != 1 and assigned_card_values[player_hand[1]] != 1:
        list_of_possible_player_initial_totals.append(assigned_card_values[player_hand[0]] + assigned_card_values[player_hand[1]])
        print("Your current total is " + str(list_of_possible_player_initial_totals[0]))

def output_dealt_initial_cards(dealer_hand, player_hand, assigned_card_values):
    print("The Dealer has a " + dealer_hand[0].split(" ")[-1] + " and one Unknown Card")
    print("You have a " + player_hand[0].split(" ")[-1] + " and a " + player_hand[1].split(" ")[-1])
    # Print the dealer's hand value in case people do not know what value a face card is
    list_of_possible_player_initial_totals = []
    generate_possible_player_initial_totals(player_hand, assigned_card_values, list_of_possible_player_initial_totals)
    return(list_of_possible_player_initial_totals)

def prompt_to_hit():
    print("\n" + "Do you want to Hit?")
    print("Type 'Y' to Hit or 'N' to Stay")
    hit_input = input()
    return(hit_input)

def draw_card(cards_left, hand_to_append, other_hand):
    hand_to_append.append(random.sample(cards_left, 1)[0])
    # random.sample returns a list
    return([card for card in cards_left if card not in hand_to_append + other_hand])

def output_dealer_and_initial_status(dealer_hand, player_hand):
    print("\n" + "The Dealer has a " + dealer_hand[0].split(" ")[-1] + " and one Unknown Card")
    initial_string = ("You have a " + player_hand[0].split(" ")[-1] + ", a " + player_hand[1].split(" ")[-1])
    for card in range(2, len(player_hand) - 1):
        initial_string += (", a " + player_hand[card].split(" ")[-1])
    initial_string += (", and a " + player_hand[-1].split(" ")[-1])
    print(initial_string)

def action_output(original_list_of_totals):
    if len(original_list_of_totals) > 1:
        print("Your current possible totals are " + str(original_list_of_totals).strip("[]"))
    elif len(original_list_of_totals) == 1:
        print("Your current total is " + str(original_list_of_totals).strip("[]"))

def output_if_stay_or_incorrect_input(dealer_hand, player_hand):
    if len(player_hand) == 2:
        print("\n" + "The Dealer has a " + dealer_hand[0].split(" ")[-1] + " and one Unknown Card")
        initial_string = ("You have a " + player_hand[0].split(" ")[-1] + " and a " + player_hand[1].split(" ")[-1])
        print(initial_string)
    elif len(player_hand) > 2:
        output_dealer_and_initial_status(dealer_hand, player_hand)

def check_for_21_or_over(new_player_totals, update_counter, player_hand, cards_left):
    if all(total > 21 for total in new_player_totals) is True:
        new_player_totals = ["BUST"]
        print("\n" + "BUST... Got over 21, moving to Dealer's Turn")
        update_counter += 1
        return (player_hand, cards_left, new_player_totals)
    else:
        hit_input = prompt_to_hit()

def bust_output(final_player_value, update_counter):
    final_player_value = "BUST"
    print("\n" + "BUST... Got over 21, moving to Dealer's Turn")
    update_counter += 1

def update_player_hand(hit_input, player_hand, dealer_hand, cards_left, assigned_card_values, list_of_possible_player_initial_totals):
    update_counter = 0
    new_player_totals = []
    final_player_value = 0
    while update_counter < 1:
        if hit_input == "Y" and len(player_hand) == 2:
            cards_left = draw_card(cards_left, player_hand, dealer_hand)
            output_dealer_and_initial_status(dealer_hand, player_hand)
            if player_hand[-1].endswith("Ace"):
                new_player_totals = ([entry + 1 for entry in list_of_possible_player_initial_totals]
                                     + [entry + 11 for entry in list_of_possible_player_initial_totals])
                action_output(new_player_totals)
                if all(total > 21 for total in new_player_totals) is True:
                    bust_output(final_player_value, update_counter)
                    return (player_hand, cards_left, final_player_value)
                else:
                    hit_input = prompt_to_hit()
            else:
                new_player_totals = [entry + assigned_card_values[player_hand[2]] for entry in list_of_possible_player_initial_totals]
                action_output(new_player_totals)
                if all(total > 21 for total in new_player_totals) is True:
                    bust_output(final_player_value, update_counter)
                    return (player_hand, cards_left, final_player_value)
                else:
                    hit_input = prompt_to_hit()
        elif hit_input == "Y" and len(player_hand) > 2:
            cards_left = draw_card(cards_left, player_hand, dealer_hand)
            output_dealer_and_initial_status(dealer_hand, player_hand)
            if player_hand[-1].endswith("Ace"):
                new_player_totals = [entry + 1 for entry in new_player_totals] + [entry + 11 for entry in new_player_totals]
                action_output(new_player_totals)
                if all(total > 21 for total in new_player_totals) is True:
                    bust_output(final_player_value, update_counter)
                    return (player_hand, cards_left, final_player_value)
                else:
                    hit_input = prompt_to_hit()
            else:
                new_player_totals = [entry + assigned_card_values[player_hand[-1]] for entry in new_player_totals]
                action_output(new_player_totals)
                if all(total > 21 for total in new_player_totals) is True:
                    bust_output(final_player_value, update_counter)
                    return (player_hand, cards_left, final_player_value)
                else:
                    hit_input = prompt_to_hit()
        elif hit_input == "N":
            print("\n" + "Player chose to Stay")
            update_counter += 1
            output_if_stay_or_incorrect_input(dealer_hand, player_hand)
            if new_player_totals == []:
                new_player_totals = list_of_possible_player_initial_totals
                final_player_value = max([total for total in new_player_totals if total <= 21])
                print("Your Total is " + str(final_player_value))
                return (player_hand, cards_left, final_player_value)
            else:
                final_player_value = max([total for total in new_player_totals if total <= 21])
                print("Your Total is " + str(final_player_value))
                return (player_hand, cards_left, final_player_value)
        else:
            print("\n" + "Incorrect input...")
            output_if_stay_or_incorrect_input(dealer_hand, player_hand)
            hit_input = prompt_to_hit()

def generate_possible_dealer_initial_totals(dealer_hand, assigned_card_values, list_of_possible_dealer_initial_totals):
    if assigned_card_values[dealer_hand[0]] == 1 and assigned_card_values[dealer_hand[1]] != 1:
        list_of_possible_dealer_initial_totals.append(1 + assigned_card_values[dealer_hand[1]])
        list_of_possible_dealer_initial_totals.append(11 + assigned_card_values[dealer_hand[1]])
    elif assigned_card_values[dealer_hand[0]] == 1 and assigned_card_values[dealer_hand[1]] == 1:
        list_of_possible_dealer_initial_totals.append(1 + 1)
        list_of_possible_dealer_initial_totals.append(11 + 1)
        list_of_possible_dealer_initial_totals.append(11 + 11)
    elif assigned_card_values[dealer_hand[0]] != 1 and assigned_card_values[dealer_hand[1]] == 1:
        list_of_possible_dealer_initial_totals.append(assigned_card_values[dealer_hand[0]] + 1)
        list_of_possible_dealer_initial_totals.append(assigned_card_values[dealer_hand[0]] + 11)
    elif assigned_card_values[dealer_hand[0]] != 1 and assigned_card_values[dealer_hand[1]] != 1:
        list_of_possible_dealer_initial_totals.append(assigned_card_values[dealer_hand[0]] + assigned_card_values[dealer_hand[1]])

def output_dealer_status(dealer_hand):
    initial_string = ("The Dealer has a " + dealer_hand[0].split(" ")[-1] + ", a " + dealer_hand[1].split(" ")[-1])
    for card in range(2, len(dealer_hand) - 1):
        initial_string += (", a " + dealer_hand[card].split(" ")[-1])
    initial_string += (", and a " + dealer_hand[-1].split(" ")[-1])
    print(initial_string)

def update_dealer_hand(player_hand, cards_left, dealer_hand, assigned_card_values):
    print("\n" + "The Dealer flips over the Unknown Card...")
    time.sleep(2)
    print("The Dealer has a " + dealer_hand[0].split(" ")[-1] + " and a " + dealer_hand[1].split(" ")[-1])
    time.sleep(2)
    list_of_possible_dealer_totals = []
    generate_possible_dealer_initial_totals(dealer_hand, assigned_card_values, list_of_possible_dealer_totals)
    dealer_final_value = 0
    dealer_counter = 0
    while dealer_counter < 1:
        if all(total < 17 for total in list_of_possible_dealer_totals) is True:
            print("\n" + "The Dealer draws a card..." + "\n")
            time.sleep(2)
            cards_left = draw_card(cards_left, dealer_hand, player_hand)
            output_dealer_status(dealer_hand)
            if dealer_hand[-1].endswith("Ace"):
                list_of_possible_dealer_totals = ([entry + 1 for entry in list_of_possible_dealer_totals]
                                                  + [entry + 11 for entry in list_of_possible_dealer_totals])
            else:
                list_of_possible_dealer_totals = [entry + assigned_card_values[dealer_hand[-1]] for entry in list_of_possible_dealer_totals]
        elif all(total > 21 for total in list_of_possible_dealer_totals) is True:
            dealer_counter += 1
            dealer_final_value = "BUST"
            print("\n" + "BUST... Dealer got over 21")
            return(dealer_final_value)
        elif any((17 <= total <= 21) for total in list_of_possible_dealer_totals) is True:
            dealer_counter += 1
            print("\n" + "Dealer chooses to Stay")
            list_of_possible_dealer_totals = [total for total in list_of_possible_dealer_totals if (17 <= total <= 21)]
            dealer_final_value = max(list_of_possible_dealer_totals)
            print("The Dealer Total is " + str(dealer_final_value))
            return(dealer_final_value)

def calculate_winner(player_final_value, dealer_final_value):
    if (player_final_value and dealer_final_value) != "BUST":
        if (player_final_value - dealer_final_value) < 0:
            print("\n" + "Dealer Wins, You Lose")
        elif (player_final_value - dealer_final_value) > 0:
            print("\n" + "You Win!")
        elif (player_final_value - dealer_final_value) == 0:
            print("\n" + "Dealer and Player Tie")
    elif player_final_value == "BUST" and dealer_final_value != "BUST":
        print("\n" + "Dealer Wins, You Lose")
    elif player_final_value != "BUST" and dealer_final_value == "BUST":
        print("\n" + "You Win!")

def continue_game():
    time.sleep(2)
    print("\n" + "Play another game?")
    print("Type 'Y' to Continue or 'N' to Quit")
    continue_input = input()
    return(continue_input)

def full_game_run():
    print("BLACKJACK" + "\n")
    time.sleep(1)
    game_counter = 0
    while game_counter < 1:
        list_of_all_cards = create_deck_of_cards()
        assigned_card_values = assign_card_values_to_dict(list_of_all_cards)
        dealer_hand, player_hand, cards_left = deal_initial_cards(list_of_all_cards)
        list_of_possible_player_initial_totals = output_dealt_initial_cards(dealer_hand, player_hand,
                                                                            assigned_card_values)
        hit_input = prompt_to_hit()
        player_hand, cards_left, final_player_value = update_player_hand(hit_input, player_hand, dealer_hand,
                                                                         cards_left,
                                                                         assigned_card_values,
                                                                         list_of_possible_player_initial_totals)
        dealer_final_value = update_dealer_hand(player_hand, cards_left, dealer_hand, assigned_card_values)
        calculate_winner(final_player_value, dealer_final_value)
        continue_input = continue_game()
        if continue_input == "Y":
            game_counter += 0
        elif continue_input == "N":
            game_counter += 1
        else:
            while continue_input != ("Y" or "N"):
                continue_input = continue_game()

full_game_run()

# TODO: Make a GUI using Qt for Python
