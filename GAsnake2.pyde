from GA import brain
trainer = brain(100)
screen_w = 600
screen_h = 600

def setup():
    size(screen_w, screen_h)
    background(0)
    frameRate(30)
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
