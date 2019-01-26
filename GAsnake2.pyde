from GA import brain
import csv
testing = True
record = 'record.csv'

trainer = brain(1000)
screen_w = 600
screen_h = 600

def setup():
    size(screen_w, screen_h)
    background(0)
    frameRate(60)
    trainer.generateSnakes()

def draw():
    background(0)
    trainer.update()
    fill(255)
    text("Generation: "+str(trainer.gen), 10, 20)
    text("Best: "+str(trainer.best), 10, 70)
    text("Average: "+str(trainer.average), 10, 120)
    text("Mutation Rate: "+str(trainer.mutationRate), 10, 170)
    text("Mutation Delta: "+str(trainer.delta), 10, 220)
    text("Cut Off: "+str(trainer.cutOff), 10, 270)
    text("Gen Size: "+str(trainer.genSize), 10, 320)

def keyPressed():
    if key == 'p' and testing:
        with open(record, "w") as output:
            writer = csv.writer(output, lineterminator='\n')
            for i in range(len(trainer.bests)):
                writer.writerow([i,trainer.bests[i], trainer.averages[i]])  
            exit()

        
    
