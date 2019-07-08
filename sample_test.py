import random
import numpy as np

def solution_one(A):
    ''' Returns a smallest element in a given int array '''
    big = max(A)
    small = min(A)

    print(small)

def solution_two(A):
    '''Returns a string of length N consisting of alternating characters: "+" and "-", starting with a "+" character. You can assume N is between 1 and 100.'''
    result = ""

    for i in range(0, A, 1):
        if((i%2) == 0):
            result = result+"+"
        else:
            result = result+"-"
    
    return result

def solution_three(input):
    ''' given an integer N (1 ≤ N ≤ 100), returns an array containing N unique integers that sum up to 0. The function can return any such array. '''
    while(True):
        result = []
        for i in range(0, input, 1):
            # rand_num = np.random.randint(-10, 10)
            rand_num = random.randint(-10, 10)
            if(not(rand_num in result)):
                result.append(rand_num)
        check_val = sum(result)
        if(check_val == 0):
            break
    return result

def solution_four(A):
    ''' given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A '''
    big = max(A)
    while(True):
        smallest_pos_int = random.randint(1, 100000)
        if(not(smallest_pos_int in A)):
            if(smallest_pos_int < big):
                return smallest_pos_int
            else:
                if(big>0):
                    distance = smallest_pos_int - big
                    if(distance == 1):
                        return smallest_pos_int
                if(big<0):
                    temp = abs(big)
                    distance = smallest_pos_int - temp
                    if(distance == 0):
                        return smallest_pos_int

def solution_five(N):
    '''given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.'''
    bin_num = '{0:08b}'.format(N)
    binary_gaps = []
    counter = 0
    count_check = False
    for i in range(0, len(bin_num)-1, 1):
        pos1 = bin_num[i]
        pos2 = bin_num[i+1]
        if(count_check == True):
            if(bin_num[i] == '0'):
                counter = counter + 1
            else:
                binary_gaps.append(counter)
                counter = 0
                count_check = False
        else:
            if(bin_num[i] == '1'):
                if(bin_num[i+1] == '0'):
                    count_check = True
                    continue

    if(len(binary_gaps)>0):
        return max(binary_gaps)
    else:
        return 0


if(__name__ == "__main__"):
    # solution_one([1, 2, 3, 4, 5])
    # print(solution_two(5))
    # print(solution_three(4))
    # input = [-1, -3]
    # print(solution_four(input))
    # print(solution_five(15))
    print("done")