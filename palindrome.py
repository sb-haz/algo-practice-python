class Solution:
    
    def run(self, word):
        lowercaseWord = word.lower()
        return True if lowercaseWord[::-1] == lowercaseWord else False 
    
solution = Solution()
print(solution.run("Madam"))