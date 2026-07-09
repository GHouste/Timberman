import random

SCREEN_HEIGHT = 768
SCREEN_WIDTH = 768

class Tree_block:
    def __init__(self, start_pos):
        self.pos = start_pos
        self.branch = 0
        self.side = 256
        self.pos_y_list= [-256,0,256,512,768]

    def rand_branch(self):
        # -1 left branch | 0 no branches | 1 right branch
        self.branch = random.randint(-1, 1)

    def get_pos(self):
        return self.pos
    
    def get_branch(self):
        return self.branch
    
    def move(self):
        if self.pos >= len(self.pos_y_list)-1:
            self.pos = 0
            self.rand_branch()
        else:
            self.pos += 1
    
    def draw_tree(self):
        # draw tree core
        rect(SCREEN_WIDTH/2-self.side/2, self.pos_y_list[self.pos], self.side, self.side) #change to sprites later
        
         # drawing branches
        if self.branch == -1:
            rect(0,self.pos_y_list[self.pos]-40+self.side/2,self.side,40)
        if self.branch == 1:
            rect(512,self.pos_y_list[self.pos]-40+self.side/2,self.side,40)

class Player:
    def __init__(self):
        self.pos = -1 
        self.size = 256

    def get_player_pos(self):
        return self.pos
    
    def move(self, direction):
        self.pos = direction
    
    def draw_player(self):
        if self.pos == -1:
            rect(0, SCREEN_WIDTH-self.size, self.size, self.size)
        if self.pos == 1:
            rect(512, SCREEN_WIDTH-self.size, self.size, self.size)



def setup():
    size(SCREEN_WIDTH, SCREEN_HEIGHT)
    global player,tree_block_1,tree_block_2,tree_block_3,tree_block_4,tree_block_5, clicked, points
    
    points = 0
    player = Player()
    tree_block_1 = Tree_block(0)
    tree_block_2 = Tree_block(1)
    tree_block_3 = Tree_block(2)
    tree_block_4 = Tree_block(3)
    tree_block_5 = Tree_block(4)
    clicked = False

def keyPressed():
    global clicked
    
    if key == "a" and clicked == False:
        player.move(-1)
        tree_block_1.move()
        tree_block_2.move()
        tree_block_3.move()
        tree_block_4.move()
        tree_block_5.move()
        clicked = True
        hitbox_check()
        
    elif key == "d" and clicked == False:
        player.move(1)
        tree_block_1.move()
        tree_block_2.move()
        tree_block_3.move()
        tree_block_4.move()
        tree_block_5.move()
        clicked = True
        hitbox_check()

def keyReleased():
    global clicked
    clicked = False

def hitbox_check():
    global points
    
    if tree_block_1.get_pos() == 3:
        if tree_block_1.get_branch() == player.get_player_pos():
            exit()
        else:
            points += 1
    if tree_block_2.get_pos() == 3:
        if tree_block_2.get_branch() == player.get_player_pos():
            exit()
        else:
            points += 1
    if tree_block_3.get_pos() == 3:
        if tree_block_3.get_branch() == player.get_player_pos():
            exit()
        else:
            points += 1
    if tree_block_4.get_pos() == 3:
        if tree_block_4.get_branch() == player.get_player_pos():
            exit()
        else:
            points += 1
    if tree_block_5.get_pos() == 3:
        if tree_block_5.get_branch() == player.get_player_pos():
            exit()
        else:
            points += 1

def draw():
    player.draw_player()
    rect(0,0,SCREEN_WIDTH, SCREEN_HEIGHT)
    tree_block_1.draw_tree()
    tree_block_2.draw_tree()
    tree_block_3.draw_tree()
    tree_block_4.draw_tree()
    tree_block_5.draw_tree()