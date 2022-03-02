class Solution:

    def run(self, num):
        
        fib = []
        fib.append(0)
        fib.append(1)

        for i in range(2, num+1):
                fib.append(fib[i-1] + fib[i-2])

        return fib[num]


solution = Solution()
print(solution.run(10))
