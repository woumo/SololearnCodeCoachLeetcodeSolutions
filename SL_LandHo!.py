"""You are on a large ship and you put down anchor near a beautiful beach. There is a small boat ferrying passengers back and forth, and you get in line for it. How long will you have to wait to get to the beach? You know that 20 people can fit on the boat and each trip to shore takes 10 minutes each way.

Task: 
Determine your wait time if you know the total number of people ahead of you in line.  

Input Format: 
An integer that represents the total number of people ahead of you in line.

Output Format: 
An integer that represents the number of minutes that you will have to wait until you are standing on the beach.

Sample Input: 
15

Sample Output: 
10"""

# I DONT GET THIS
people_ahead = int(input())
waiting_time = 10

while people_ahead >= 20:
    waiting_time += 20
    people_ahead -= 20

print(waiting_time)


