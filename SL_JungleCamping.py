"""You are camping alone out in the jungle and you hear some animals in the dark nearby. Based on the noise they make, determine which animals they are.

Task: 
You are given the noises made by different animals that you can hear in the dark, evaluate each noise to determine which animal it belongs to. Lions say 'Grr', Tigers say 'Rawr', Snakes say 'Ssss', and Birds say 'Chirp'.

Input Format: 
A string that represent the noises that you hear with a space between them.

Output Format: 
A string that includes each animal that you hear with a space after each one. (animals can repeat)

Sample Input: 
Rawr Chirp Ssss

Sample Output: 
Tiger Bird Snake"""


line = input()
line = line.split(" ")
endLine = []

for i in range(len(line)):
    if line[i] == "Grr":
        endLine.append("Lion")
    elif line[i] == "Rawr":
        endLine.append("Tiger")       
    elif line[i] == "Ssss":
        endLine.append("Snake")
    elif line[i] == "Chirp":
        endLine.append("Bird")
   
print(" ".join(endLine))