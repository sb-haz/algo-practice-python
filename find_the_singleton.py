class Solution:
    
    def run(self, student_list):
        
        single_student_number = 0

        for num in student_list:
            if student_list.count(num) == 1:
                single_student_number = num
        print(single_student_number)
        
        return single_student_number

solution = Solution()
solution.run([2,4,5,4,2])