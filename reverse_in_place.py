def reverse(list_of_chars):
    length = len(list_of_chars)
    for i in range(length):
    	# pdb.set_trace()
        list_of_chars.append(list_of_chars[length - i - 1])
    del list_of_chars[0: length]
    print(list_of_chars)

reverse(['A', 'B', 'C', 'D', 'E'])