
class BinaryGapRegex:
    @staticmethod
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
    BinaryGapRegex.solution_five(10)
    print("done")