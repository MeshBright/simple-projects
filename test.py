def blackjack_hand_greater_than(hand_1, hand_2):
    """
    Return True if hand_1 beats hand_2, and False otherwise.
    
    In order for hand_1 to beat hand_2 the following must be true:
    - The total of hand_1 must not exceed 21
    - The total of hand_1 must exceed the total of hand_2 OR hand_2's total must exceed 21
    
    Hands are represented as a list of cards. Each card is represented by a string.
    
    When adding up a hand's total, cards with numbers count for that many points. Face
    cards ('J', 'Q', and 'K') are worth 10 points. 'A' can count for 1 or 11.
    
    When determining a hand's total, you should try to count aces in the way that 
    maximizes the hand's total without going over 21. e.g. the total of ['A', 'A', '9'] is 21,
    the total of ['A', 'A', '9', '3'] is 14.
    
    Examples:
    >>> blackjack_hand_greater_than(['K'], ['3', '4'])
    True
    >>> blackjack_hand_greater_than(['K'], ['10'])
    False
    >>> blackjack_hand_greater_than(['K', 'K', '2'], ['3'])
    False
    """
    pass
    hand_1_value = 0
    hand_1_A_count = 0
    hand_2_value = 0
    hand_2_A_count = 0
    for hand_1_items in hand_1:
        if (hand_1_items == 'J' or "Q" or "K"):
            hand_1_value += 10
        elif (hand_1_items == "A"):
            hand_1_A_count += 1
            if ((hand_1_items == "A") and (hand_1_A_count == 1)):
                hand_1_value += 1
                hand_1_A_count == 0
                
            else:
                hand_1_value += 11
        else:
            hand_1_value += hand_1_items

    for hand_2_items in hand_2:
        if (hand_2_items == 'J' or "Q" or "K"):
            hand_2_value += 10
        elif (hand_2_items == "A"):
            hand_2_A_count += 1
            if ((hand_2_items == "A") and (hand_2_A_count == 1)):
                hand_2_value += 1
                hand_2_A_count == 0
                
            else:
                hand_2_value += 11
        else:
            hand_2_value += hand_2_items
    if (((hand_1_value <= hand_2_value) or (hand_2_value <= 21)) and (hand_1_value <= 21)):
        return True
    else:
        return False