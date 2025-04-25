class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Create the frequency list of 26 character
        freq = [0] * 26
        for letter in s:
            # Increase the value at the index corresponding to the character order
            freq[ord(letter) - ord('a')] += 1
            
        # Loop through the string again and find out first with frequency of 1
        for letter in s:
            if freq[ord(letter) - ord('a')] == 1:
                return letter
        
        return None # If no unique character is found, return None
    
    
# Example usage
solution = Solution()
print(solution.firstUniqChar("sapstar"))  
print(solution.firstUniqChar("aabbcc"))  
