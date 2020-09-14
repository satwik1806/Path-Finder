
from collections import deque
def bfs(g,st):
    visited = [0]*(len(g))
    visited[st] = 1
    queue = deque([])
    queue.append(st)
    new = []
    while(len(queue) != 0):
        s = queue.popleft()
        new.append(s)
        for i in g[s]:
            if(visited[i] == 0):
                visited[i] = 1
                queue.append(i)
    return new


def dfs(v,visited,st,new):
    new.append(st)
    visited[st] = 1
    for i in v[st]:
        if(visited[i] == 0):
            dfs(v,visited,i,new)


### START ITERATE RECURSION ###
from types import GeneratorType
def iterative(f, stack=[]):
  def wrapped_func(*args, **kwargs):
    if stack: return f(*args, **kwargs)
    to = f(*args, **kwargs)
    while True:
      if type(to) is GeneratorType:
        stack.append(to)
        to = next(to)
        continue
      stack.pop()
      if not stack: break
      to = stack[-1].send(to)
    return to
  return wrapped_func
#### END ITERATE RECURSION ####



@iterative
def dfs(v,visited,st,new):
    new.append(st)
    visited[st] = 1
    for i in v[st]:
        if(visited[i] == 0):
            ok = yield dfs(v,visited,i,new)
    yield True


def dfsusingstack(v,visited,st,new):
    d = deque([])
    d.append(st)
    visited[st] = 1
    while(len(d) != 0):
        curr = d.pop()
        new.append(curr)
        for i in v[curr]:
            if(visited[i] == 0):
                visited[i] = 1
                d.append(i)

    return new

def dfsusingstackexample(v,st,par,cnt,p):
    d = deque([])
    d.append(st)
    visited = [0]*(len(v))
    visited[st] = 1
    new = deque([])
    while(len(d) != 0):
        curr = d.pop()
        new.append(curr)
        for i in v[curr]:
            if(visited[i] == 0):
                par[i] = curr
                visited[i] = 1
                d.append(i)

    while(len(new)!=0): #backtracing example
        curr = new.pop()
        lol = 0
        for kids in v[curr]:
            if(par[curr] == kids):
                continue
            lol+=cnt[kids]
        cnt[curr] = lol+p[curr]


ver = int(input())
edg = int(input())

v = [[]for i in range(0,ver)]
# for i in range(0,ver):
#     v.append([])

for i in range(0,edg):
    a,b = map(int,input().split())
    v[a].append(b)
    v[b].append(a)
print(v)
# visited = [0]*ver
# new = bfs(v,4)
# print(new,'bfs')

visited = [0]*ver
new = []
dfs(v,visited,0,new)
print(new)
visited = [0]*ver
new = []
print(dfsusingstack(v,visited,0,new))


# 6
# 6
# 0 1 2
# 0 3 1
# 1 2 5
# 2 3 2
# 3 4 9
# 4 5 4
# [[1, 3], [0, 2], [1, 3], [0, 2, 4], [3, 5], [4]]
