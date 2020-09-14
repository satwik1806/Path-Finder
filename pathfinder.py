RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 255, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
GREY = (128, 128, 128)
TURQUOISE = (64, 224, 208)
from heapq import *
import pygame
from math import *

window_size = 800
window = pygame.display.set_mode((window_size, window_size))
grid_size = 50  # 50x50

pygame.display.set_caption("Satwik's PathFinder ;)")

window.fill(WHITE)
gap = window_size // grid_size
blocksize = gap

class block:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.xcor = row*gap
        self.ycor = col*gap
        self.color = WHITE #initial color
        self.neighbors = []

    def makeblock(self):
        pygame.draw.rect(window,self.color,(self.xcor,self.ycor,gap,gap))

    def assign_neighbours(self,grid):
        if(self.row>0 and grid[self.row-1][self.col].color != BLACK):
            self.neighbors.append(grid[self.row-1][self.col])
        if(self.row<grid_size-1 and grid[self.row+1][self.col].color != BLACK):
            self.neighbors.append(grid[self.row+1][self.col])
        if(self.col>0 and grid[self.row][self.col-1].color!=BLACK):
            self.neighbors.append(grid[self.row][self.col-1])
        if(self.col<grid_size-1 and grid[self.row][self.col+1].color!= BLACK):
            self.neighbors.append(grid[self.row][self.col+1])


def makegridlines():
    for i in range(grid_size):
        # pygame.draw.rect(window,BLACK,(i*gap,0),(i*gap,window_size))
        pygame.draw.line(window, BLACK, (0, i * gap), (window_size, i * gap))
        for j in range(grid_size):
            # pygame.draw.rect(window,BLACK,(0,j*gap),(window_size,j*gap))
            pygame.draw.line(window, BLACK, (j * gap, 0), (j * gap, window_size))


def draw(grid):
    window.fill(WHITE)

    for i in range(len(grid)):
        for j in range(len(grid)):
            grid[i][j].makeblock()

    makegridlines()
    pygame.display.update()


def djkistra(draw,grid,st,end):
    hash = {}
    h = []
    dist = {}
    for i in range(grid_size):
        for j in range(grid_size):
            dist[grid[i][j]] = 10**9
    print(dist[st],dist[end])
    dist[st] = 0

    cnt = 0 #for error handling, '<' is not supported be=tw block and block
    heappush(h,(0,cnt,st))
    while(len(h)!=0):
        print(h)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        curr = heappop(h)[2]
        for i in curr.neighbors:
            if(dist[i] > dist[curr]+1):
                dist[i] = dist[curr]+1
                i.color = GREEN
                cnt+=1
                heappush(h,(dist[i],cnt,i))

        draw()
        if(curr!=st):
            curr.color = RED

    #djkistra is not working properly, must be some logical fault.
    #debug it
    #trace the shortest path.
    #if traced then make it an animation using anycolor showing sshortest distance.



def bfs01():
    pass #complete bfs also.

def main():
    grid = []
    for i in range(grid_size):
        temp = []
        for j in range(grid_size):
            temp.append(block(i,j))
        grid.append(temp)
    st = False
    end = False
    flag = True
    while(flag):
        draw(grid)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = False

            if(event.type == pygame.KEYDOWN):

                if(event.key == pygame.K_c):
                    grid = []
                    for i in range(grid_size):
                        temp = []
                        for j in range(grid_size):
                            temp.append(block(i,j))
                        grid.append(temp)
                    st = False
                    end = False
                else:
                    for i in range(grid_size):
                        for j in range(grid_size):
                            grid[i][j].assign_neighbours(grid)
                    if(event.key == pygame.K_d): #djkistra
                        print('WORKING')
                        djkistra(lambda:draw(grid),grid,st,end)



            else:

                if(pygame.mouse.get_pressed()[0]): #clicked left
                    x,y= pygame.mouse.get_pos()
                    i = x//gap
                    j = y//gap

                    if(not st and grid[i][j] != end):
                        st = grid[i][j]
                        grid[i][j].color = YELLOW

                    elif(not end and grid[i][j] != st):
                        end = grid[i][j]
                        grid[i][j].color = TURQUOISE

                    elif(grid[i][j] != st and grid[i][j]!=end):
                        grid[i][j].color = BLACK

                else:
                    if(pygame.mouse.get_pressed()[2]):
                        x,y = pygame.mouse.get_pos()
                        i = x//gap
                        j = y//gap

                        if(grid[i][j] == st):
                            st = False
                            grid[i][j].color = WHITE
                        elif(grid[i][j] == end):
                            end = False
                            grid[i][j].color = WHITE
                        else:
                            grid[i][j].color = WHITE


main()
















# f = True
# cnt = 0
# while (cnt != 100):
#     window.fill(WHITE)
#     for i in range(grid_size):
#         pygame.draw.line(window, BLACK, (0, i * gap), (window_size, i * gap))
#         for j in range(grid_size):
#             if ((i + j) % 2 == 1):
#                 pygame.draw.rect(window, GREEN, (i * gap, j * gap, gap, gap))
#             else:
#                 pygame.draw.rect(window, BLACK, (i * gap, j * gap, gap, gap))
#                 if(j == 2):
#                     pygame.draw.rect(window, RED, (i * gap, j * gap, gap, gap))
#             pygame.draw.line(window, BLACK, (j * gap, 0), (j * gap, window_size))
#
#     pygame.display.update()
#     cnt += 1
