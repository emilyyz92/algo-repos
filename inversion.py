#!/usr/bin/env python3
import pdb
import math
from pathlib import Path

def inversion(num_list):
	n = len(num_list)
	if n == 1:
		return 0
	else:
		half = int(math.floor(n / 2))
		first_half = num_list[0:half]
		second_half = num_list[half:n]
		sorted_first = first_half.copy()
		sorted_second = second_half.copy()
		sorted_first = merge_sort(sorted_first)
		sorted_second = merge_sort(sorted_second)
		# get first half and second half # of inversions
		# sort the first and second half
		first_inv = inversion(first_half)
		second_inv = inversion(second_half)
		merge_inv = i = j = 0
		# merge the sorted first and second half
		while j < len(sorted_second) and i < len(sorted_first):
			if sorted_second[j] < sorted_first[i]:
				merge_inv += len(sorted_first) - i
				j += 1
			else:
				i += 1
		return first_inv + second_inv + merge_inv

def command_line():
	str_input = input("Enter string of numbers: ")
	if len(str_input) > 0:
		inversion_list = list(map(lambda x: int(x), str_input.split()))
		print(inversion(inversion_list)) 
	else:
		command_line()

def merge_sort(num_list):
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
        left = merge_sort(first_half)
        right = merge_sort(second_half)
        # merge left and right half
        i = j = k = 0
        sorted_list = num_list.copy()
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_list[k] = left[i]
                i += 1
                k += 1
            elif right[j] < left[i]:
                sorted_list[k] = right[j]
                j += 1
                k += 1
            else:
                sorted_list[k] = right[j]
                sorted_list[k + 1] = left[i]
                k += 2
        if i < len(left):
            sorted_list[k:] = left[i:len(left)]
        if j < len(right):
            sorted_list[k:] = right[j:len(right)]
        return sorted_list

def read_file():
	p = "./IntegerArray.txt";
	integer_file = open(p, 'r')
	initial_list = integer_file.readlines()
	integer_list = list(map(lambda x: int(x), initial_list))
	print(inversion(integer_list))


command_line()
# read_file()