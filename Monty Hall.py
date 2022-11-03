import random

#The actual game: 
def MontyHallGame():
    winCount = 0
    for i in range(0, 100):
        doors = ['goat', 'goat', 'goat']
        doorNum = random.randint(0, 2)
        doors[doorNum] = 'car'
        """
        We check if a car is in both 2 or 3 because we are trying to find if the player switches every time from door 1 to door 2 or 3, what the odds of winning is. 
        Since we know that we are going to pick, 2 or 3 - whichever door that the host doesn't open - then we know that if the car is behind either of the two doors, we will win. 
        """
        if doors[1] == 'car' or doors [2] == 'car':
            winCount += 1
    return winCount

#playing the game 10,000 times and sorting the total win counts in order from least to greatest
numWinList = []
dataRange = 10000
for i in range(0, dataRange):
    numWinList.append(MontyHallGame())
numWinList.sort()

#calculate the IQR and determine what would be an outlier.
thirdQuartile = int(dataRange - dataRange / 4)
firstQuartile = int(dataRange / 4)
IQR = numWinList[thirdQuartile] - numWinList[firstQuartile]
outliers = IQR * 1.5
topOutlier = numWinList[thirdQuartile] + outliers
bottomOutlier = numWinList[firstQuartile] - outliers

#calculate how many outliers exist if any.
overOutliers = 0
underOutliers = 0
for num in numWinList:
    if num > topOutlier:
        overOutliers += 1
    elif num < bottomOutlier:
        underOutliers += 1

#calculate the average amount of wins which is roughly equivalent to the probability of winning by switching doors. 
average = sum(numWinList) / len(numWinList)

#output results
print('Bottom Outlier Number = ' + str(bottomOutlier))
print('Top Outlier Number = ' + str(topOutlier))
print('Number of outliers at the top: ' + str(overOutliers))
print('Number of outliers at the bottom: ' + str(underOutliers))
print('Average of times won: ' + str(average))
