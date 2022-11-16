"""You are trying to determine which of two apartments has a larger balcony. Both balconies are rectangles, and you have the length and width, but you need the area.

Task
Evaluate the area of two different balconies and determine which one is bigger.

Input Format
Your inputs are two strings where the measurements for height and width are separated by a comma. The first one represents apartment A, the second represents apartment B.

Output Format:
A string that says whether apartment A or apartment B has a larger balcony.

Sample Input
'5,5'
'2,10'

Sample Output
Apartment A"""


A = input("A: ")
B = input("B: ")

A = A.split(sep=",")
B = B.split(sep=",")

areaA = int(A[0]) * int(A[1])
areaB = int(B[0]) * int(B[1])

if areaA > areaB:
    print("Apartment A")
elif areaA < areaB:
    print("Apartment B")
