# find repeats in array

def find_repeat(the_list):
    if len(the_list) <= 1:
        return 0
    else:
        length = len(the_list)
        middle = length // 2
        left = the_list[0:middle]
        right = the_list[middle:length]
        for num in left:
            if num in right:
                return num
                break
        if find_repeat(left) == 0:
            return find_repeat(right)

print(find_repeat([1, 2, 5, 8, 8, 8]))