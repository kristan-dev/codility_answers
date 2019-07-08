import random

class SolutionFour:
    @staticmethod
    def smallest_pos_int(A = None):
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

if(__name__ == "__main__"):
    input = [-1, -3]
    SolutionFour.smallest_pos_int(A=input)
    print("done")