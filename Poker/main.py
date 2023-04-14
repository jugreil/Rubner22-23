import random


class Hands():
    count_high_hand = 0
    count_one_pair = 0
    count_two_pair = 0
    count_three_kind = 0
    count_straight = 0
    count_flush = 0
    count_full_house = 0
    count_four_kind = 0
    count_straight_flush = 0
    count_royal_flush = 0


hands = Hands()
existing_cards = range(52)

drew_cards = []
drew_colors = []
drew_types = []
calculated_percentage = [50.1, 42.3, 4.75, 2.11, 0.392, 0.197, 0.144, 0.0240, 0.0014, 0.000154]


def draw_cards(number):
    global drew_cards
    for i in range(number):
        card = random.randint(0, 51)
        while card in drew_cards:
            card = random.randint(0, 51)
        drew_cards.append(card)


def get_card_color(card):
    return card // 13


def get_card_type(card):
    return card % 13


def split_cards():
    global drew_colors, drew_types
    for i in drew_cards:
        drew_colors.append(get_card_color(i))
        drew_types.append(get_card_type(i))


def calculate_combination():
    global hands, drew_colors, drew_types
    max_color = max(drew_colors, key=drew_colors.count)
    max_type = max(drew_types, key=drew_types.count)
    count_color = drew_colors.count(max_color)
    count_type = drew_types.count(max_type)
    if count_color == 5:
        # check royal flush, straight flush, flush
        drew_types.sort()
        if drew_types[-1] - 4 == drew_types[0]:
            if drew_types[-1] == 12:
                hands.count_royal_flush += 1
                return
            else:
                hands.count_straight_flush += 1
                return
        hands.count_flush += 1
        return
    if count_type >= 2:
        if count_type >= 3:
            if count_type == 4:
                hands.count_four_kind += 1
                return
            else:
                # check full house
                filtered_list = [x for x in drew_types if x != max_type]
                if filtered_list.count(max(filtered_list, key=filtered_list.count)) == 2:
                    hands.count_full_house += 1
                    return
                hands.count_three_kind += 1
                return
        else:
            # check one pair, two pair
            filtered_list = [x for x in drew_types if x != max_type]
            if filtered_list.count(max(filtered_list, key=filtered_list.count)) == 2:
                hands.count_two_pair += 1
                return
            hands.count_one_pair += 1
            return
    # check straight
    drew_types.sort()
    if drew_types[-1] - 4 == drew_types[0]:
        hands.count_straight += 1
        return
    # bad hand:
    hands.count_high_hand += 1
    reset()
    return


def reset():
    global drew_colors, drew_types, drew_cards
    drew_colors = []
    drew_types = []
    drew_cards = []


def turn():
    draw_cards(5)
    split_cards()
    calculate_combination()
    reset()


if __name__ == '__main__':
    sum_hands = 5000000
    for i in range(sum_hands):
        turn()
    counter = 0
    for key in sorted(vars(hands), key=vars(hands).get, reverse=True):
        print("{0}: {1} -> {2}% -> {3}% (calculated) ".format(key, vars(hands)[key],
                                                              round((vars(hands)[key] / sum_hands * 100), 5),
                                                              calculated_percentage[counter]))
        counter += 1
