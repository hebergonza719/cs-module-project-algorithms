'''
Input: an integer
Returns: an integer
'''
def eating_cookies(n, cache=None):
    # Your code here
    if n <= 0:
        return 1
    elif n <= 2:
        return n
    # checks if there is a cache and if cache[i] has a value other than 0
    elif cache and cache[n] > 0:
        return cache[n]
    else:
        if cache == None:
            cache = [0 for x in range(n + 1)]
            cache[1] = 1
            cache[2] = 2
        cache[n] = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    return cache[n]
        
    # return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)

if __name__ == "__main__":
    # Use the main function here to test out your implementation
    num_cookies = 5

    print(f"There are {eating_cookies(num_cookies)} ways for Cookie Monster to each {num_cookies} cookies")
