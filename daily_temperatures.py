class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer=[]
        for i in range(len(temperatures)):
            n=1
            while(i+n<len(temperatures)):
                if(temperatures[i+n]>temperatures[i]):
                # print('i',i)
                # print('j',j)
                # print('j+n',j+n)
                    # diff=temperatures[i+n]-temperatures[i]
                    answer.append(n)
                    break
                elif(temperatures[i+n]<=temperatures[i] and i+n+1<len(temperatures)):
                    n=n+1
                else:
                    answer.append(0)
                    break
                # print('j+n - e', j+n)
                # if len(answer)==i+1:
                #       break

            if i==len(temperatures)-1:
                answer.append(0)
        return answer
