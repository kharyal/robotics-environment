import numpy as np
import pygame

'''
Functions to check collision
'''
def ccw(A,B,C):
    return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

def intersect(A,B,C,D):
    '''
    Check if lines AB and CD intersect
    '''
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)
'''
'''

class World():
    '''
    The world object
    '''

    def __init__(self, x_range, y_range):
        self.x_range = 600
        self.y_range = 600
        self.obstacles = [(0,0,10,y_range), (0,0,x_range,10), (0,y_range-10,x_range,10), (x_range-10,0,10,y_range)]

    def add_obstacles(self, obstacles):
        '''
        a function to add custom obstacles to the world

        ONLY RECTANGULAR OBSTAClES SUPPORTED
        obstacles: [(rect1.x_pos, rect1.y_pos, rect1.length, rect1.width), 
                    (rect2.x_pos, rect2.y_pos, rect2.length, rect2.width)...]
        '''

        self.obstacles = self.obstacles + obstacles

    def print_obstacles(self, gameDisplay):
        '''
        prints obstacles onto the display

        Default obstacle colour: (0,0,0)
        '''

        for obstacle in self.obstacles:
            pygame.draw.rect(gameDisplay, (0,0,0), pygame.Rect(obstacle[0], obstacle[1], obstacle[2], obstacle[3]))
    
    def check_collision_holonomic(self, start, end, num_samples = 0):
        '''
        checks collision with obstacles for a straight line path from <start> to <end>

        checks if the line start->end and any of the four obstacle lines intersect

        start: (start_x, start_y)
        end:   (end_x, end_y)
        
        returns: True if collision, False otherwise 
        '''

        for obstacle in self.obstacles:
            obstacle_lines = [
                [(obstacle[0], obstacle[1]), (obstacle[0]+obstacle[2], obstacle[1])],
                [(obstacle[0], obstacle[1]), (obstacle[0], obstacle[1]+obstacle[3])],
                [(obstacle[0]+obstacle[2], obstacle[1]), (obstacle[0]+obstacle[2], obstacle[1]+obstacle[3])],
                [(obstacle[0], obstacle[1]+obstacle[3]), (obstacle[0]+obstacle[2], obstacle[1]+obstacle[3])]
            ]
            for line in obstacle_lines:
                collide = intersect(start, end, line[0], line[1])
                
                if collide:
                    return True

        return False 