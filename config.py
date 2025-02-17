import random as rand
import math

class Config:
    # region Simulation Configuration
    screenSize = 100
    tickPerSec = 60
    simulationScale = 1
    leftCount = 0
    leftExecutionCount = 0
    # endregion

    # region Cell Configuration
    initialCellNum = 100
    cellColor = 'cyan'
    cellWidth = 1
    cellHeight = 1
    cellVisionRadius = 3
    cellStartingEnergy = 10
    energyLossPerTick = 1
    cellCoordinateWeightScaler = 150
    cellEnergyWeightScaler = 50
    # endregion

    # region Food Configuration
    initialFoodNum = 800
    foodColor = 'darkgoldenrod1'
    foodWidth = 1
    foodHeight = 1
    foodEnergy = 10
    # endregion

    # region Delta Variables
    cellNum = initialCellNum
    foodNum = initialFoodNum
    cellList = []
    foodList = []
    # endregion

    # region Common Functions
    def randAllele(bruh):
        allele = {
            "gene1": rand.random()*float(rand.randrange(-50,50)),
            "gene2": rand.random()*float(rand.randrange(-50,50)),
        }
        return allele

    def visualWeight(obj1, objList, lookCoords):
        weight = 0
        for obj2 in objList:
            if lookCoords == obj2.coordinates:
                if obj1.coordinates[0] < lookCoords[0]:
                    if obj1.coordinates[1] < lookCoords[1]:
                        weight += 10
                    elif obj1.coordinates[1] > lookCoords[1]:
                        weight += 10
                elif obj1.coordinates[0] > lookCoords[0]:
                    if obj1.coordinates[1] < lookCoords[1]:
                        weight -= 10
                    elif obj1.coordinates[1] > lookCoords[1]:
                        weight -= 10
                continue
            else:
                continue
        return weight
    # endregion

