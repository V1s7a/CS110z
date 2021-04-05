import pythonGraph

x_cordinates = 1000
y_cordinates = 900

pythonGraph.open_window(x_cordinates,y_cordinates)
        
pythonGraph.draw_circle(x_cordinates/2,y_cordinates/2, 100, pythonGraph.colors.BLUE, True)

pythonGraph.draw_circle(x_cordinates/6,y_cordinates/6, 100, pythonGraph.colors.GREEN, True)

pythonGraph.draw_text('Hello', 500, 300, pythonGraph.colors.RED, 72)

pythonGraph.draw_arc(1, 100, 200, 1, 250, 50, 1, 1, pythonGraph.colors.YELLOW, 3)

pythonGraph.draw_rectangle( 300,300, 250, 25, pythonGraph.colors.GREEN, True)
# Animation loop
while pythonGraph.window_not_closed():

    # Keyboard Example 
    """
    if pythonGraph.key_pressed("a"):
        print("'a' key was pressed")

    if pythonGraph.key_pressed("left"):
        print("Left Arrow key was pressed")
    """

    # Mouse Example
    """
    if pythonGraph.mouse_button_pressed(pythonGraph.mouse_buttons.LEFT):
        print("Left button clicked")
    """

    # Display drawn items to screen
    pythonGraph.update_window()