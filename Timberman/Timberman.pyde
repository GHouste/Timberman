
SCREEN_HEIGHT = 768
SCREEN_WIDTH = 768

class Tree_block:
    def __init__(self, start_pos):
        self.pos = start_pos
        self.branch = 0
        self.side = 256
        self.pos_y_list= [-256,0,256,512,768]
        
    def draw_tree(self):
        rect(SCREEN_WIDTH/2-self.side/2,self.pos_y_list[self.pos],self.side,self.side) #change to sprites later
        print(self.pos) #delete later
    def move(self):
        if self.pos >= len(self.pos_y_list)-1:
            self.pos = 0
        else:
            self.pos += 1
        
    def get_branch(self):
        pass

class Player:
    def __init__():
        pass
    
    def move(self):
        pass
        
    def draw_player(self):
        pass



def setup():
    size(SCREEN_WIDTH, SCREEN_HEIGHT)
    global test, clicked
    test = Tree_block(1)#delete later
    clicked = False

def keyPressed():
    global clicked
    
    if key == "a" and clicked == False:
        test.move() #delete later
        clicked = True
    elif key == "d" and clicked == False:
        test.move() #delete later
        clicked = True

def keyReleased():
    global clicked
    clicked = False

def draw():
    rect(0,0,SCREEN_WIDTH, SCREEN_HEIGHT)
    test.draw_tree() #delete later
