import pdb

def collatz(n, step):
    if n == 1:
        print(step)
    elif n % 2 == 0:
        n = n / 2
        step += 1
        collatz(n, step)
    else:
        n = 3 * n + 1
        step +=  1
        collatz(n, step)


def main():
    num = input("Integer: ")
    if int(num) > 0:
        collatz(int(num), 0)
    else:
        main()

main()
