import numpy as np
import pygame

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
    
    