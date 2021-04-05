import pythonGraph

SCR_HEIGHT = 800
SCR_WIDTH = 800


pythonGraph.open_window(SCR_HEIGHT, SCR_WIDTH)

ball_x = SCR_HEIGHT // 2
ball_y = SCR_WIDTH // 2
ball_radius = 25
delta_x = 6
delta_y = 4

while pythonGraph.window_not_closed():
    # Erase the frame
    pythonGraph.clear_window(pythonGraph.colors.WHITE)
    
    # Move the ball
    ball_x += delta_x
    ball_y += delta_y
    
    if ball_x <= ball_radius or ball_x >= (SCR_WIDTH - ball_radius):
        delta_x = -delta_x
        
    if ball_y <= ball_radius or ball_y >= (SCR_HEIGHT - ball_radius):
        delta_y = -delta_y
    
    # Draw the ball
    pythonGraph.draw_circle(ball_x, ball_y, ball_radius, pythonGraph.colors.BLUE, True)
    
    # Update the window    
    pythonGraph.update_window()

