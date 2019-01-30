import pdb
import math

def quick_sort(unsorted_list, pivot_index, comp_count = 0):
	if len(unsorted_list) <= 1:
		return {'a': unsorted_list, 'count': comp_count}
	else:
		# comp_count to count number of comparisons made
		comp_count += len(unsorted_list) - 1
		new_list = unsorted_list.copy()
		del new_list[pivot_index]
		pivot = unsorted_list[pivot_index]
		sorted_list = [pivot]
		# i is what we've looked at, j is position of partition to insert(pivot)
		i = 0
		j = 0 
		while i < len(new_list):
			if new_list[i] < sorted_list[j]:
				sorted_list.insert(j, new_list[i])
				j += 1
			else:
				sorted_list.append(new_list[i])
			i += 1
		dict_left = dict_right = {'a': [], 'count': comp_count}
		return_result = {'count': comp_count}
		pivot_index_left = median(sorted_list[0:j])
		dict_left = quick_sort(sorted_list[0:j], pivot_index_left, 0)
		pivot_index_right = median(sorted_list[j+1:len(sorted_list)])
		dict_right = quick_sort(sorted_list[j+1:len(sorted_list)], pivot_index_right, 0)
		return_result['a'] = dict_left['a'] + [sorted_list[j]] + dict_right['a']
		return_result['count'] += dict_left['count'] + dict_right['count']
		return return_result

def median(unsorted_list):
	if len(unsorted_list) > 0:
		dict_m = {}
		first = unsorted_list[0]
		dict_m[f'{first}'] = 0
		last = unsorted_list[len(unsorted_list) - 1]
		dict_m[f'{last}'] = len(unsorted_list) - 1
		if len(unsorted_list) % 2 != 0:
			middle = len(unsorted_list) // 2
		else:
			middle = len(unsorted_list) // 2 - 1
		mid = unsorted_list[middle]
		dict_m[f'{mid}'] = middle
		return dict_m[f'{sorted([first, mid, last])[1]}']
	else:
		return 0

def command_line():
	str_input = input("Enter string of numbers: ")
	if len(str_input) > 0:
		unsorted_list = list(map(lambda x: int(x), str_input.split()))
		sorted_list = quick_sort(unsorted_list, median(unsorted_list))
		print(sorted_list) 
	else:
		command_line()

def read_file():
	p="./quick_sort.txt"
	int_file = open(p, 'r')
	initial_list = int_file.readlines()
	int_list = list(map(lambda x: int(x), initial_list))
	print(quick_sort(int_list, len(int_list) - 1))

read_file()
# command_line()