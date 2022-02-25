import random

fullstack = ["tadiwanashe","tawanda","tanya","diana","anesu","precell"]

teamA = []
teamB = []
teamC = []

for i in range(2):
    one = random.choice(fullstack)
    teamA.append(one)
    fullstack.remove(one)

for i in range(2):
    one = random.choice(fullstack)
    teamB.append(one)
    fullstack.remove(one)

for i in range(2):
    one = random.choice(fullstack)
    teamC.append(one)
    fullstack.remove(one)    

print(teamA) 
print(teamB)  
print(teamC)  