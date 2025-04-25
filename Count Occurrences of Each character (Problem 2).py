class Solution(object):
    def countOccurrences(self, s):
        """
        :type s: str
        :rtype: dict
        """
        # Create a dictionary to count occurrences of each character
        char_dict = {}
        # Loop through the string and count occurrences
        for letter in s:
            # Increase the count for the character in the dictionary
            if letter in char_dict:
                char_dict[letter] += 1
            else:
                char_dict[letter] = 1
        return char_dict
    
    
    
# Example usage
solution = Solution()
print(solution.countOccurrences("sapstar"))  
print(solution.countOccurrences("aaabbbbcc"))  
