def reverse(list_of_chars):
    length = len(list_of_chars)
    for i in range(length):
    	# pdb.set_trace()
        list_of_chars.append(list_of_chars[length - i - 1])
    del list_of_chars[0: length]
    return list_of_chars

def reverse_words(message):
    msg_str = ''.join(message)
    msg_list = msg_str.split()
    rev_list = reverse(msg_list)
    length = len(message)
    for word in rev_list:
        for letter in word:
            message.append(letter)
        message.append(' ')
    del message[0:length]
    return message

print(reverse_words(list('yummy is cake bundt chocolate')))