class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        last = str()
        maxNum = 0
        maxCurrent =0
        if len(s)==1:
            return 1
        for i in s:
            if i in last:
                index_n = last.find(i)
                last = last[index_n+1:]
                last= last+i
                maxCurrent=len(last)
            else: 
                last = last+i
                print(last)
                maxCurrent +=1
                print(maxCurrent)
                if maxCurrent>maxNum:
                    maxNum = maxCurrent
        if maxCurrent>maxNum:
            maxNum = maxCurrent
        return(maxNum)
                        
s= Solution()

length_of_subset = s.lengthOfLongestSubstring("abcdabc")
print(length_of_subset)