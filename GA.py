from snake import snake
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
        self.cutOff = 0.5
        self.mutationRate = 0.05
        self.delta = 0.2
        self.snakes = self.generateSnakes()
        self.mutationDelta = 0.01
        self.best = []
        self.average = []
        
    def generateSnakes(self, newGen = []):
        if self.gen == 1:
            return [snake(None, randomColor(), self.randomDirection()) for i in range(self.genSize)]
        else:
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
            #print self.snakes
            self.gen+=1
            self.best = max([s.fitness for s in self.snakes])
            self.average = self.averageFitness()
            self.sortFitness()
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
    
    def breedWeights(self, aw, bw):
        o = aw.createCopy()
        for r in range(o.rows):
            for c in  range(o.cols):
                if random(1) > 0.5:
                    o.values[r][c] = bw.values[r][c]*1
                if random(1) < self.mutationRate:
                    current = o.values[r][c]
                    o.values[r][c] *= random(-1/current, 1/current)
        return o
    
    
    def breed(self, a, b):

        babyColor = (((a.col[0]+b.col[0])/2)+random(-1*self.delta, self.delta), ((a.col[1]+b.col[1])/2)+random(-1*self.delta, self.delta), ((a.col[2]+b.col[2])/2)+random(-1*self.delta, self.delta))
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
    def adjustFitness(self, alphas):
        lowest = min([s.fitness for s in self.snakes])
        for a in alphas:
            a.fitness += abs(lowest)
            
    def birth(self, alphas):
        self.adjustFitness(alphas)
        newGen = []
        for i in range(int(self.genSize*(1-self.cutOff))):
            parent1 = self.selectParent(alphas)
            parent2 = self.selectParent([a for a in alphas if a != parent1])
            newGen.append(self.breed(parent1, parent2))
        for i in alphas: 
            i.reset()
        return self.generateSnakes(alphas + newGen)
        
    def sortFitness(self):
        self.snakes.sort(key=lambda x: x.fitness, reverse = True)
