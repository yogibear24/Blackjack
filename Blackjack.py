import random

def create_deck_of_cards():
    list_of_suits = ["Red_Heart", "Red_Diamond", "Black_Spade", "Black_Clover"]
    list_of_card_types = ["Ace"] + [str(number) for number in range(2, 11)] + ["Jack", "Queen", "King"]
    list_of_all_cards = []
    for suit in range(0, len(list_of_suits)):
        for card_type in range(0, len(list_of_card_types)):
            list_of_all_cards.append(list_of_suits[suit] + " " + list_of_card_types[card_type])
    return(list_of_all_cards)

list_of_all_cards = create_deck_of_cards()

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

assigned_card_values = assign_card_values_to_dict(list_of_all_cards)

def deal_initial_cards(list_of_all_cards):
    drawn_cards = random.sample(list_of_all_cards, 4)
    dealer_hand = drawn_cards[:2]
    player_hand = drawn_cards[2:]
    cards_left = [card for card in list_of_all_cards if card not in drawn_cards]
    return(dealer_hand, player_hand, cards_left)

dealer_hand, player_hand, cards_left = deal_initial_cards(list_of_all_cards)

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

list_of_possible_player_initial_totals = output_dealt_initial_cards(dealer_hand, player_hand, assigned_card_values)

def prompt_to_hit():
    print("\n" + "Do you want to Hit?")
    print("Type 'Y' to Hit or 'N' to Stay")
    hit_input = input()
    return(hit_input)

hit_input = prompt_to_hit()

def draw_card(cards_left, player_hand, dealer_hand, list_of_all_cards):
    player_hand.append(random.sample(cards_left, 1)[0])
    # random.sample returns a list
    return([card for card in list_of_all_cards if card not in player_hand + dealer_hand])

def output_dealer_and_initial_status(assigned_card_values, dealer_hand, player_hand):
    print("\n" + "The Dealer currently has " + str(assigned_card_values[dealer_hand[0]]) + " and one Unknown Number")
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

def output_if_stay_or_incorrect_input(assigned_card_values, dealer_hand, player_hand, list_of_possible_player_initial_totals, new_player_totals):
    if len(player_hand) == 2:
        output_dealer_and_initial_status(assigned_card_values, dealer_hand, player_hand)
        action_output(list_of_possible_player_initial_totals)
    elif len(player_hand) > 2:
        output_dealer_and_initial_status(assigned_card_values, dealer_hand, player_hand)
        action_output(new_player_totals)

def update_player_hand(hit_input, player_hand, dealer_hand, cards_left, assigned_card_values, list_of_possible_player_initial_totals):
    update_counter = 0
    new_player_totals = []
    while update_counter < 1:
        if hit_input == "Y" and all(total > 21 for total in new_player_totals) is True:
            output_dealer_and_initial_status(assigned_card_values, dealer_hand, player_hand)
            print("\n" + "BUST... Got over 21, moving to Dealer's Turn")
            new_player_totals = ["BUST"]
            update_counter += 1
            return (player_hand, cards_left, new_player_totals)
        elif hit_input == "Y" and len(player_hand) == 2:
            cards_left = draw_card(cards_left, player_hand, dealer_hand, list_of_all_cards)
            output_dealer_and_initial_status(assigned_card_values, dealer_hand, player_hand)
            if player_hand[-1].endswith("Ace"):
                new_player_totals = ([entry + 1 for entry in list_of_possible_player_initial_totals]
                                     + [entry + 11 for entry in list_of_possible_player_initial_totals])
                action_output(new_player_totals)
            else:
                new_player_totals = [entry + assigned_card_values[player_hand[2]] for entry in list_of_possible_player_initial_totals]
                action_output(new_player_totals)
            hit_input = prompt_to_hit()
        elif hit_input == "Y" and len(player_hand) > 2:
            cards_left = draw_card(cards_left, player_hand, dealer_hand, list_of_all_cards)
            output_dealer_and_initial_status(assigned_card_values, dealer_hand, player_hand)
            if player_hand[-1].endswith("Ace"):
                new_player_totals = [entry + 1 for entry in new_player_totals] + [entry + 11 for entry in new_player_totals]
                action_output(new_player_totals)
            else:
                new_player_totals = [entry + assigned_card_values[player_hand[-1]] for entry in new_player_totals]
                action_output(new_player_totals)
            hit_input = prompt_to_hit()
        elif hit_input == "N":
            print("\n" + "Player chose to Stay")
            update_counter += 1
            output_if_stay_or_incorrect_input(assigned_card_values, dealer_hand, player_hand,
                                            list_of_possible_player_initial_totals, new_player_totals)
            return (player_hand, cards_left, new_player_totals)
        else:
            print("\n" + "Incorrect input...")
            output_if_stay_or_incorrect_input(assigned_card_values, dealer_hand, player_hand,
                                            list_of_possible_player_initial_totals, new_player_totals)
            hit_input = prompt_to_hit()

player_hand, cards_left, new_player_totals = update_player_hand(hit_input, player_hand, dealer_hand, cards_left, assigned_card_values, list_of_possible_player_initial_totals)

# TODO: Set automatic Turn End if player busts
# TODO: Create function for dealer to show Unknown Card and draw until 17 to 21 or bust
# TODO: Calculation function to see who wins

