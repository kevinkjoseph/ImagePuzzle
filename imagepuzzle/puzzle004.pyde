add_library('minim')
import os, random
path = os.getcwd()
player = Minim(this)

class Tile:
    def __init__(self,r,c,v):
        self.r=r
        self.c=c
        self.v=v
        self.img=loadImage(path+"/images/"+str(v)+".png")
        
    def display(self):
        if self.v != 0 or p.win == True:
            image(self.img,self.c*200,self.r*200)
            
            if p.win == False:
                stroke(0)
                rect(self.c*200,self.r*200,200,200)
        
class Puzzle:
    def __init__(self):
        self.numRows=4
        self.numCols=4
        self.tiles=[]
        self.win = False
        self.clickSound = player.loadFile(path+"/effects/click.mp3")
        self.music = player.loadFile(path+"/effects/background.mp3")
        self.winSound = player.loadFile(path+"/effects/win.mp3")
        self.music.play()
        
        cnt=0
        for r in range(self.numRows):
            for c in range(self.numCols):
                self.tiles.append(Tile(r,c,cnt))
                cnt+=1
        self.shuffleP(10)
                
    def shuffleP(self,difficulty):
        eT = self.getTile(0,0)
        
        for i in range(difficulty):
            n = random.choice([[-1,0],[1,0],[0,-1],[0,1]])
            nT = self.getTile (eT.r+n[0],eT.c+n[1])
            if nT != False:
                self.swap(nT,eT)    
                eT = nT
                
    def display(self):
        for t in self.tiles:
            t.display()
        
        if self.win == False:
            c = mouseX // 200
            r = mouseY // 200
            print (r,c)
            stroke(0,255,0)
            rect(c*200,r*200,200,200)
    
    def getTile(self,r,c):
        for t in self.tiles:
            if t.r == r and t.c == c:
                return t
        return False
    
    def swap(self,t1,t2):
        tmp1 = t1.v
        tmp2 = t1.img
        t1.v = t2.v
        t1.img = t2.img
        t2.v = tmp1
        t2.img = tmp2
        
    def click(self):
        c = mouseX // 200
        r = mouseY // 200
        t = self.getTile(r,c)
        for n in [[-1,0],[1,0],[0,-1],[0,1]]:
            nT = self.getTile(r+n[0], c+n[1])
            if nT != False and nT.v == 0:
                self.swap(t,nT)
                self.clickSound.rewind()
                self.clickSound.play()
                self.win = self.checkWin()
                return
            
    def checkWin(self):
        for t in self.tiles:
            if t.v != t.r*4+t.c:
                return False
        self.winSound.play()
        return True

def setup():
    size(800,800)
    background(0)
    noFill()
    strokeWeight(5)

p = Puzzle()

def draw():
    background(0)
    p.display()

def mouseClicked():
    if p.win == True:
        p.shuffleP(1000)
        p.win = False
        p.winSound.rewind()
    else:
        p.click()
