import pythonGraph

pythonGraph.open_window(500, 500)

x = 250
y = 250
delta_x = 3
delta_y = 6

#pythonGraph.wait_for_close()
while pythonGraph.window_not_closed():
    #Erase window
    pythonGraph.clear_window(pythonGraph.colors.WHITE)
    
#    # move
#    x = x + (3 * delta_x)
#    
#    if x > 549 or x < -49:
#        delta_x = delta_x * -1

      
     
    #Draw
    pythonGraph.draw_circle(x, 250, 50, pythonGraph.colors.BLUE, True)
    
    
 
    
    pythonGraph.update_window()

