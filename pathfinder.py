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
from collections import deque



window_size = 600
window = pygame.display.set_mode((window_size, window_size))
grid_size = 40  # 50x50

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
        self.color = BLACK #initial color
        self.neighbors = []

    def makeblock(self):
        pygame.draw.rect(window,self.color,(self.xcor,self.ycor,gap,gap))

    def assign_neighbours(self,grid):
        if(self.row>0 and grid[self.row-1][self.col].color != WHITE):
            self.neighbors.append(grid[self.row-1][self.col])
        if(self.row<grid_size-1 and grid[self.row+1][self.col].color != WHITE):
            self.neighbors.append(grid[self.row+1][self.col])
        if(self.col>0 and grid[self.row][self.col-1].color!=WHITE):
            self.neighbors.append(grid[self.row][self.col-1])
        if(self.col<grid_size-1 and grid[self.row][self.col+1].color!= WHITE):
            self.neighbors.append(grid[self.row][self.col+1])


def makegridlines():
    for i in range(grid_size):
        # pygame.draw.rect(window,BLACK,(i*gap,0),(i*gap,window_size))
        pygame.draw.line(window, GREY, (0, i * gap), (window_size, i * gap))
        for j in range(grid_size):
            # pygame.draw.rect(window,BLACK,(0,j*gap),(window_size,j*gap))
            pygame.draw.line(window, GREY, (j * gap, 0), (j * gap, window_size))


def draw(grid):
    window.fill(BLACK)

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
    # print(dist[st],dist[end])
    dist[st] = 0

    trackpath = {}

    cnt = 0 #for error handling, '<' is not supported be=tw block and block
    heappush(h,(0,cnt,st))
    while(len(h)!=0):
        # print(h)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        curr = heappop(h)[2]
        if(curr == end):
            while(curr in trackpath):
                curr = trackpath[curr]
                curr.color = RED
                draw()
            return

        for i in curr.neighbors:
            if(dist[i] > dist[curr]+1):
                trackpath[i] = curr
                dist[i] = dist[curr]+1
                i.color = GREEN
                cnt+=1
                heappush(h,(dist[i],cnt,i))
        # print('===========')
        draw()
        if(curr!=st):
            curr.color = ORANGE

    return
def manhaton(a,b):
    return abs(a.xcor-b.xcor)+abs(a.ycor-b.ycor)

def Astar(draw,grid,st,end):
    #f(block) = g(block)+manhaton dist of block and end
    trackpath = {}
    h = []
    cnt = 0
    f = {}
    g = {}
    for i in range(grid_size):
        for j in range(grid_size):
            f[grid[i][j]] = 10**9
            g[grid[i][j]] = 10**9

    g[st] = 0
    f[st] = g[st]+ manhaton(st,end)
    heappush(h,(f[st],cnt,st))
    while(len(h) != 0):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        curr = heappop(h)[2]

        if(curr == end):
            while(curr in trackpath):
                curr = trackpath[curr]
                curr.color = RED
                draw()
            return

        for i in curr.neighbors:
            if(g[i] > g[curr]+1):
                trackpath[i] = curr
                g[i] = g[curr]+1
                f[i] = g[i] + manhaton(i,end)
                cnt+=1
                i.color = GREEN
                heappush(h,(f[i],cnt,i))

        draw()
        if(curr != st):
            curr.color = ORANGE

    return




def bfs01(draw,grid,st,end):
    vis = {}
    for i in range(grid_size):
        for j in range(grid_size):
            vis[grid[i][j]] = False
    queue = deque([])
    trackpath = {}
    vis[st] = True
    queue.append(st)
    while(len(queue)!=0):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        curr = queue.popleft()
        if(curr == end):
            while(curr in trackpath):
                curr = trackpath[curr]
                curr.color = RED
                draw()
            return

        for i in curr.neighbors:
            if(not vis[i]):
                vis[i] = True
                i.color = GREEN
                trackpath[i] = curr
                queue.append(i)

        draw()
        if(curr != st):
            curr.color = ORANGE
    return

def dfsusingstack(draw,grid,st,end):
    vis = {}
    for i in range(grid_size):
        for j in range(grid_size):
            vis[grid[i][j]] = False
    stack = deque([])
    stack.append(st)
    vis[st] = True
    trackpath = {}
    while(len(stack)!=0):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        curr = stack.pop()
        if(curr == end):
            while(curr in trackpath):
                curr = trackpath[curr]
                curr.color = RED
                draw()
            return

        for i in curr.neighbors:
            if(not vis[i]):
                trackpath[i] = curr
                i.color = GREEN
                vis[i] = True
                stack.append(i)

        draw()
        if(curr != st):
            curr.color = ORANGE
    return

def eucledean(a,b):
    return ((a.xcor-b.xcor)**2 + (a.ycor-b.ycor)**2)**(0.5)

def bestfirstsearch(draw,grid,st,end):
    vis = {}
    val = {}
    for i in range(grid_size):
        for j in range(grid_size):
            vis[grid[i][j]] = False
            val[grid[i][j]] = eucledean(grid[i][j],end)
    trackpath = {}
    have = []
    cnt = 0
    vis[st] = True
    heappush(have,(val[st],cnt,st))
    while(len(have)!=0):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        curr = heappop(have)[2]
        if(curr == end):
            while(curr in trackpath):
                curr = trackpath[curr]
                curr.color = RED
                draw()
            return

        for i in curr.neighbors:
            if(not vis[i]):
                i.color = GREEN
                trackpath[i] = curr
                vis[i] = True
                cnt+=1
                heappush(have,(eucledean(i,end),cnt,i))
        draw()
        if(curr != st):
            curr.color = ORANGE
    return


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

                for i in range(grid_size):
                        for j in range(grid_size):
                            grid[i][j].assign_neighbours(grid)

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

                    if(event.key == pygame.K_d): #djkistra
                        djkistra(lambda:draw(grid),grid,st,end)
                        continue
                    if(event.key == pygame.K_a): #Astar
                        Astar(lambda:draw(grid),grid,st,end)
                        continue
                    if(event.key == pygame.K_b): #bfs
                        bfs01(lambda:draw(grid),grid,st,end)
                        continue
                    if(event.key == pygame.K_f): #dfs
                        dfsusingstack(lambda : draw(grid),grid,st,end)
                        continue
                    if(event.key == pygame.K_s): #best first seach
                        bestfirstsearch(lambda :draw(grid),grid,st,end)
                        continue



            if(pygame.mouse.get_pressed()[0]): #clicked left
                x,y= pygame.mouse.get_pos()
                i = x//gap
                j = y//gap

                if(not st and grid[i][j] != end):
                    st = grid[i][j]
                    grid[i][j].color = YELLOW

                elif(not end and grid[i][j] != st):
                    end = grid[i][j]
                    grid[i][j].color = PURPLE

                elif(grid[i][j] != st and grid[i][j]!=end):
                    grid[i][j].color = WHITE

            else:
                if(pygame.mouse.get_pressed()[2]):
                    x,y = pygame.mouse.get_pos()
                    i = x//gap
                    j = y//gap

                    if(grid[i][j] == st):
                        st = False
                        grid[i][j].color = BLACK
                    elif(grid[i][j] == end):
                        end = False
                        grid[i][j].color = BLACK
                    else:
                        grid[i][j].color = BLACK


    pygame.quit()
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
