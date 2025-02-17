from config import Config
import random

def createFoods(foodList):
    for x in range(Config.initialFoodNum):
        foodList.append(Food(x))
    return(foodList)
def createFood(food_item):
    Config.foodList.append(Food(food_item.name))
    return
class Food:
    def __init__(self, name):
        self.name = f"food,{name}"
        self.coordinates = (random.randint(0, Config.screenSize), random.randint(0, Config.screenSize))
        self.size = (Config.foodWidth, Config.foodHeight)
        self.color = Config.foodColor

    def foodList(self):
        return self.name, self.coordinates