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
		return_result = {}
		# below is when pivot is always last element of list
		# pivot_index_left = j - 1
		pivot_index_left = 0
		dict_left = quick_sort(sorted_list[0:j], pivot_index_left, 0)
		# below is when pivot is always last element of list
		# pivot_index_right = len(sorted_list) - j - 2
		pivot_index_right = 0
		dict_right = quick_sort(sorted_list[j+1:len(sorted_list)], pivot_index_right, 0)
		return_result['a'] = dict_left['a'] + [sorted_list[j]] + dict_right['a']
		return_result['count'] = comp_count + dict_left['count'] + dict_right['count']
		return return_result

def command_line():
	str_input = input("Enter string of numbers: ")
	if len(str_input) > 0:
		unsorted_list = list(map(lambda x: int(x), str_input.split()))
		sorted_list = quick_sort(unsorted_list, len(unsorted_list) - 1)
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