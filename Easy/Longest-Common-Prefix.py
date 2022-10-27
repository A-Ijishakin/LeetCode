""" Write a function to find the longest common prefix string amongst an array of strings 
If there is no common prefix, return an empty string 

Input: strs = ["flower","flow","flight"]
Output: "fl" 

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

"""
#create a dictionary of strings which may be tested 
tests = {'1': ["cir","car"], '2': ["flower","flow","flight"], '3':["dog","racecar","car"],  '4': ["reflower","flow","flight"],
         '5': ["flower","fkow"], '6': ["aaa","aa","aaa"], '7': ["c","acc","ccc"],'8': ['a'], '9': ['a', 'ab']}  

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str: 
        #pre-set the prefix to be the shortest string in the list of strings 
        prefix = min(strs, key=len) 
        #then remove that string 
        strs.remove(prefix) 
        #
        lack = False
        #if the list isn't empty (needed in the case where there's only one string in the list)
        if strs:
            for word in strs:
                #get the index where the previous prefix and the current word stop corresponding at, loop in the shortest range between the two 
                pre = [idx for idx in range(len(min(word, prefix, key=len))) if word[idx] != prefix[idx]] 
                #if there is total correspondence then skip this word 
                if len(pre) == 0:
                    continue 
                #if there is no correspondence then note the lack of correspondence and then skip this word 
                if pre[0] == 0: 
                    lack = True
                    continue 
                else:
                    #otherwise set the prefix to the current word up until the point of no correspondence 
                    prefix = word[:pre[0]]   
                
            #if any word does not share any of prefix with other words or the prefix is not found in any word in the list
            if lack or not any(prefix in word for word in strs):
                #then return an empty string 
                prefix = ''
        
        return prefix 


Prefix = Solution().longestCommonPrefix(tests['1']) 

pass 

