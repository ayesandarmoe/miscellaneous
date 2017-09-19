#https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    # your code goes here
    cnt = len("{0:b}".format(number))
    for n in range(1,number+1):
        print "{0:{align}{width}d} {0:{align}{width}o} {0:{align}{width}X} {0:{align}{width}b}".format(n, align=">",width=cnt)

if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)
