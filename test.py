n = int(input())

m = int(input())


def q1(b):
    return [1]*len(b)
def q2(b):
    for i in range(1, len(b)+1, 2):
        b[i] = 0
    return b
def q3(b):
    for i in range(0, len(b)+1, 2):
        b[i] = 0
    return b
def q4(b):
    return [0]*len(b)


buckets = [0]*n



for query in range(m):

    q = int(input())

    if q == 1:
        q1(buckets)
    elif q == 2:
        q1(buckets)
    elif q == 3:
        q1(buckets)
    elif q == 4:
        q1(buckets)

count = 0

for i in buckets:
    if i > 0:count += 1

return count