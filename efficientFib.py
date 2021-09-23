def fib_efficient(n, d):
    global numOfTimes
    numOfTimes += 1
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

numOfTimes = 0
d = {1:1, 2:2}
print("fib efficient:",fib_efficient(12, d))
print('number of times the function calls', numOfTimes)