#Douglass Jeffrey simple drawing application, 2024-06-02
from utils import *
from running import DrawModel

WHITE = (255, 255, 255)
GREY = (127, 127, 127)
BLACK = (0, 0, 0)

WIDTH = 28
HEIGHT = 28

class DrawDetermine:
    def __init__(self):
        self.width = WIDTH  #hardcode for now
        self.height = HEIGHT
        self.scaling_fact = 20
        self.drawing_grid = np.full((self.width, self.height, len(WHITE)), WHITE, dtype=int)
        self.window = pygame.display.set_mode((self.width * self.scaling_fact, self.height * self.scaling_fact))
        self.screen = pygame.Surface((self.width, self.height), flags=0)
        self.curr_cursor_pos = (0, 0)
        self.cursor_rad = 1
        self.drawing_on = False
        self.end_drawing = False
        self.model_used = DrawModel()

    def get_drawing_bw(self):
        bwgrid = np.reshape(self.drawing_grid[:, :, 0], (1, WIDTH, HEIGHT))
        #print(bwgrid.shape)
        return bwgrid

    def clear(self):
        self.drawing_grid = np.full((self.width, self.height, len(WHITE)), WHITE, dtype=int)
        return

    def drawing_loop(self):
        while not self.end_drawing:
            #print(self.drawing_grid)
            event = pygame.event.poll()

            if event.type == pygame.QUIT:
                self.end_drawing = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.drawing_on = True
                if event.button == 3:
                    self.drawing_on = False
                    self.clear()

            if event.type == pygame.MOUSEBUTTONUP:
                self.drawing_on = False

            if event.type == pygame.MOUSEMOTION:
                if self.drawing_on:
                    self.curr_cursor_pos = (np.divide(pygame.mouse.get_pos(), self.scaling_fact)).astype(int) % WIDTH
                    self.drawing_grid[self.curr_cursor_pos[0]][self.curr_cursor_pos[1]] = BLACK

            pygame.surfarray.blit_array(self.screen, self.drawing_grid)
            self.window.blit(pygame.transform.scale(self.screen, (self.width * self.scaling_fact, self.height * self.scaling_fact)), (0, 0))

            yhat = self.model_used.predict(self.get_drawing_bw())
            print(yhat)
            pygame.display.flip()



if __name__ == '__main__':
    d = DrawDetermine()
    d.drawing_loop()

