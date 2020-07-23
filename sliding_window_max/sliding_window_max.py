'''
Input: a List of integers as well as an integer `k` representing the size of the sliding window
Returns: a List of integers
'''
import sys
# INT_MIN = -sys.maxsize -1

def sliding_window_max(arr, n, k):
    # Your code here
    # max_sum = INT_MIN
    max_upto = [0 for i in range(n)]
    # n = len(arr)
    s =[]
    s.append(0)

    for i in range(1,n):
        while (len(s) > 0 and arr[s[-1]] < arr[i]):
            max_upto[s[-1]] = i - 1
            del s[-1]

            s.append(i)

        while(len(s) > 0):
            max_upto[s[-1]] = n -1
            del s[-1]

        j = 0
        for i in range(n -k + 1):
            while(j < i or max_upto[j] < i + k -1):
                j += 1
                print (arr[j], end=" ")
            print()


    #     for x in range(k):
    #         current = current + arr[i + x]

    #     max_sum = max(current, max_sum)

    # return max_sum


if __name__ == '__main__':
    # Use the main function here to test out your implementation 
    arr = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    n = len(arr)
    
    print(sliding_window_max(arr, n, k))

    # print(f"Output of sliding_window_max function is: {sliding_window_max(arr, k)}")
