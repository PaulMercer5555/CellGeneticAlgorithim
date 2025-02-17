import cell
import food
import pygame as pyg
from config import Config

pyg.init()
screen = pyg.display.set_mode((Config.screenSize, Config.screenSize))
clock = pyg.time.Clock()
clock.tick(Config.tickPerSec)
running = True

Config.cellList = cell.createCells(Config.cellList)
Config.foodList = food.createFoods(Config.foodList)

def main():
    Config.leftExecutionCount =0
    screen.fill('black')
    drawCells(Config.cellList)
    drawFoods(Config.foodList)
    for obj in Config.cellList:
        obj.Brain()
    pyg.display.flip()
    #print(Config.leftExecutionCount, len(Config.cellList))

    # return()

def drawCells(cellList):
    for obj in cellList:
        pyg.draw.rect(screen, obj.color, (obj.coordinates,obj.size))
def drawFoods(foodList):
    for obj in foodList:
        pyg.draw.rect(screen, obj.color, (obj.coordinates,obj.size))

while running:

    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    main()