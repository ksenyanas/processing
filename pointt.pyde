x = 3
def setup():
    size(600,400)
    background(255,255,255)
def draw():
    global x 
    ellipse(x,x,100,100)
    x = x + 3
