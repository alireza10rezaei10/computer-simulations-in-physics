import numpy as np
import pygame
pygame.init();


# configs ------------------------------

class Configs:
    def __init__(self): 
        self.fullscreen = True
        self.window_width, self.window_height = 800, 600
        
        # frame per second
        self.FPS = 1
        
        self.number_of_initial_points = 100000
        self.font = pygame.font.SysFont('Corbel',35)
        self.generate_button_text = self.font.render("generate new initial points", True, "white")
        self.generate_button_background_color = "blue"
        
configs = Configs()


def main_loop(functions):
    
    WINDOW = ""

    if configs.fullscreen:
        WINDOW = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        configs.window_width, configs.window_height = pygame.display.get_window_size()
    else:
        WINDOW = pygame.display.set_mode((configs.window_width, configs.window_height))


    class Points:
        def __init__(self, number_of_initial_points):
            self.number_of_initial_points = number_of_initial_points
            self.initial_points = (np.random.exponential(size=self.number_of_initial_points)-0.5).reshape(self.number_of_initial_points//2, 2)*np.random.randint(500)

        def generate_new_initial_points(self):
            
            # choose a random distribution from 3 distributions
            random_dist = np.random.randint(3)

            if random_dist == 0:
                self.initial_points = (np.random.exponential(size=self.number_of_initial_points)-0.5).reshape(self.number_of_initial_points//2, 2)*np.random.randint(500)
            elif random_dist == 1:
                self.initial_points = (np.random.random(self.number_of_initial_points)-0.5).reshape(self.number_of_initial_points//2, 2)*np.random.randint(500)
            else:
                self.initial_points = (np.random.binomial(n=50, p=0.5, size=self.number_of_initial_points)-0.5).reshape(self.number_of_initial_points//2, 2)*np.random.randint(20)

        def do_one_step(self):
            for i, point in enumerate(self.initial_points):
                # randomly select a function and do that on all points and save points
                
                random_selected_function = np.random.choice(functions)
                point = random_selected_function(point)
                self.initial_points[i] = point

        def draw(self):
            for point in self.initial_points:
                pygame.draw.rect(WINDOW, "blue", pygame.Rect((configs.window_width-300)/2+point[0], 2*configs.window_height/3-point[1] ,1 ,1))


    class GenerateButton:
        def __init__(self, text, background_color):
            self.text = text
            self.background_color = background_color
            self.width = 390
            self.height = 60
            self.x = configs.window_width/2-self.width/2
            self.y = 4*configs.window_height/5

        def is_hovered(self):
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x > self.x and mouse_x < self.x+self.width and mouse_y > self.y and mouse_y < self.y+self.height:
                return True
            else:
                return False

        def clicked(self, points):
            if self.is_hovered():
                points.generate_new_initial_points()

        def draw(self):
            pygame.draw.rect(WINDOW, self.background_color, pygame.Rect(self.x, self.y, self.width, self.height))
            WINDOW.blit(self.text, (self.x+10, self.y+10))


    generate_button = GenerateButton(configs.generate_button_text, configs.generate_button_background_color)
    points = Points(configs.number_of_initial_points)

    clock = pygame.time.Clock()

    run = True
    while run:    
        WINDOW.fill("black")

        points.do_one_step()
        points.draw()

        generate_button.draw()

        pygame.display.update()

        clock.tick(configs.FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                generate_button.clicked(points)