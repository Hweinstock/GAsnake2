from GA import brain
from data import dataCollector

record = 'record.csv'
bestNN = 'nn.csv'

screen_w = 600
screen_h = 600

data = dataCollector(bestNN, record)

singleSnakeMode = False

if singleSnakeMode:
    trainer = brain(1)
    readIn = data.readInWeights()
    trainer.snakes[0].nn.weights_i.values = readIn[0]
    trainer.snakes[0].nn.weights_h.values = readIn[1]
    trainer.snakes[0].nn.bias_i.values = readIn[2]
    trainer.snakes[0].nn.bias_h.values = readIn[3]
else:
    trainer = brain(500)

def setup():

    size(screen_w, screen_h)
    background(0)
    if singleSnakeMode:
        frameRate(60)
    else:
        frameRate(1000)
    trainer.generateSnakes()

def draw():
    
    background(0)
    trainer.update()
    fill(255)
    text("Generation: "+str(trainer.gen), 10, 20)
    text("Best Fitness: "+str(trainer.bestFitness), 10, 70)
    text("Average: "+str(trainer.average), 10, 120)
    text("Mutation Rate: "+str(trainer.mutationRate), 10, 170)
    text("Mutation Delta: "+str(trainer.mutationDelta), 10, 220)
    text("Cut Off: "+str(trainer.cutOff), 10, 270)
    text("Gen Size: "+str(trainer.genSize), 10, 320)
    text("Best Score: "+str(trainer.bestFoodScore), 10, 370)

def keyPressed():
    if key == 'p':
        data.writeOutData(trainer)
        data.writeOutWeights(trainer)
        exit()
