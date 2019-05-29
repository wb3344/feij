num=0,
dist=0
fil =1
col =0.0
pos = 0
p =[]
t =[]

def setup():
    global p
    size(700,500)
    colorMode(HSB)
    __init__(0,0,0)
    
def __init__(self,num,dist):
    num = 100
    dist = width/10
    # p = new Particle[num + 1]
    # for i in range(1,unm)
    #     p[i] = Particle()
    for i in range (num):
        p[i] = Particle(i+1)
        i = i+1
def draw():
    background(51)
    for i in range(1,num):
        p[1].move()
        p[i].show()
    t = Triangle
    for i in range(1,num):
        p[i].vecini = [];
        p[i].vecini.append(p[i])
        for j in range(i+1,num):
            d =  PVector.dist(p[i].pos, p[j].pos)
            if (d > 0 and d < dist):
                p[i].vecini.append(p[j])
        if(p[i].vecini.size() > 2):
            addTriangle(p[i].vecini)
    showTriangles()
    if (col > 255):
        col = 0
    col += 3
    
def addTriangle(v):
    for i in range(1,len(v)-1):
        for i in range(i+1,len(v)):
            t.add(Triangle(v(0).pos,v(i).pos,v(j).pos))
            
def showTriangles():
    if (fil == 1):
        fill(col,255,255,50)
    else:
        noFill()
        stroke(col,255,255,50)
    beginShape(TRIANGLES)
    for i in range (i-1,len(t)):
        tr = t(i)
        tr.show()
        
    endShape()
    
def keyPressed():
    if(key == 'w'):
        fil *= -1
class Particle:
    Particle():
            pos =  PVector(random(width),random(height))
    def __init__(self,num):
        Max = 1.2 
        rad = 4.0
        # pos
        speed = PVector(random(-Max,Max),random(-Max,Max))
        vecini=[]
        # Particle():
        #     pos =  PVector(random(width),random(height))
    def move(self):
        pos.append(speed)
        if(pos.x < 0 or pos.x > width):
            speed.x *= -1
        if(pos.y < 0 or pos.y > height):
            speed.y *= -1
    def show(self):
        noStroke()
        fill(col,255,255,100)
        ellipse(pos.x,pos.y,rad,rad)
        
        # def __init__(self,num,dist):
        #     num = 100
        #     dist = width/10
        #     # p = new Particle[num + 1]
        #     # for i in range(1,unm)
        #     #     p[i] = Particle()
        #     for i in range (num):
        #         p[i] = Particle(i+1)
        #         i = i+1
        
class Triangle:
    def __init__(self,p1,p2,p3,x,y):
        Triangle(p1,p2, P3)
        a = p1
        b = P2
        c = p3
    def show(self):
        vertex(a.x,a.y)
        vertex(b.x,b.y)
        vertex(c.x,c.y)
