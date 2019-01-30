import math
import pdb

# pseudo code
# if n = 2 (e.g., 12 * 78)
# do karatsuba - return 10 ** 2 * ac + 10 * ((a+b)(c+d) - ac - bd) + bd
# else - n > 2
# do karatsuba for ad
# do karatsuba for (a+b)(c+d)
# do karatsuba for bd
# add together like above

def multiply(int1, int2):
    if int1 == 0 or int2 == 0:
        return 0
    elif int(math.log10(int1)) < 1 or int(math.log10(int2)) < 1:
        return int1 * int2
    else:
        n = int(math.ceil(min(len(str(int1)), len(str(int2)))/2)) 
        a = int(int1 / (10 ** n))
        b = int(int1 - a * (10 ** n))
        c = int(int2 / (10 ** n))
        d = int(int2 - c * (10 ** n))
        # pdb.set_trace()
        one = multiply(a, c)
        two = multiply((a+b), (c+d))
        three = multiply(b, d)
        result = (10 ** (n*2)) * one + 10 ** n * (two - one - three) + three
        return result

def get_int():
    int1 = input("First integer: ")
    int2 = input("Second integer: ")
    print(multiply(int(int1), int(int2)))

get_int()