import random

def create_deck_of_cards():
    list_of_suits = ["Red_Heart", "Red_Diamond", "Black_Spade", "Black_Clover"]
    list_of_card_types = [str(number) for number in range(1, 11)] + ["Jack", "Queen", "King"]
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
        if current_card[-1].isnumeric() is True and current_card[-1] != "0":
            card_value_dict.update({current_card : int(current_card[-1])})
        # Assign initial value of 1 to a 1 Card, but later on mechanic is it can be 1 or 11...
        elif current_card.endswith(("10", "Jack", "Queen", "King")):
            card_value_dict.update({current_card : 10})
    return(card_value_dict)

assigned_card_values = assign_card_values_to_dict(list_of_all_cards)

def deal_initial_cards(list_of_all_cards):
    drawn_cards = random.sample(list_of_all_cards, 4)
    dealer_hand = drawn_cards[:2]
    player_hand = drawn_cards[2:]
    return(dealer_hand, player_hand)

dealer_hand, player_hand = deal_initial_cards(list_of_all_cards)

def output_dealt_initial_cards(dealer_hand, player_hand, assigned_card_values):
    print("The Dealer has a " + dealer_hand[0].split(" ")[-1] + " and one Unknown Card")
    print("You have a " + player_hand[0].split(" ")[-1] + " and a " + player_hand[1].split(" ")[-1])
    player_initial_total = assigned_card_values[player_hand[0]] + assigned_card_values[player_hand[1]]
    print("\n" + "The Dealer currently has " + str(assigned_card_values[dealer_hand[0]]) + " and one Unknown Number")
    # Print the dealer's hand value in case people do not know what value a face card is
    print("Your current total is " + str(player_initial_total))

output_dealt_initial_cards(dealer_hand, player_hand, assigned_card_values)

def prompt_to_hit():
    print("\n" + "Do you want to Hit?")
    print("Type 'Y' to Hit or 'N' to Stay")
    hit_input = input()
    return(hit_input)

hit_input = prompt_to_hit()
