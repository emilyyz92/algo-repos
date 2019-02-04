import functools
import pdb

def highest_product_of_3(list_of_ints):
    # keep track of biggest 3 + ints, smallest 2 neg ints, and biggest 3 neg ints
    if len(list_of_ints) <= 3:
        # return functools.reduce(lambda x, y: x*y, list_of_ints)
        raise ValueError('Less than 3 items')
    else:
        max_ints = []
        min_neg_ints = []
        max_neg_ints = []
        for num in list_of_ints:
            if num > 0:
                if len(max_ints) > 0 and num > min(max_ints):
                    # put smallest in the end
                    max_ints.append(num)
                else:
                    max_ints.append(num)
                if len(max_ints) > 3:
                    del max_ints[max_ints.index(sorted(max_ints)[0])]
            if num < 0:
                # put smallest abs value at the end
                if len(max_neg_ints) > 0 and num < max(max_neg_ints):
                    max_neg_ints.append(num)
                else:
                    max_neg_ints.append(num)
                if len(max_neg_ints) > 2:
                    del max_neg_ints[max_neg_ints.index(sorted(max_neg_ints)[2])]
                if len(min_neg_ints) > 0 and num > min(min_neg_ints):
                    min_neg_ints.append(num)
                else:
                    min_neg_ints.append(num)
                if len(min_neg_ints) > 3:
                    del min_neg_ints[min_neg_ints.index(sorted(min_neg_ints)[0])]
        # pdb.set_trace()
        # if there are both + and - number in list
        if len(max_neg_ints) == 2 and len(max_ints) > 0:
            max_pd = functools.reduce(lambda x, y: x*y, max_neg_ints) * max(max_ints)
        elif len(max_neg_ints) > 0 and len(max_ints) == 0:
            max_pd = functools.reduce(lambda x, y: x*y, min_neg_ints)
        else:
            max_pd = functools.reduce(lambda x, y: x*y, max_ints)
        return max_pd

print(highest_product_of_3([-10, 1, 3, 2, -10]))