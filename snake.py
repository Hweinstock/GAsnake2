from food import food
from nn import NeuralNetwork
import math as m

screen_w = 600
screen_h = 600

class snake:
    
    def __init__(self, nn, col, dir):
        self.direction = dir
        self.w = screen_w/50
        self.h = screen_h/50
        self.x = screen_w/2 - self.w
        self.y = screen_h/2 - self.h
        self.tailLength = 4
        self.tail = []
        self.col = col
        self.moveNum = 1
        self.dead = False
        self.fitness = 0
        self.maxMoves = 300
        self.best = False
        self.food = food(col)
        self.sinceFood = 0
        
        if nn == None:
            self.nn = NeuralNetwork(4, 6, 3)
        else:
            self.nn = nn
    
    def reset(self):
        self.x = screen_w/2 - self.w
        self.y = screen_h/2 - self.h
        self.tailLength = 4
        self.tail = []
        self.moveNum = 1
        self.dead = False
        self.fitness = 0
        self.food = food(self.col)
        self.best = False
        self.food.best = False
        self.sinceFood = 0
        
    def show(self):
        if self.best:
            fill(255)
        else:
            fill(color(self.col[0], self.col[1], self.col[2]))
        rect(self.x, self.y, self.w, self.h)
    
    def kill(self):
        self.dead = True
    
    def checkBounds(self, x, y):
        if x > screen_w-self.w or x < 0:
            return True
        if y > screen_h-self.h or y < 0:
            return True
        return False
    
    def checkDirection(self, ang):
        newC = [(self.x + self.w*round(cos(self.direction + ang))), (self.y+self.h*round(sin(self.direction + ang)))]
        if self.checkBounds(newC[0], newC[1]) or [t for t in self.tail if t == newC] != []:
            return 0.0
        return 1.0    
    
    def dirFood(self):
        relX = self.x - self.food.x
        relY = self.food.y - self.y
        absoluteAngle = atan2(relY, relX) % TAU
        relTurn = (absoluteAngle - self.direction) % TAU
        return relTurn / TAU
    
    def checkFoodDirection(self, ang):
        dir = self.direction + ang
        tx = self.x * 1
        ty = self.y * 1
        while not self.checkBounds(tx, ty):
            tx += round(cos(dir))
            ty += round(sin(dir))
            if tx == self.food.x and ty == self.food.y:
                return 0
        return 1
    
    def findDistances(self):
        
        left = self.checkDirection(PI/2)
        right = self.checkDirection(-PI/2)
        straight = self.checkDirection(0)
        
        # food_left = 1
        # food_right = 1
        # food_straight = 1
        
        # if self.x == self.food.x or self.y == self.food.y:
        #     food_left = self.checkFoodDirection(PI/2)
        #     food_right = self.checkFoodDirection(-PI/2)
        #     food_straight = self.checkFoodDirection(0)
        
        # o = [left, straight, right, food_left, food_right, food_straight]
        
        fv = self.dirFood()
        o = [left, straight, right, fv]

        return o
            
    def updateDirection(self):

        pDirections = [-PI/2, 0, PI/2]
        outputs = self.nn.feedForward(self.findDistances()).toVector()
        guess = pDirections[outputs.index(max(outputs))]
        self.direction += guess 
        self.moveNum += 1
    
    def updateTail(self):

        if len(self.tail) < self.tailLength:
            self.tail.append([self.x, self.y])
        else:
            self.tail.append(self.tail.pop(0))
            self.tail[-1] = [self.x, self.y]
            
    def displayTail(self):
        if self.best:
            fill(255)
        else:
            fill(color(self.col[0], self.col[1], self.col[2]))
        for t in self.tail:
            if t[0] == self.x and t[1] == self.y and len(self.tail) != 1:
                self.kill()
            else:
                rect(t[0], t[1], self.w, self.h)
                
    def updateFood(self):
        self.food.update()

        if self.x == self.food.x and self.y == self.food.y:
            self.tailLength += 1
            self.fitness += 30
            self.sinceFood = 0
            self.food.respawn()
            
    def updateFitness(self, oldD):
        self.fitness += 0.01
        newD = sqrt((self.x - self.food.x)**2 + (self.y - self.food.y)**2)
        if newD > oldD:
            self.fitness += 0.0
        if oldD > newD:
            self.fitness -= 0
        
    def update(self):
        
        if not self.dead:
            if self.tailLength > 0:
                self.updateTail()
                
            distanceToFood = sqrt((self.x - self.food.x)**2 + (self.y - self.food.y)**2)

            if self.checkBounds(self.x, self.y) or self.sinceFood > 300:
                self.kill()
                
            # elif self.moveNum >= self.maxMoves:
            #     self.fitness += 10
            #     self.kill()
                
            else:
                self.updateDirection()
                self.x += self.w*round(cos(self.direction))
                self.y += self.h*round(sin(self.direction))
                self.show()
                self.displayTail()
                self.sinceFood += 1
                self.updateFitness(distanceToFood)
                
                self.updateFood()
        
        
        
    
