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

"""
python에서 문자열을 다른 언어에 비해 자유롭게 쓸수 있다는 점에서 편하게 생각할 수 있었다.
문자열 붙이기를 사용하여 반복되지 않은 문자가 추가되었을때는 (기존문자열 + 새로운문자)로 추가
반복된 문자가 추가 되었을때는 []인덱싱으로 추가해주었다.

헷갈린 점 반복된 문자가 추가되었을 시에 인덱싱 범위를 정해주는 것에서 헷갈렸다. -> 처음에는 반복된 문자를 지워주었음. -> 이후 반복된 문자 뒤에서부터만 챙기면 된다는 것을 깨닫고 .find로 찾은 인덱스 뒤부터 [+1:]로 새로운 문자열을 생성해주었다.
꼼꼼해야 할 점 문자열이 = " "일때. 문자열이 반복되는 것이 없을때.(기본형)
"""