'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    # Your code here
    # single = 0
    # for i in arr:
    #     count = 0
    #     for j in arr:
    #         if j == i:
    #             count += 1
    #     if count == 1:
    #         single = i
    
    # return single
    counts = dict()
    for i in arr:
        # if counts.get(i) didn't exist, it would be 0
        # hence the get(i, 0)
        # if it does exist, you add one to it
        counts[i] = counts.get(i, 0) + 1

    for x, y in counts.items():
        if y == 1:
            return x


if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")