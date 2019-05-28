balls = []
def setup():
    global balls
    size(800, 600)
    noFill()
    for i in range(2):
        balls.append(Ball())
    
def draw():
    background(255)
    rect(mouseX, height * 3 / 4, 80, 20)
    for i in range(2):
        balls[i].checkHit(mouseX, height * 3 / 4, 80, 20)
        balls[i].update()
        balls[i].draw()
    
    
class Ball:
    def __init__(self):
        self.init()
    def init(self):
        self.x = random(width / 3)
        self.y = 0
        self.vx = random(5)
        self.vy = random(-5, 5)
    def update(self):
        self.x += self.vx
        self.y += self.vy
    def draw(self):
        ellipse(self.x, self.y, 10, 10)
    def checkHit(self, x, y, w, h):
        if self.x < 0 or self.x > width or (((self.x < x and self.x + self.vx >= x) or (self.x > x + w and self.x + self.vx <= x + w)) and self.y > y and self. y < y + h) :
            self.vx *= -1
        if self.y < 0 or self.y > height or ((self.y < y and self.y + self.vy >= y) or (self.y > y + h and self.y + self.vy <= y + h)) and self.x > x and self. x < x + w :
            self.vy *= -1
        if self.y > y + h * 2:
            self.init()
