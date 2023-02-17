''' 
Example input
a = [6, 1, 4, 6, 3, 2, 7, 4]
k = 3
l = 2
'''
def findMaximumApples( A, k, l):
    ans1 = findMaximumApples(A, k, l)
    ans2 = findMaximumApples(A, l, k)
    return max(ans1, ans2)

def findMaximumApples( A, k, l):
    print(k, l)
    if k + l > len(A):
        return -1
    sum = [None]*1000
    sum[0] = A[0]
    i = 1
    while i < len(A):
        sum[i] = sum[i - 1] + A[i]
        i += 1
    max = -1
    x = 0
    y = 0
    z = 0
    while z + k - 1 < len(A):
        if z > 0:
            x = sum[z + k - 1] - sum[z - 1]
        else:
            x = sum[z + k - 1]
        b=a+k
        while b + l - 1 < len(A):
            if b > 0:
                y = sum[b + l - 1] - sum[b - 1]
            else:
                y = sum[b + l - 1]
            if x + y > max:
                max = x + y
            b += 1
        z += 1
    return max
