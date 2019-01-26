screen_w = 600
screen_h = 600
randomSeed(0)
def randomColor():
    return (random(0, 255), random(0, 255), random(0, 255))

class food:
    
    def __init__(self, col):
        self.w = screen_w/50.0
        self.h = screen_h/50.0
        self.coords = self.spawn()
        self.x = self.coords[0]
        self.y = self.coords[1]
        self.col = col
        self.best = False
        
    def spawn(self):
        return [floor(random(screen_w/self.w))*self.w, floor(random(screen_h/self.h))*self.h]
    
    def show(self):
        if self.best:
            fill(255)
        else:
            fill(self.col[0], self.col[1], self.col[2])
            
        rect(self.x, self.y, self.w, self.h)
    
    def update(self):
        self.show()
        
    def respawn(self):
        newCoords = self.spawn()
        self.x = newCoords[0]
        self.y = newCoords[1]
        
        
