import pdb
import math

def merge(num_list):
    length = len(num_list)
    if length == 1:
        # return the result of the sorted num_list
        return num_list
    else:
        # divide the unsorted list by half
        n = int(math.floor(length / 2))
        first_half = num_list[0:n]
        second_half = num_list[n:length]
        # sort left and right half
        left = merge(first_half)
        right = merge(second_half)
        # merge left and right half
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                num_list[k] = left[i]
                i += 1
                k += 1
            elif right[j] < left[i]:
                num_list[k] = right[j]
                j += 1
                k += 1
            else:
                num_list[k] = right[j]
                num_list[k + 1] = left[i]
                k += 2
        if i < len(left):
            num_list[k:] = left[i:len(left)]
        if j < len(right):
            num_list[k:] = right[j:len(right)]
        return num_list

