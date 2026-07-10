import random

SCREEN_HEIGHT = 768
SCREEN_WIDTH = 768

class Tree_block:
    def __init__(self, start_pos):
        self.pos = start_pos
        self.branch = 0
        self.side = 256
        self.pos_y_list= [-256,0,256,512,768]
        self.tree_sprite = loadImage("assets/tree.png")
        self.branch_sprite = loadImage("assets/branch.png")
        
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
        image(self.tree_sprite,SCREEN_WIDTH/2-self.side/2,self.pos_y_list[self.pos])
        
         # drawing branches
        if self.branch == -1:
            image(self.branch_sprite,0,self.pos_y_list[self.pos]-40+self.side/2)
        if self.branch == 1:
            image(self.branch_sprite,384,self.pos_y_list[self.pos]-40+self.side/2)

class Player:
    def __init__(self):
        self.pos = -1 
        self.size = 128
        self.player_sprite = loadImage("assets/player.png")
        
    def get_player_pos(self):
        return self.pos
    
    def move(self, direction):
        self.pos = direction
    
    def draw_player(self):
        if self.pos == -1:
            image(self.player_sprite,0+self.size/2, SCREEN_WIDTH-self.size,)
        if self.pos == 1:
            image(self.player_sprite,512+self.size/2, SCREEN_WIDTH-self.size)



def setup():
    size(SCREEN_WIDTH, SCREEN_HEIGHT)
    textSize(200)
    
    global bg ,player,tree_block_1,tree_block_2,tree_block_3,tree_block_4,tree_block_5, clicked, points
    
    bg = loadImage("assets/background.png")
    
    points = 0
    player = Player()
    tree_block_1 = Tree_block(0)
    tree_block_2 = Tree_block(1)
    tree_block_3 = Tree_block(2)
    tree_block_4 = Tree_block(3)
    tree_block_5 = Tree_block(4)
    clicked = False

def show_score():
        global points
        fill(0,0,0)
        if points < 10:
            text(points,320,200)
        if points < 100 and points >9:
            text(points,256,200)
        elif points >= 100:
            text(points,192,200)
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
    if tree_block_2.get_pos() == 3:
        if tree_block_2.get_branch() == player.get_player_pos():
            exit()
    if tree_block_3.get_pos() == 3:
        if tree_block_3.get_branch() == player.get_player_pos():
            exit()
    if tree_block_4.get_pos() == 3:
        if tree_block_4.get_branch() == player.get_player_pos():
            exit()
    if tree_block_5.get_pos() == 3:
        if tree_block_5.get_branch() == player.get_player_pos():
            exit()
    points += 1

def draw():
    image(bg,0,0)
    player.draw_player()
    tree_block_1.draw_tree()
    tree_block_2.draw_tree()
    tree_block_3.draw_tree()
    tree_block_4.draw_tree()
    tree_block_5.draw_tree()
    show_score()
