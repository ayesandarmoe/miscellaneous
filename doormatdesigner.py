# https://www.hackerrank.com/challenges/designer-door-mat?utm_campaign=challenge-recommendation&utm_medium=email&utm_source=24-hour-campaign


N, M = map(int,raw_input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
for i in xrange(1,N,2): 
    print '{:-{align}{width}}'.format(i * '.|.', align='^',width=M)
print '{:-{align}{width}}'.format('WELCOME', align='^',width=M)
for i in xrange(N-2,-1,-2): 
    print '{:-{align}{width}}'.format(i * '.|.', align='^',width=M)
