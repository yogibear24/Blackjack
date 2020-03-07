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
        elif current_card.endswith("10"):
            card_value_dict.update({current_card: 10})
        elif current_card.endswith("Jack"):
            card_value_dict.update({current_card : 11})
        elif current_card.endswith("Queen"):
            card_value_dict.update({current_card : 12})
        elif current_card.endswith("King"):
            card_value_dict.update({current_card : 13})
    return(card_value_dict)

assigned_card_values = assign_card_values_to_dict(list_of_all_cards)
