'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
    print(n)
    # base cases
    if n < 0:
        return 0
    elif n == 0:
        return 1
    # check if the work has already been done by looking in the cache
    elif cache is not None and cache[n] > 0:
        # return the previous computed answer and don't recurse
        return cache[n]
    else: 
        # might need to create our cache for the first time
        # store the value of the recursive call expressions in our cache
        if cache is None:
            #initialize an empty list for a cache
            cache = [0 for i in range(n+1)]

        cache[n] = eating_cookies(n-1, cache) + eating_cookies(n-2, cache) + eating_cookies(n-3, cache)

    return cache[n]


eating_cookies(20)

    # print(n)
    # if n == 0:
    #     return 1 
    # if n <= 0:
    #     return 0
    # return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(eating_cookies(num_cookies))
    # print(num_cookies)

    # print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
