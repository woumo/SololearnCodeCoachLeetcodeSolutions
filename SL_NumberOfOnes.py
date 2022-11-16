"""Task:
Count the number of ones in the binary representation of a given integer.

Input Format:
An integer.

Output Format: 
An integer representing the count of ones in the binary representation of the input.

Sample Input:
9

Sample Output:
2"""


num = int(input())
inbin = bin(num)[2::]

print(inbin.count("1"))

