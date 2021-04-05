import math
def dist_points(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2 - y1)**2)

def in_circle(x1, y1, cir_x1, cir_y1, radius):
#    return dist_points(x1, y1, cir_x1, cir_x2)*radius
    if dist_points(x1, y1, cir_x1, cir_y1) < radius:
        return True
    else:
        return False
    
