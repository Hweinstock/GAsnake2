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
        self.food = food(col)
        self.fitness = 0
        self.maxMoves = 300
        
        if nn == None:
            self.nn = NeuralNetwork(5, 6, 3)
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
        
    def show(self):
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
        newC = [(self.x + round(cos(self.direction + ang))), (self.y+round(sin(self.direction + ang)))]
        if self.checkBounds(newC[0], newC[1]) or [t for t in self.tail if t == newC] != []:
            return 0.0
        return 1.0
      
    def findDistances(self):

        left = self.checkDirection(PI/2)
        right = self.checkDirection(-PI/2)
        straight = self.checkDirection(0)
    
        fx = (self.food.x - self.x)
        fy = (self.food.y - self.y)
        #fv = abs(self.direction - atan2(fy, fx))
    
        o = [left, straight, right, fx/screen_w, fy/screen_h]
        #o = [(fv+PI)/(2*PI)]
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
        for t in self.tail:
            if t[0] == self.x and t[1] == self.y and len(self.tail) != 1:
                self.kill()
            else:
                fill(color(self.col[0], self.col[1], self.col[2]))
                rect(t[0], t[1], self.w, self.h)
                
    def updateFood(self):
        self.food.update()

        if self.x == self.food.x and self.y == self.food.y:
            self.tailLength += 1
            self.fitness += 30
            self.food.respawn()
            
    def updateFitness(self, oldD):
        #self.fitness += 1
        newD = sqrt((self.x - self.food.x)**2 + (self.y - self.food.y)**2)
        if newD > oldD:
            self.fitness += 1.0
        if oldD > newD:
            self.fitness -= 1.5
        
    def update(self):
        
        if not self.dead:
            if self.tailLength > 0:
                self.updateTail()
                
            distanceToFood = sqrt((self.x - self.food.x)**2 + (self.y - self.food.y)**2)

            if self.checkBounds(self.x, self.y) or self.fitness < 0:
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
                    
                self.updateFitness(distanceToFood)

                self.updateFood()
        
        
        
    
