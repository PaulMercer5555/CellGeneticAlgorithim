import random as rand
import math
from config import Config
import food

def createCells(cellList):
    for x in range(Config.initialCellNum):
        cellList.append(Cell(x,Config.randAllele(0),Config.randAllele(0), (rand.randint(0, math.ceil(Config.screenSize/Config.simulationScale)), rand.randint(0, math.ceil(Config.screenSize/Config.simulationScale)))))
    return(cellList)

class Cell:

    def __init__(self,name,parent1,parent2, coordinates):
        self.name = f"cell,{name}"
        self.coordinates = coordinates
        self.size = (Config.cellWidth*Config.simulationScale, Config.cellHeight*Config.simulationScale)
        self.color = Config.cellColor
        self.energyLevel = Config.cellStartingEnergy
        self.visionRadius = Config.cellVisionRadius*Config.simulationScale
        self.weight = 0
        self.genes = {
            "gene1": parent1["gene1"],
            "gene2": parent1["gene2"],
            "gene3": parent2["gene1"],
            "gene4": parent2["gene2"],
        }
    # region Cell Basic Function
    def energyCheck(self):
        if self.energyLevel <= 0:
            return True
        else:
            return False

    def loseEnergy(self, energyLoss):
        self.energyLevel -= energyLoss
        return

    def eatFood(self,food_item):
        self.energyLevel += Config.foodEnergy
        food.createFood(food_item)
        for obj in Config.foodList:
            if obj.name == food_item.name:
                Config.foodList.remove(obj)
                break
        del(food_item)
        return

    def breed(self,cell1):
        name=self.name
        Lcoordinates = list(self.coordinates)
        Lcoordinates[0] += Config.simulationScale
        coordinates = tuple(Lcoordinates)
        Cell(name,self.genes,cell1.genes,coordinates)
        Lcoordinates = list(self.coordinates)
        Lcoordinates[0] -= Config.simulationScale
        coordinates = tuple(Lcoordinates)
        self.coordinates = coordinates
    # endregion

    def Move(self,direction):
        if direction == "UP":
            y = list(self.coordinates)
            y[1] += Config.simulationScale
            self.coordinates = tuple(y)
        elif direction == "DOWN":
            y = list(self.coordinates)
            y[1] -= Config.simulationScale
            self.coordinates = tuple(y)
        elif direction == "LEFT":
            x = list(self.coordinates)
            x[0] -= Config.simulationScale
            self.coordinates = tuple(x)
            Config.leftExecutionCount += 1
        elif direction == "RIGHT":
            x = list(self.coordinates)
            x[0] += Config.simulationScale
            self.coordinates = tuple(x)

        return

    def decisionMaker(self):
        gene1Output = self.weight + self.genes["gene1"]
        gene2Output = self.weight + self.genes["gene2"]
        gene3Output = self.weight + self.genes["gene3"]
        gene4Output = self.weight + self.genes["gene4"]

        totalOutput = gene1Output + gene2Output + gene3Output + gene4Output
        #print(totalOutput)

        if totalOutput > 0:
            if totalOutput < 50:
                self.Move("UP")
            elif totalOutput < 100:
                self.Move("DOWN")
        else:
            #if totalOutput > -50:
            #    self.Move("LEFT")
            #    Config.leftCount += 1
            if totalOutput > -100:
                self.Move("RIGHT")
        return

    # region Input Functions
    def visualInput(self,foodList,cellList):
        weight = 0
        visionRadius = self.visionRadius
        coordinates = self.coordinates
        for i in range(visionRadius):
            x = coordinates[0] - visionRadius
            y = coordinates[1] - visionRadius
            while (x <= coordinates[0] + visionRadius):
                y = coordinates[1] - visionRadius
                while (y <= coordinates[1] + visionRadius):
                    weight += Config.visualWeight(self,cellList,(x,y))
                    weight += Config.visualWeight(self,foodList,(x,y))
                    y += Config.simulationScale
                x += Config.simulationScale
        return (weight)

    def selfCoordinatesToWeight(self):
        coordinates = self.coordinates
        weight = 0
        weight += coordinates[0]
        weight += coordinates[1]
        return (weight)

    def energyLevelToWeight(self):
        energyLevel = self.energyLevel
        weight = 0
        weight += energyLevel
        return(weight)
    # endregion

    def Brain(self):
        if self.coordinates[0] < 0:
            x = list(self.coordinates)
            x[0] += Config.screenSize
            self.coordinates = tuple(x)
        for obj1 in Config.foodList:
            if self.coordinates == obj1.coordinates:
                self.eatFood(obj1)
                break
            else:
                continue

        for obj1 in Config.cellList:
            if self.coordinates == obj1.coordinates:
                self.breed(obj1)
                break
            else:
                continue

        if self.energyCheck():
            Config.cellList.remove(self)
            del self
            return

        self.weight = 0
        self.weight += self.visualInput(Config.foodList,Config.cellList)
        self.weight += self.selfCoordinatesToWeight()
        self.weight += self.energyLevelToWeight()

        self.decisionMaker()

        self.loseEnergy(Config.energyLossPerTick)


