class Solution(object):
    def mergeSort(self, l1, l2):
        """
        :type l1: list of integers
        :type l2: list of integers
        :rtype: list of integers
        """
        merged = []
        i, j = 0, 0
        # Merge the two sorted lists while there are elements in both lists (Two sliders)
        while i < len(l1) and j < len(l2):
            # Compare the current elements of both lists
            if l1[i] < l2[j]:
                merged.append(l1[i])
                i += 1
            else:
                merged.append(l2[j])
                j += 1
            
        # If one of the lists is exhausted, append the remaining elements of the other list
            if i >= len(l1):
                merged.extend(l2[j:])
            elif j >= len(l2):
                merged.extend(l1[i:])
          
        return merged
    
# Example usage
solution = Solution()

print(solution.mergeSort([1, 3, 5], [2, 4, 6]))
print(solution.mergeSort([1, 5], [2, 3, 4]))
