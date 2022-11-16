"""You need to calculate the sum of all the multiples of 3 or 5 below a given number.

Task: 
Given an integer number, output the sum of all the multiples of 3 and 5 below that number. 
If a number is a multiple of both, 3 and 5, it should appear in the sum only once.

Input Format: 
An integer.

Output Format: 
An integer, representing the sum of all the multiples of 3 and 5 below the given input.

Sample Input: 
10

Sample Output:
23"""


num = int(input())
nums = list(range(1, num))

solutionList = []
suma = 0

for i in range(len(nums)):
    if nums[i] % 3 ==0 or nums[i] % 5 == 0:
        solutionList.append(nums[i])
        suma += nums[i]

print(suma)
