import random

SCREEN_HEIGHT = 768
SCREEN_WIDTH = 768

class Tree_block:
    def __init__(self, start_pos):
        self.pos = start_pos
        self.branch = 0
        self.side = 256
        self.pos_y_list = [-256, 0, 256, 512, 768]
        self.tree_sprite = loadImage("assets/tree.png")
        self.branch_sprite = loadImage("assets/branch.png")

    def rand_branch(self):
        # -1: left branch, 0: no branch, 1: right branch
        self.branch = random.randint(-1, 1)

    def get_pos(self):
        return self.pos

    def get_branch(self):
        return self.branch

    def move(self):
        # Reset to top and randomize branch if it reaches the bottom
        if self.pos >= len(self.pos_y_list) - 1:
            self.pos = 0
            self.rand_branch()
        else:
            self.pos += 1

    def draw_tree(self):
        # Draw the main trunk
        image(self.tree_sprite, SCREEN_WIDTH/2 - self.side/2, self.pos_y_list[self.pos])

        # Draw side branches based on current state
        if self.branch == -1:
            image(self.branch_sprite, 0, self.pos_y_list[self.pos] - 40 + self.side/2)
        if self.branch == 1:
            image(self.branch_sprite, 384, self.pos_y_list[self.pos] - 40 + self.side/2)

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
        # -1: player on left, 1: player on right
        if self.pos == -1:
            image(self.player_sprite, 0 + self.size/2, SCREEN_WIDTH - self.size)
        if self.pos == 1:
            image(self.player_sprite, 512 + self.size/2, SCREEN_WIDTH - self.size)


def setup():
    global bg, player, tree_block_1, tree_block_2, tree_block_3, tree_block_4, tree_block_5, clicked, points, energy, max_energy, game_over

    size(SCREEN_WIDTH, SCREEN_HEIGHT)
    textSize(200)
    bg = loadImage("assets/background.png")

    # Initialize game stats and objects
    points = 0
    player = Player()
    tree_block_1 = Tree_block(0)
    tree_block_2 = Tree_block(1)
    tree_block_3 = Tree_block(2)
    tree_block_4 = Tree_block(3)
    tree_block_5 = Tree_block(4)
    clicked = False

    # Initialize energy bar and game status
    max_energy = 400.0
    energy = max_energy / 2  # Start with half energy
    game_over = False

def show_score():
    global points
    fill(0, 0, 0)
    # Adjust score text position based on digits
    if points < 10:
        text(points, 320, 200)
    elif points < 100:
        text(points, 256, 200)
    elif points >= 100:
        text(points, 192, 200)

def hitbox_check():
    global points, game_over, energy, max_energy

    # Check if any branch hits the player at the bottom level
    if tree_block_1.get_pos() == 3 and tree_block_1.get_branch() == player.get_player_pos():
        game_over = True
        return
    if tree_block_2.get_pos() == 3 and tree_block_2.get_branch() == player.get_player_pos():
        game_over = True
        return
    if tree_block_3.get_pos() == 3 and tree_block_3.get_branch() == player.get_player_pos():
        game_over = True
        return
    if tree_block_4.get_pos() == 3 and tree_block_4.get_branch() == player.get_player_pos():
        game_over = True
        return
    if tree_block_5.get_pos() == 3 and tree_block_5.get_branch() == player.get_player_pos():
        game_over = True
        return

    # Reward player for a successful chop
    points += 1
    energy += 15.0
    if energy > max_energy:
        energy = max_energy

def keyPressed():
    global clicked, game_over

    if game_over:
        return

    # Handle left chop (A key)
    if key == "a" and not clicked:
        player.move(-1)
        tree_block_1.move()
        tree_block_2.move()
        tree_block_3.move()
        tree_block_4.move()
        tree_block_5.move()
        hitbox_check()

    # Handle right chop (D key)
    elif key == "d" and not clicked:
        player.move(1)
        tree_block_1.move()
        tree_block_2.move()
        tree_block_3.move()
        tree_block_4.move()
        tree_block_5.move()
        hitbox_check()

    clicked = True

def keyReleased():
    global clicked
    clicked = False

def draw():
    global energy, game_over

    # Render game world and entities
    image(bg, 0, 0)
    player.draw_player()
    tree_block_1.draw_tree()
    tree_block_2.draw_tree()
    tree_block_3.draw_tree()
    tree_block_4.draw_tree()
    tree_block_5.draw_tree()
    show_score()

    if not game_over:
        # Drain energy over time
        energy -= 0.4
        if energy <= 0:
            game_over = True

        # Draw energy bar background
        fill(200, 200, 200)
        rect(SCREEN_WIDTH/2 - max_energy/2, 50, max_energy, 30, 10)

        # Draw active energy level
        fill(255, 0, 0)
        rect(SCREEN_WIDTH/2 - max_energy/2, 50, max_energy if energy > max_energy else energy, 30, 10)

    else:
        # Display Game Over overlay screen
        fill(0, 150)
        rect(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT)

        fill(255, 0, 0)
        textAlign(CENTER)
        textSize(80)
        text("GAME OVER", SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

        fill(255)
        textSize(50)
        text("Score: " + str(points), SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 80)

        # Reset text settings for show_score() compatibility
        textAlign(LEFT)
        textSize(200)