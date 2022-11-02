import random

def MontyHallGame():
    winCount = 0
    for i in range(1, 101):
        doors = ['goat', 'goat', 'goat']
        doorNum = random.randint(0, 2)
        doors[doorNum] = 'car'
        if doors[1] == 'car' or doors [2] == 'car':
            winCount += 1
    return winCount

numWinList = []
for i in range(0, 100):
    numWinList.append(MontyHallGame())
numWinList.sort()

IQR = numWinList[74] - numWinList[24]
outliers = IQR * 1.5
bottomOutlier = numWinList[24] - outliers
topOutlier = numWinList[74] + outliers

overOutliers = 0
underOutliers = 0

for num in numWinList:
    if num > topOutlier:
        overOutliers += 1
    elif num < bottomOutlier:
        underOutliers += 1

average = sum(numWinList) / len(numWinList)

print('Bottom Outlier Number = ' + str(bottomOutlier))
print('Top Outlier Number = ' + str(topOutlier))
print('Number of outliers at the top: ' + str(overOutliers))
print('Number of outliers at the bottom: ' + str(underOutliers))
print('Average of times won: ' + str(average))
