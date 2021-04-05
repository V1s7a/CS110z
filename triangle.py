
import pythonGraph


#open window
pythonGraph.open_window(600, 600)

#draw a triangle (300, 100) (150,450) (450,450)
pythonGraph.draw_line(300, 100, 450, 450, pythonGraph.colors.BLUE, 3)
pythonGraph.draw_line(450, 450, 150, 450, pythonGraph.colors.BLUE, 3)
pythonGraph.draw_line(150, 450, 300, 100, pythonGraph.colors.BLUE, 3)

#update window
while pythonGraph.window_not_closed():
    # Display drawn items to screen
    pythonGraph.update_window()