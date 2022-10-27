""" Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M. 

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

 

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].


"""

### MY INITIAL SOLUTION ###
class Solution:
    def __init__(self):
        #set up a dictionary mapping from roman numerals to integers 
        self.code = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        #set up a list of all the pairs of roman numerals with peculiar meanings 
        self.doubles = ['IV', 'XL', 'CD', 'IX', 'XC', 'CM']  
        #create a variable called skip which will dictate whether or not a character should be skipped over 
        self.skip = False 
        #a variable which will finally be the integer which the roman numerals denote 
        self.num = 0 
    
    def romanToInt(self, s): 
        #turn the string into a list for ease of computation 
        numerals = list(s)

        #loop through
        for idx, letter in enumerate(numerals): 
            if self.skip:
                #set skip to false so that it does not continously keep skipping all characters
                self.skip = False 
                #skip over the present character 
                continue 
            
            #if we are not at the penultimate character 
            if idx != len(numerals) - 1:
                #then create a cell with the current two characters used later to check if they're a special pair 
                cell = numerals[idx] + numerals[idx+1]  
            else: 
                #otherwise add the total tally and the final character 
                self.num += self.code[letter] 
                continue 

            if cell not in self.doubles:
                #if the cell is not special then add the 
                self.num += self.code[letter] 
            else:
                #otherwise add the number accorindly 
                self.num += self.code[cell[1]] - self.code[cell[0]] 
                #set the variable to skip so that the second character in the cell is not added 
                self.skip = True         
        
        return self.num 


num = Solution().romanToInt('LVIII')

### ONLINE SOLUTION ###

class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000} 
        sum = 0 
        
        for letter in range(len(s)-1,-1,-1):
            num = roman[s[letter]] 

            if num*3 < sum:
                sum -= num 
            else:
                sum += num 
        
        return sum 

num = Solution().romanToInt('MCMXCIV') 

pass 

