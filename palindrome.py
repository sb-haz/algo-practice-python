class Solution:
    
    def run(self, word):
        return True if word[::-1] == word else False 
    
solution = Solution()
print(solution.run("madam"))