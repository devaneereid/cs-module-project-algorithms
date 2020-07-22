'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
import sys
INT_MIN = -sys.maxsize -1

def sliding_window_max(nums, k):
    # Your code here
    max_num = INT_MIN

    for i in range(len(nums) - k + 1):
        current = 0

        for x in range(k):
            current = current + nums[i + x]

        max_num = max(current, max_num)

    return max_num


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    
    # print(sliding_window_max(arr, k))

    print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
