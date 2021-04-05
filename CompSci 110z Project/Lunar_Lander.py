""" gc5_template.py - CS110Z Project

    Team Members: Grace Fleming, Colton Willits
    Section: M6A
    Requirements NOT Fully Functional (this GC only):
        Rqmt 1:
        Rqmt 2:
        ...
        Rqmt N:
    Extra Credit Features:
        Feature 1:
        Feature 2:
        ...
        Feature N:
    Documentation:
        Stmt 1: No documentation needed.
        Stmt 2: Recieved help from Dr. Weingart
        ...
        Stmt N:
"""
import pythonGraph, random, math



""" Global Variables """

GATE_CHECK = "Final"
PARTNER1 = 'Grace Fleming '
PARTNER2 = 'Colton Willits'

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
mountains = []

up_thrust = False
left_thrust = False
right_thrust = False
quit_game = False

deltaY = 0
deltaX = 0
lander_x = 0
lander_y = 0

crash = bool
landing = bool

""" Functions """

def config():
    global landing_padX, landing_padXone, lander_x, lander_y

    #open window and set title
    pythonGraph.open_window(SCREEN_WIDTH, SCREEN_HEIGHT)
    pythonGraph.set_window_title('Lunar Lander' + PARTNER1 + PARTNER2 )
    pythonGraph.clear_window(pythonGraph.colors.BLACK)
    
    """Set lander position/initialize variables"""
    
    
    landing_padX = random.randint(0,SCREEN_WIDTH)
    landing_padXone = landing_padX + 70
    
    lander_x = SCREEN_WIDTH / 2
    lander_y = (SCREEN_HEIGHT * 5/8) / 2
    
    draw_lander(lander_x,lander_y)
    generate_landscape(mountains)


def generate_landscape(mountains):
    """ generate randomized mountians"""
    global landingpad_height
    step_max = 2.6
    step_change = 0.9
    height_max = SCREEN_HEIGHT * 3/8
    height = random.random() * height_max
    landingpad_height = height
    slope = 0
    x_location = 1
    
    
    for i in range(SCREEN_WIDTH):
        if i >= landing_padX and i <= landing_padXone:
            pythonGraph.draw_line(landing_padX, SCREEN_HEIGHT - height, landing_padXone, SCREEN_HEIGHT - height, pythonGraph.colors.GREEN, 5)
            pythonGraph.draw_line(i, SCREEN_HEIGHT, i, SCREEN_HEIGHT - height, pythonGraph.colors.WHITE, 1)
        else:
            slope = slope + (random.random() * step_change * 2-step_change)
            height = height + slope
            if slope > step_max:
                slope = step_max
                
            if slope < -step_max:
                slope = -step_max
            
            if height > height_max:
                height = height_max
                slope = -slope
            
            if height < 1:
                height = 1
                slope = -slope
            pythonGraph.draw_line(i, SCREEN_HEIGHT, i, SCREEN_HEIGHT - height,pythonGraph.colors.WHITE, 1)
        mountains.append(SCREEN_HEIGHT - height)
    pass

def erase_objects():
    erase_lander()
    erase_thrusters()
    pass

def erase_lander():
    x_one = lander_x +40
    y_one = lander_y +40
    x_two = lander_x  -1
    y_two = lander_y -1
    pythonGraph.draw_rectangle(x_one, y_one, x_two, y_two, pythonGraph.colors.BLACK, True)
    pass

def erase_thrusters():
    pythonGraph.draw_rectangle(lander_x + 14, lander_y + 35, lander_x + 40, lander_y + 58, pythonGraph.colors.BLACK, True)
    pythonGraph.draw_rectangle(lander_x - 20, lander_y +5, lander_x, lander_y + 30 , pythonGraph.colors.BLACK, True)
    pythonGraph.draw_rectangle(lander_x + 40, lander_y + 5, lander_x + 50, lander_y + 40, pythonGraph.colors.BLACK, True)
    pass

def move_objects():
    global lander_x, lander_y, deltaY, deltaX
    if up_thrust == True:
        deltaY = deltaY - 0.06
        
    else:
        deltaY = deltaY + 0.06
    
    if right_thrust == True:
        deltaX = deltaX + 0.06
    
    if left_thrust == True:
        deltaX = deltaX - 0.06
        
    lander_x = lander_x + deltaX
    lander_y = lander_y + deltaY
    
    wrap_lander()
    
    pass

def draw_objects():
    draw_lander(lander_x, lander_y)
    draw_thrusters()
    pass

def draw_lander(lander_x, lander_y):
    """ Draws lander """
    pythonGraph.draw_image("lander.jpg", lander_x, lander_y, 40,40)
    pass

def draw_thrusters():
    if up_thrust == True:
        pythonGraph.draw_text("v", lander_x + 14, lander_y + 35, pythonGraph.colors.WHITE, 40)
    if right_thrust == True:
        pythonGraph.draw_text("<", lander_x - 10, lander_y + 5, pythonGraph.colors.WHITE, 40)
    if left_thrust == True:
        pythonGraph.draw_text(">", lander_x + 35, lander_y + 5, pythonGraph.colors.WHITE, 40)
    pass
    
def process_controls():
    global up_thrust, left_thrust, right_thrust, quit_game
    if pythonGraph.key_down('up'):
        up_thrust = True
    else:
        up_thrust = False
    
    if pythonGraph.key_down('left'):
        left_thrust = True
    else:
        left_thrust = False
    
    if pythonGraph.key_down('right'):
        right_thrust = True
    else:
        right_thrust = False
    
    if pythonGraph.key_down('escape'):
        quit_game = True
    else:
        quit_game = False
    
    if pythonGraph.mouse_button_down(pythonGraph.mouse_buttons.LEFT):
        exit()

    pass

def wrap_lander():
    global lander_x
    if lander_x + 40 >= SCREEN_WIDTH:
        lander_x = 20
    if lander_x - 10 < 10:
        lander_x = SCREEN_WIDTH - 40

    pass


def detect_collisions():
    global crash, landing
    crash = False
    landing = False
    x_position = lander_x
    landerHeight = lander_y + 35


    for i in range(int(x_position), int(lander_x) + 35):
        if i in range(landing_padX, landing_padXone) and landerHeight > mountains[i]:
            landing = True
            return
        elif landerHeight > mountains[i]:
            crash = True
            return
        
    
    pass

def game_over():
    global deltaX, deltaY
    if crash == True:
        pythonGraph.draw_text("You Crashed!", SCREEN_WIDTH / 3, SCREEN_HEIGHT /3, pythonGraph.colors.RED, 80)
        pythonGraph.draw_text("Click left mouse button to exit", SCREEN_WIDTH / 3, SCREEN_HEIGHT / 4, pythonGraph.colors.WHITE, 50)
        deltaX = 0
        deltaY = 0
    if landing == True:
        pythonGraph.draw_text("You Landed!", SCREEN_WIDTH / 3, SCREEN_HEIGHT/3, pythonGraph.colors.GREEN, 80)
        pythonGraph.draw_text("Click left mouse button to exit", SCREEN_WIDTH / 3, SCREEN_HEIGHT / 4, pythonGraph.colors.WHITE, 50)
        deltaX = 0
        deltaY = 0
    pass

""" main """
config()




while pythonGraph.window_not_closed():


    pythonGraph.update_window()
    erase_objects()
    move_objects()
    draw_objects()
    process_controls()
    detect_collisions()
    game_over()
    if quit_game == True:
        exit()
    
pythonGraph.close_window()


