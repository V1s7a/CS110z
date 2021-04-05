""" gc4_template.py - CS110Z Project

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
        Stmt 1: Recieved EI from Dr. Weingart
        Stmt 2:
        ...
        Stmt N:
"""
import pythonGraph, random, math


""" Global Variables """

GATE_CHECK = 4
PARTNER1 = 'Grace Fleming '
PARTNER2 = 'Colton Willits'

SCREEN_HEIGHT = 800
SCREEN_WIDTH = 1000
mountains = []


""" Functions """

def config():
    global landing_padX, landing_padXone

    #open window and set title
    pythonGraph.open_window(SCREEN_WIDTH, SCREEN_HEIGHT)
    pythonGraph.set_window_title('Lunar Lander GC4 ' + PARTNER1 + PARTNER2 )
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
    
    step_max = 2.6
    step_change = 0.9
    height_max = SCREEN_HEIGHT * 3/8
    height = random.random() * height_max
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
            pythonGraph.draw_line(i, SCREEN_HEIGHT, i, SCREEN_HEIGHT - height, pythonGraph.colors.WHITE, 1)
          
    

        

    pass

def erase_objects():
    """ describe what this fuction does """
    pass

def erase_lander():
    """ describe what this fuction does """
    pass

def erase_thrusters():
    """ describe what this fuction does """
    pass

def move_objects():
    """ describe what this fuction does """
    pass

def draw_objects():
    """ describe what this fuction does """
    pass

def draw_lander(lander_x, lander_y):
    """ Draws lander """
    x_one= lander_x+20
    y_one =lander_y-20
    x_two = lander_x -20
    y_two = lander_y +20
    pythonGraph.draw_rectangle(x_one, y_one, x_two, y_two, pythonGraph.colors.WHITE, True)
    
    pass

def draw_thrusters():
    """ describe what this fuction does """
    pass
    
def process_controls():
    """ describe what this fuction does """
    pass

def detect_collisions():
    """ describe what this fuction does """
    pass

def game_over():
    """ describe what this fuction does """
    pass

""" main """
config()

while pythonGraph.window_not_closed():
    
    pythonGraph.update_window()

pythonGraph.close_window()
