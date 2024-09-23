import turtle 

class MyTurtle:
    def __init__(self, color, shape):
        self.t = turtle.Turtle()
        self.t.color(color)
        self.t.shape(shape)
    
    def maju(self, jarak):
        self.t.forward(jarak)
    def putar_kiri(self, sudut):
        self.t.left(sudut)
    
    def buat_segitiga(self, ukuran):
        for _ in range(3):
            self.maju(ukuran)
            self.putar_kiri(120)
    
    def selesai(self):
        turtle.done()
        
turtle1= MyTurtle("brown", "turtle")
turtle1.buat_segitiga(250)
turtle1.selesai()
