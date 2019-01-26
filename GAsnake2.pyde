from GA import brain
import csv

record = 'record.csv'
bestNN = 'nn.csv'

screen_w = 600
screen_h = 600

def readInWeights():
    weights = [[],[],[],[]]
    i = 0

    with open(bestNN, "r") as input:
        reader = csv.reader(input)
        for row in reader:
            if row == ['']:
                i += 1
            else:
                weights[i].append([float(r) for r in row])

    return weights

singleSnakeMode = False
dataCollect = False

if singleSnakeMode:
    trainer = brain(1, dataCollect)
    readIn = readInWeights()
    trainer.snakes[0].nn.weights_i.values = readIn[0]
    trainer.snakes[0].nn.weights_h.values = readIn[1]
    trainer.snakes[0].nn.bias_i.values = readIn[2]
    trainer.snakes[0].nn.bias_h.values = readIn[3]
else:
    trainer = brain(50, dataCollect)

def setup():

    size(screen_w, screen_h)
    background(0)
    frameRate(1000)
    trainer.generateSnakes()

def draw():
    x = 0
    if not trainer.testing:
        background(0)
        fill(255)
        text("Generation: "+str(trainer.gen), 10, 20)
        text("Best: "+str(trainer.bestFitness), 10, 70)
        text("Average: "+str(trainer.average), 10, 120)
        text("Mutation Rate: "+str(trainer.mutationRate), 10, 170)
        text("Mutation Delta: "+str(trainer.delta), 10, 220)
        text("Cut Off: "+str(trainer.cutOff), 10, 270)
        text("Gen Size: "+str(trainer.genSize), 10, 320)
    else:
        if x != trainer.gen:
            print trainer.gen
            x += 1
    
    trainer.update()

def keyPressed():
    if key == 'p' and testing:
        with open(record, "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            writer.writerow(['Gen', 'Best', 'Average'])
            for i in range(len(trainer.bests)):
                writer.writerow([i+1,trainer.bests[i], trainer.averages[i]])

        with open(bestNN, "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            tables = [trainer.best.nn.weights_i, trainer.best.nn.weights_h, trainer.best.nn.bias_i, trainer.best.nn.bias_h]
            for t in tables:
                writer.writerows(t.values)
                writer.writerow([''])

        exit()
