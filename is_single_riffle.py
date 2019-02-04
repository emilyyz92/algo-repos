import pdb

def is_single_riffle(half1, half2, shuffled_deck):
    is_single_riffle = True
    if len(shuffled_deck) == len(half1) + len(half2):
        if len(half1) == 0:
            is_single_riffle = shuffled_deck == half2
        elif len(half2) == 0:
            is_single_riffle = shuffled_deck == half1
        elif len(shuffled_deck) == 0:
            is_single_riffle = False
        else:
            i = j = 0
            # pdb.set_trace()
            for k, card in enumerate(shuffled_deck):
                if i < len(half1) and j < len(half2):
                    if card == half1[i]:
                        i += 1
                    elif card == half2[j]:
                        j += 1
                    else:
                        is_single_riffle = False
                        break
            if i == len(half1) and j < len(half2):
                is_single_riffle = half2[j:] == shuffled_deck[k:]
            if j == len(half2) and i < len(half1):
                is_single_riffle = half1[i:] == shuffled_deck[k:]
        return is_single_riffle
    else:
        return not is_single_riffle

print(is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5]))