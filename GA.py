from snake import snake
import copy as c
screen_width = 600.0
screen_height = 600.0

def randomColor():
    return (random(0, 255), random(0, 255), random(0, 255))

def listSum(l):
    if l == []:
        return 0
    return l[0] + sum(l[1:])

class brain:

    def __init__(self, genSize):
        self.gen = 1
        self.genSize = genSize
        self.cutOff = 0.2
        self.mutationRate = 0.2
        self.snakes = self.generateSnakes()
        self.mutationDelta = 1
        self.bestFitness = 0
        self.average = 0
        self.bests = []
        self.averages = []
        self.bestFoodScore = 0

    def generateSnakes(self, newGen = []):
        if self.gen == 1:
            return [snake(None, randomColor(), self.randomDirection()) for i in range(self.genSize)]
        else:
            if self.gen > 100:
                for snek in newGen:
                    snek.sinceFoodCap = 2500
            return newGen

    def randomDirection(self):
        pDirections = [3*PI/2, 0, PI/2, PI]
        return pDirections[floor(random(len(pDirections)))]

    def averageFitness(self):
        fSum = 0
        for s in self.snakes:
            fSum += s.fitness

        return fSum/len(self.snakes)

    def update(self):
        if self.checkDead():
            self.gen+=1
            self.average = self.averageFitness()
            self.sortFitness()
            self.best = c.deepcopy(self.snakes[0])
            self.bestFitness = self.best.fitness
            self.bestFoodScore = self.best.tailLength - 4
            self.bests.append(self.bestFitness)
            self.averages.append(self.average)
            self.snakes = self.birth(self.snakes[:ceil(self.genSize*self.cutOff)])
            self.update()
        else:
            for s in [s for s in self.snakes if not s.dead]:
                s.update()

    def checkDead(self):
        for s in self.snakes:
            if s.dead == False:
                return False
        else:
            return True
    
    def mutate(self, v):
        return random(-1.0/v, 1.0/v)
        #return v + random(self.mutationDelta*(-1.0 - v), self.mutationDelta*(1.0-v))
    
    def breedWeights(self, aw, bw):
        o = aw.createCopy()
        for r in range(o.rows):
            for c in  range(o.cols):
                if random(1) > 0.5:
                    o.values[r][c] = bw.values[r][c]*1
                if random(1) < self.mutationRate:
                    o.values[r][c] *= self.mutate(o.values[r][c])
        return o

    def breed(self, a, b):

        babyColor = (((a.col[0]+b.col[0])/2)+random(-1*self.mutationDelta, self.mutationDelta), ((a.col[1]+b.col[1])/2)+random(-1*self.mutationDelta, self.mutationDelta), ((a.col[2]+b.col[2])/2)+random(-1*self.mutationDelta, self.mutationDelta))
        babyNN = a.nn.createCopy()

        babyNN.weights_i = self.breedWeights(a.nn.weights_i, b.nn.weights_i)
        babyNN.weights_h = self.breedWeights(a.nn.weights_h, b.nn.weights_h)
        babyNN.bias_i = self.breedWeights(a.nn.bias_i, b.nn.bias_i)
        babyNN.bias_h = self.breedWeights(a.nn.bias_h, b.nn.bias_h)

        return snake(babyNN, babyColor, self.randomDirection())

    def selectParent(self, parents):
        s = 0
        r = random(listSum([a.fitness for a in parents]))
        for i in range(len(parents)):
            s+=parents[i].fitness
            if s >= r:
                return parents[i]
    
    def birth(self, alphas):
        newGen = []
        for i in range(int(self.genSize*(1-self.cutOff))):
            parent1 = self.selectParent(alphas)
            parent2 = self.selectParent([a for a in alphas if a != parent1])
            newGen.append(self.breed(parent1, parent2))
        for i in alphas:
            i.reset()
        alphas[0].best = True
        alphas[0].food.best = True
        return self.generateSnakes(alphas + newGen)

    def sortFitness(self):
        self.snakes.sort(key=lambda x: x.fitness, reverse = True)
