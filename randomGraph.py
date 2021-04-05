import pythonGraph
import random

pythonGraph.open_window(640, 480)
pythonGraph.set_window_title("RandomGraph")
i = 0
while i < 10:
    x_one = random.randint(0,400)
    y_one = random.randint(0,400)
    x_two = random.randint(0,400)
    y_two = random.randint(0,400)
    pythonGraph.draw_line(x_one, y_one, x_two, y_two, pythonGraph.colors.GREEN, True)
    i += 1
    

pythonGraph.wait_for_close()