int num, dist, fil = 1;
float col = 0;
Particle[] p;
ArrayList<Triangle> t;
void setup() {
  size(700, 500);
  //fullScreen();
  colorMode(HSB);
  init();
}
void init() {
  num = 100;
  dist = width / 10;
  p = new Particle[num + 1];
  for (int i=1; i<=num; ++i)
    p[i] = new Particle();
}
void draw() {
  background(51);
  for (int i=1; i<=num; ++i) {
    p[i].move();
    p[i].show();
  }
  t = new ArrayList<Triangle>(); 
  for (int i=1; i<=num; ++i) {
    p[i].vecini = new ArrayList<Particle>();
    p[i].vecini.add(p[i]);
    for (int j=i+1; j<=num; ++j) {
      float d = PVector.dist(p[i].pos, p[j].pos);
      if (d > 0 && d < dist)p[i].vecini.add(p[j]);
    }
    if (p[i].vecini.size() > 2)addTriangle(p[i].vecini);
  }
  showTriangles();
  if (col > 255)col = 0;
  col += 3;
}
void addTriangle(ArrayList<Particle> v) {
  for (int i=1; i<v.size()-1; ++i) 
    for (int j=i+1; j<v.size(); ++j)
      t.add(new Triangle(v.get(0).pos, v.get(i).pos, v.get(j).pos));
}
void showTriangles() {
  if (fil == 1)fill(col, 255, 255, 50);
  else {
    noFill();
    stroke(col, 255, 255, 50);
  }
  beginShape(TRIANGLES);
  for (int i=0; i<t.size(); ++i) {
    Triangle tr = t.get(i);
    tr.show();
  }
  endShape();
}
void keyPressed() {
  if (key == 'w')fil *= -1;
}
class Particle {
  float max = 1.2, rad = 4;
  PVector pos, speed = new PVector(random(-max, max), random(-max, max));
  ArrayList<Particle> vecini;
  Particle() {
    pos = new PVector(random(width), random(height));
  }
  void move() {
    pos.add(speed);
    if(pos.x < 0 || pos.x > width)speed.x *= -1;
    if(pos.y < 0 || pos.y > height)speed.y *= -1;
  }
  void show() {
    noStroke();
    fill(col, 255, 255, 100);
    ellipse(pos.x, pos.y, rad, rad);
  }
}
class Triangle {
  PVector a, b, c;
  Triangle(PVector p1, PVector p2, PVector p3) {
    a = p1;
    b = p2;
    c = p3;
  }
  void show() {
    vertex(a.x, a.y);
    vertex(b.x, b.y);
    vertex(c.x, c.y);
  }
}
