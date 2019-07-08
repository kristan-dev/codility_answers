import random

class SolutionThree:
    @staticmethod
    def unique_sum_to_zero(input = None):
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


if(__name__ == "__main__"):
    print(SolutionThree.unique_sum_to_zero(input=4))